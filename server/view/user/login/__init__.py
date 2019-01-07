import os
import json
import requests

from flask import jsonify


def validate_email(email):
    print(type(email))
    print("a", os.getenv('EMAIL_VALIDATE_KEY'))
    response = requests.request(
        method="GET",
        url="https://api.mailgun.net/v3/address/validate",
        auth=("api", os.getenv('EMAIL_VALIDATE_KEY')),
        params={"address": email}
    ).json()
    print(response)
    return response['is_valid']
