import random
import requests
from django.conf import settings
import environ
env = environ.Env()
environ.Env.read_env()


def send_otp_to_phone(phone_number):
    try:
        otp = random.randint(100000, 999999)
        url = 'https://api.smsfly.uz/'
        credentials = {
            "key": env("token"), #"8f527b2c-e8d7-11ec-a71e-0242ac120002",
            "phone": str(phone_number),
            "message": str(otp)
        }
        response = requests.post(url, json=credentials)
        return otp
    except Exception as e:
        print(e)
    return None
