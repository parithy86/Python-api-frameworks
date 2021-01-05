import importlib
import os
from aiohttp import web

from aiohttp_server.constants.constants import Constants
from aiohttp_server.utils.helpers_util import read_yaml_configs


async def health(request):
    return web.Response(text="<h1> Async Rest API using aiohttp : Health OK </h1>",
                        content_type='text/html')


async def run_services(request):
    service_name = request.match_info['service_name']
    service_details = read_yaml_configs(os.path.abspath('./configs/service_config.yaml'))
    service_config_details = service_details['services'].get(service_name)

    execute_func = getattr(importlib.import_module('aiohttp_server.services.' + service_config_details['package_name']),
                           service_config_details['function_name'])

    resp, resp_code = await execute_func(request)

    return web.Response(text=resp, content_type=Constants.CONTENT_TYPE)


async def init():
    app = web.Application()
    app.router.add_get("/", health)
    app.router.add_post("/v1/services/{service_name}", run_services)
    return app


if __name__ == "__main__":
    application = init()
    web.run_app(application, port=8000)
