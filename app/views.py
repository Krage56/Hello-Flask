from app import app
from flask import request
import json

@app.route('/keys', methods=['GET'])
def keys_parser():
    j_data = request.get_json()
    return json.dumps(list(j_data.keys()))
