from flask import Flask
from flask import request
from flask import make_response
import time
import base64

app = Flask(__name__)

@app.route('/<base>/<type>/<int:status>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def stub(base, type, status):
    wait = int(request.args.get('wait', '0'))
    content_length = int(request.args.get('content-length', '1024'))

    time.sleep(int(wait))

    contents = "hello world" * ( int(content_length / 10 ) + 1 )
    response_text = contents[0:int(content_length)]
    response = make_response(response_text, status)
    response.headers["mime-type"] = "/".join([base, type])

    return response
