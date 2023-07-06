
from flask import Flask
from flask import request

import json
import subprocess

app = Flask(__name__)

#@app.route('/')
@app.route('/', methods=['POST', 'GET'])
def index():
    print("hello world")
    if request.method == 'POST':
        do_notice()
    return "ok"

def do_notice():
    _data = request.get_data()
    data = json.loads(_data)
    #subprocess.call(['python3', "./tools/SendICNotice.py", output])
    print(data)

if __name__ == '__main__':
    app.run()
