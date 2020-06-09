import unittest
import requests
from parameterized import parameterized

from api.register_login_api import Register_Api, Login_Api
from utils_zuoye import insert_data


class TpshopTest(unittest.TestCase):
    def setUp(self):
        self.session=requests.Session()
        self.register_api=Register_Api()
        self.login_api=Login_Api()
    def tearDown(self):
        if self.session is None:
            self.session.close()
    @parameterized.expand(insert_data)
    def test_register_login(self,username,reg_password,login_password,status,reg_msg,login_msg,http_code):
        # 获取验证码
        self.register_api.get_verify(self.session)
        # 获取注册接口
        data = {"auth_code": "TPSHOP", "scene": "1", "username": username, "verify_code": "8888",
                "password": reg_password, "password2": reg_password}
        response_register=self.register_api.register(self.session,data=data)
        print("注册的结果为: ",response_register.json())
        # 断言结果
        self.assertEqual(status,response_register.json().get('status'))
        self.assertIn(reg_msg,response_register.json().get('msg'))
        self.assertEqual(http_code,response_register.status_code)
        # 获取验证码
        self.login_api.get_verify(self.session)
        # 获取登录接口
        data = {"username": username, "password": login_password, "verify_code": "8888"}
        response_login=self.login_api.login(self.session,data=data)
        print("登陆的结果为: ",  response_login.json())
        # 断言
        self.assertEqual(status,response_login.json().get('status'))
        self.assertIn(login_msg,response_login.json().get('msg'))
        self.assertEqual(http_code,response_login.status_code)