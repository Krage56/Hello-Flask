from app import app
from flask import request
from flask import Response
import json
from app.logic.json_generator import get_random_json


@app.route('/keys', methods=['GET'])
def keys_parser():
    j_data = request.get_json()
    return json.dumps(list(j_data.keys()))


@app.route('/generate', methods=['GET'])
def generate_random_json():
    params = request.args
    try:
        lvl = int(params["level"])
        num_keys = int(params["numkeys"])
    except ValueError:
        return Response(json.dumps({}))
    if lvl < 0 or num_keys < 0:
        return Response(json.dumps({}))

    j_data = get_random_json(lvl, num_keys)
    return Response(j_data)
