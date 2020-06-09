import unittest

import requests


class UnittestTest(unittest.TestCase):
    def setUp(self):
        self.login_url="http://ihrm-test.itheima.net/api/sys/login"
    def tearDown(self):
        pass
    def test01_login(self):
        data={"mobile":"13800000002","password":"123456"}
        response=requests.post(url=self.login_url,json=data)
        print(response.json())
        self.assertIn("操作成功",response.json().get("message"))
