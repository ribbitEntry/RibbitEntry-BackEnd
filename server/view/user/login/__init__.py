import os
import requests


def validate_email(email):
    responsed = requests.get(
        url=str(os.getenv('EMAIL_VALIDATE_URL')),
        auth=("api", str(os.getenv('EMAIL_VALIDATE_KEY'))),
        params={"address": str(email)}
    ).json()
    return dict(responsed)['is_valid']
