from urllib import response
import requests





auth = '401ea27ea67a248b26a153291ddcc65e17f7b324e98c310a33f634a3e668156c'


baseUrl = "https://platform-api.services.nevaya.net/v1/auth"

responce = requests.post(url=baseUrl, json={"token": auth})

print(responce.content)

headers = {"Authorization": "JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uX2lkIjoiZGIzOTEzNWMtOWJlOC00ZjdlLWI5MGYtYzVmNmRhM2IwNzA5IiwidXNlcl9pZCI6IjYzOTVlYjM2LWI4YTItNDkyMy1iYzQ4LWEwZjY5ZDNjZDVkOSIsImlhdCI6MTY1MjM4ODM3OSwiZXhwIjoxNjUyNDc0Nzc5fQ.BVdg2JmXvDfgHDWmb81_kvZzBW0uOL0V0ni_P2pVpIY"}


r1 = requests.get(url="https://platform-api.services.nevaya.net/v1/cast/chromecasts?per_page=200", headers=headers)

print(r1.content)