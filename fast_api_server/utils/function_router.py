import os
import importlib
from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

from fast_api_server.utils.helpers_util import read_yaml_configs

router = APIRouter()


@router.get('/{function_name}', response_class=JSONResponse)
@router.post('/{function_name}', response_class=JSONResponse)
async def run_services(function_name: str):
    service_details = read_yaml_configs(os.path.abspath('./configs/service_config.yaml'))
    service_config_details = service_details['services'].get(function_name)
    execute_func = getattr(
        importlib.import_module('fast_api_server.services.' + service_config_details['package_name']),
        service_config_details['function_name'])

    resp, resp_code = await execute_func()

    if resp_code in [200, 201]:
        return Response(content=resp, media_type="application/json")
    else:
        return {"status": "failure", "status_code": resp.status_code}
