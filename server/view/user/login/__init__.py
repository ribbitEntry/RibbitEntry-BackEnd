import os
import requests

from flask import jsonify


def validate_email(email):
    responsed = requests.request(
        method="GET",
        url="https://api.mailgun.net/v3/address/validate",
        auth=("api", os.getenv('EMAIL_VALIDATE_KEY')),
        params={"address": str(email)}
    ).json()
    print(os.getenv('EMAIL_VALIDATE_KEY'))
    print(responsed)
    print(dict(responsed)['is_valid'])
    return dict(responsed)['is_valid']
