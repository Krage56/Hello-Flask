from app import app
from flask import request
from flask import Response
import json
from app.logic.json_generator import get_random_json
from app.logic.find_matches import get_matches


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
    except KeyError:
        return Response(json.dumps({}))
    if lvl < 0 or num_keys < 0:
        return Response(json.dumps({}))

    j_data = get_random_json(lvl, num_keys)
    return Response(j_data)


@app.route('/find', methods=['GET'])
def find_matches():
    try:
        val = request.args["value"]
    except KeyError:
        return Response(json.dumps({}))

    j_data = request.get_json()
    if j_data is None:
        return Response(json.dumps({}))
    return Response(json.dumps(get_matches(val, j_data)))
