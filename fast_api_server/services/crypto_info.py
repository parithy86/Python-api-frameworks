import requests

from fast_api_server.constants.constants import Constants


async def get_crypto_details():
    response = requests.get(Constants.URL)
    if response.status_code in Constants.RESPONSE_CODES_SUCCESS:
        return response.text, response.status_code

    else:
        return {"status": "failure"}, response.status_code
