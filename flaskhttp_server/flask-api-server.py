import importlib
import os

from flask import Flask, request, json

from flaskhttp_server.utils.helpers_util import read_yaml_configs

app = Flask(__name__)


@app.route('/', methods=['GET'])
def health():
    return "<h1> Async Rest API using aiohttp : Health OK </h1>"


@app.route('/v1/services/<service_name>', methods=['POST'])
def run_services(service_name):
    service_details = read_yaml_configs(os.path.abspath('./configs/service_config.yaml'))
    service_config_details = service_details['services'].get(service_name)

    execute_func = getattr(
        importlib.import_module('flaskhttp_server.services.' + service_config_details['package_name']),
        service_config_details['function_name'])
    resp, resp_code = execute_func(json.loads(request.data))
    return resp


if __name__ == "__main__":
    app.run(port=8000)
