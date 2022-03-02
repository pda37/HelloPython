# 1.导包unittest requests
import unittest
import requests
# import json


# 2.新建测试类--> unittest.TestCase
class TestLogin(unittest.TestCase):
    # 3.所有test方法执行之前，都会先执行setUp
    def setUp(self):
        # 获取session对象
        self.session = requests.session()
        # 登录url
        self.url_login = "https://test.gelonghui.com/api/user/login/v2"
        # # 验证码url
        # self.url_verify = ""

    # 4.所有test方法执行之后，都会执行tearDown
    def tearDown(self):
        # 关闭session
        self.session.close()

    # 5.登陆成功用例
    def test_login_success(self):
        # # 请求验证码--获取cookies
        # self.session.get(self.url_verify)
        # 请求登录
        payload = {
                "userName": "18301637969",
                "password": "111111",
                }
        # headers = {'Content-Type': 'application/json'}
        # # 方式一：对dict进行编码
        # r = self.session.post(self.url_login, data=json.dumps(payload), headers=headers)
        # 方式二：直接使用json参数
        r = self.session.post(self.url_login, json=payload)
        # 断言
        try:
            self.assertEqual(200, r.json()["statusCode"])
            print('登录成功 pass')
        except AssertionError as e:
            print(e)

    # 6.登陆失败 账号不存在用例
    def test_username_not_exist(self):
        payload = {
                "userName": "18301637968",
                "password": "111111",
                }
        r = self.session.post(self.url_login, json=payload)
        # 断言
        try:
            self.assertEqual("登录失败，用户名或者密码错误", r.json()["message"])
            print('账号错误 pass')
        except AssertionError as e:
            print(e)

    # 7.登陆失败 密码错误用例
    def test_password_error(self):
        payload = {
                "userName": "18301637969",
                "password": "123456",
                }
        r = self.session.post(self.url_login, json=payload)
        # 断言
        try:
            self.assertEqual("登录失败，用户名或者密码错误", r.json()["message"])
            print('密码错误 pass')
        except AssertionError as e:
            print(e)


# 导入时不被执行
if __name__ == '__main__':
    unittest.main()
