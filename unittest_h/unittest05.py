import requests
import re

# 使用正则提取登录接口响应头中的cookie，并加入到其他请求的请求头
url_login = "https://test.gelonghui.com/api/user/login/v2"
url_user = 'https://test.gelonghui.com/api/user/get/v2'
payload = {
        "userName": "18301637969",
        "password": "111111",
        }
r1 = requests.post(url_login, json=payload)
print(r1.headers['Set-Cookie'], type(r1.headers['Set-Cookie']))
# 使用正则提取登录接口响应头中的cookie
cookies = re.search('user_token=(.*?);', r1.headers['Set-Cookie']).group()[:-1]
headers = {'Cookie': cookies}
r2 = requests.get(url_user, headers=headers)
print(r2.status_code, '\n', r2.json(), '\n', r2.request.headers)
