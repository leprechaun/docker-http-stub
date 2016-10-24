from flask import Flask
from flask import request
import time

app = Flask(__name__)

@app.route('/<int:status>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def stub(status):
    wait = int(request.args.get('wait', '0'))
    time.sleep(int(wait))

    return 'Hello, World!', status
