from flask import Flask
from flask import request
from flask import make_response
import time

app = Flask(__name__)

@app.route('/<base>/<type>/<int:status>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def stub(base, type, status):
    wait = int(request.args.get('wait', '0'))
    time.sleep(int(wait))

    response_text = "Hello world"
    response = make_response(response_text, status)
    response.headers["mime-type"] = "/".join([base, type])

    return response
