import os
import requests
import urllib3
import argparse

import boto3

urllib3.disable_warnings()




def get_devices():

    s = requests.session()
    url = "https://nevaya-auth.auth.eu-west-1.amazoncognito.com/login?client_id=1v8ng68o5ene0365fg3a5dcuuv&redirect_uri=https%3A%2F%2Fportal.nevaya.net%2Fauth%2Fcognito%2Fcallback&response_type=code&state=752b31b64aaaec84b7d466d63eaf2e246f164329a0266aef"
    data = {"username": "gareth.cheyne@nz.harveynorman.com", "password": "Ribl#t19bo!!"}

    username = "gareth.cheyne@nz.harveynorman.com"
    password = "Ribl#t19bo!!"

    responce = s.post(url=url, json=data)

    print(responce.content)

get_devices()