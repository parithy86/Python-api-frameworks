import requests

from flaskhttp_server.constants.constants import Constants


def get_crypto_details(request):
    response = requests.get(Constants.URL.format("bitcoin"))
    if response.status_code in Constants.RESPONSE_CODES_SUCCESS:
        return response.text, response.status_code

    else:
        return {"status": "failure"}, response.status_code


def get_crypto(request):
    print(request)
    response = requests.get(Constants.URL.format(request.get('coin')))
    if response.status_code in Constants.RESPONSE_CODES_SUCCESS:
        return response.text, response.status_code

    else:
        return {"status": "failure"}, response.status_code
