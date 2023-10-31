from flask import Flask, render_template, request
from waitress import serve


app = Flask(__name__)

@app.route('/test' , methods=['POST'])
def gebruiker():
    result = request.form
    print("Example cpu received:", result['avg_cpu_perc']) 
    print("Everything received: ", result)
    return "Thank you!"


if __name__ == '__main__':
    serve(app, host='192.168.178.84', port=5000, threads=5)
