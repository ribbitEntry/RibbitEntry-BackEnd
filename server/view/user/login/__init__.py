import os
import requests


def validate_email(email):
    responsed = requests.get(
        url="https://api.mailgun.net/v3/address/validate",
        auth=("api", str(os.getenv('EMAIL_VALIDATE_KEY'))),
        params={"address": str(email)}
    ).json()
    return dict(responsed)['is_valid']
