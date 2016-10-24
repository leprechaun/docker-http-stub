from flask import Flask
from flask import request
import time

app = Flask(__name__)

@app.route('/<int:status>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def stub(status):
    wait = request.args.get('wait', '0')
    wait = int(wait)
    time.sleep(int(wait))

    return 'Hello, World!', status
