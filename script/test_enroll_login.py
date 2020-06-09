# 导包
import unittest
import requests
from api.enroll_login_api import Enroll, Login

class TpshopTest(unittest.TestCase):
    # 定义类级别初始化fixture,获取url
    @classmethod
    def setUpClass(cls):
        cls.session=requests.Session()
        cls.enroll_api=Enroll()
        cls.login_api=Login()
    # 定义类级别销毁fixture,关闭session
    @classmethod
    def tearDownClass(cls):
        if cls.session is None:
            cls.session.close()
    # 定义注册测试方法
    def test_enroll(self):
        # 获取验证码
        self.enroll_api.get_verify(self.session)
        # 获取注册接口
        data = {"auth_code": "TPSHOP", "scene": "1", "username": "13565201613", "verify_code": "8888",
                "password": "519475228fe35ad067744465c42a19b2", "password2": "519475228fe35ad067744465c42a19b2"}
        response_enroll = self.enroll_api.enroll(self.session, data=data)
        print("注册的结果为: ",response_enroll.json())
        # 断言
        self.assertEqual(1,response_enroll.json().get("status"))
        self.assertEqual("注册成功",response_enroll.json().get("msg"))
        self.assertEqual(200,response_enroll.status_code)
    # 定义登录的测试方法
    def test_login(self):
        # 获取验证码
        self.login_api.get_verify(self.session)
        # 获取登录接口
        data = {"username":"13800138006","password":"123456","verify_code":"8888"}
        response_login = self.login_api.login(self.session, data=data)
        print("登陆的结果为: ", response_login.json())
        # 断言
        self.assertEqual(1, response_login.json().get("status"))
        self.assertIn("登陆成功", response_login.json().get("msg"))
        self.assertEqual(200, response_login.status_code)