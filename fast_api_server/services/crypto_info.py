import requests

from fast_api_server.constants.constants import Constants


async def get_crypto_details(request):
    response = requests.get(Constants.URL.format("bitcoin"))
    if 'error' in response.json():
        return {"status": "failure"}, Constants.RESPONSE_500
    else:
        if response.status_code in Constants.RESPONSE_CODES_SUCCESS:
            return response.text, response.status_code
        else:
            return {"status": "failure"}, response.status_code


async def get_crypto(request):
    response = requests.get(Constants.URL.format(request.get('coin')))
    if 'error' in response.json():
        return {"status": "failure"}, Constants.RESPONSE_500
    else:
        if response.status_code in Constants.RESPONSE_CODES_SUCCESS:
            return response.text, response.status_code
        else:
            return {"status": "failure"}, response.status_code
