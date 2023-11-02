from flask import Flask, render_template, request
from waitress import serve
import sqlite3
import io
import base64
import schedule
import matplotlib.pyplot as plt

DATABASE = r'/home/eipl/Documents/automation/database/stats.db'


app = Flask(__name__)

@app.route('/test.py' , methods=['POST'])
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
    return render_template('data.html', cpu=cpu, memory=memory, disk=disk, name=name, time=time)

if __name__ == '__main__':
    serve(app, host='192.168.178.84', port=5001, threads=5)
    #app.run(host=0.0.0.0, debugmode=True, port=5001)
