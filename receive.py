from flask import Flask, render_template, request
from waitress import serve
import sqlite3
import io
import base64
import matplotlib.pyplot as plt

DATABASE = r'/home/eipl/Documents/automation/database/stats.db'


app = Flask(__name__)

@app.route('/receive.py' , methods=['POST'])
def gebruiker():
    result = request.form
    cpu_data = result['cpu_perc']
    disk_data = result['free_diskspace']
    memory_data = result['memory_perc']
    time = result['time']
    fqdn = result['fqdn']
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data (cpu, disk, memory, time, fqdn) VALUES (?, ?, ?, ?, ?)", (cpu_data, disk_data, memory_data, time, fqdn))
    conn.commit()
    conn.close()

    return "Thank you!"

@app.route('/')
def home():
    return render_template ('home.html')


def get_data():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT MAX(seq) AS hoogste_getal FROM data")
    highest_value = c.fetchone()[0]  # Fetching the highest value from the result
    start = highest_value - 15  # Subtracting 10 from the highest value
    query = "SELECT * FROM data WHERE seq >= ? ORDER BY seq ASC"
    c.execute(query, (start,))
    data = c.fetchall()
    conn.close()
    return data

def extract_time(row):
    timestamp = str(row[4])  # Ensure the timestamp is converted to a string
    time = timestamp[-8:-3]  # Get the last 5 characters (hh:mm)
    return time

# Function to generate the graph
def generate_graph():
    data = get_data()
    time = [extract_time(row) for row in data][::-1]  # Reversing x-axis values for correct order
    seq = [row[0] for row in data][::-1]  # Assuming the first column represents 'seq'
    cpu = [row[1] for row in data][::-1]  # Assuming the second column represents CPU
    memory = [row[2] for row in data][::-1]  # Assuming the third column represents memory
    disk = [row[3] for row in data][::-1]  # Assuming the fourth column represents disk
    fqdn = data[0][5]  # Fetch the FQDN from the first record only

    y_min = 0
    y_max = max(100, max(max(cpu), max(memory), max(disk)))

    plt.figure(figsize=(8, 6))
    plt.plot(seq, cpu, 'r', label='CPU')
    plt.plot(seq, memory, 'b', label='Memory')
    plt.plot(seq, disk, 'orange', label='Disk')
    
    plt.xlabel('Time')  # Set x-axis label to Time
    plt.ylabel('Percentage')
    plt.legend()
    
    plt.title(f'FQDN: {fqdn}', fontsize=12, weight='bold')
    plt.ylim(y_min, y_max)
    
    plt.xticks(seq, time, rotation='vertical')  # Set x-axis ticks to display 'time' on every 'seq'

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return f'data:image/png;base64,{graph_url}'



@app.route('/data')
def data():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(" SELECT * FROM data WHERE seq = (SELECT MAX(seq) FROM data);" )
    result = cursor.fetchone()
    cpu = result[1]
    memory = result[2]
    disk = result[3]
    name = result[5]
    time = result[4]
    conn.close()
    graph = generate_graph()
    return render_template('data.html', cpu=cpu, memory=memory, disk=disk, name=name, time=time, graph=graph)

if __name__ == '__main__':
    serve(app, host='192.168.178.84', port=5001, threads=5)
    #app.run(host=0.0.0.0, debugmode=True, port=5001)
