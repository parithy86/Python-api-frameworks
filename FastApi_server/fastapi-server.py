from fastapi import FastAPI, Response

from services import crypto_info
# import requests
#
# from FastApi_server.constants.constants import Constants
# from FastApi_server.utils.helpers_util import read_yaml_configs


app = FastAPI()


@app.get("/health")
async def health():
    return {"REST API using Fast API framework, Health Ok "}

# async def run_services(request):
#     service_name = request.match_info['service_name']
#     service_details = read_yaml_configs(os.path.abspath('./configs/service_config.yaml'))
#     service_config_details = service_details['services'].get(service_name)
#
#     execute_func = getattr(importlib.import_module('aiohttp_server.services.' + service_config_details['package_name']),
#                            service_config_details['function_name'])
#
#     resp, resp_code = await execute_func(request)
#
#     return web.Response(text=resp, content_type=Constants.CONTENT_TYPE)

#
# @app.post("/v1/crypto/info")
# async def get_crypto_info(coin_info: Crypto):
#     print(coin_info.crypto_name)
#     url = "https://api.coingecko.com/api/v3/coins/bitcoin?localization=false&tickers=false&market_data=false&community_data=false&developer_data=false&sparkline=false"
#     response = requests.get(url)
#     if response.status_code in [200, 201]:
#         return Response(content=response.text, media_type="application/json")
#     else:
#         return {"status": "failure", "status_code": response.status_code}

app.include_router(crypto_info.router)
app.include_router(
    prefix="/v1/crypto",
    tags=["users"],
    responses={418: {"description": "I'm a teapot"}},
)
