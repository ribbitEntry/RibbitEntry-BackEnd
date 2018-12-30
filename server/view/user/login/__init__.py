import requests

from os import getenv


def validate_email(email):
    responsed = requests.get(
        getenv('EMAIL_VALIDATE_URL'),
        auth=("api", getenv('EMAIL_VALIDATE_KEY')),
        params={"address": str(email)}
    ).json()
    return dict(responsed)['is_valid']
