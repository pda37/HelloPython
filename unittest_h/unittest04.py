import requests

# 使用 Session() 跨请求保持cookie
url_login = "https://test.gelonghui.com/api/user/login/v2"
url_user = 'https://test.gelonghui.com/api/user/get/v2'
payload = {
        "userName": "18301637969",
        "password": "111111",
        }
session = requests.Session()
r1 = session.post(url_login, json=payload)
r2 = session.get(url_user)
print(r2.status_code, '\n', r2.json(), '\n', r2.request.headers)
