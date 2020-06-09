class Register_Api:
    def __init__(self):
        self.verify_url="http://127.0.0.1/index.php/Home/User/verify/type/user_reg.html"
        self.register_url="http://127.0.0.1/index.php/Home/User/reg.html"
    def get_verify(self,session):
        return session.get(url=self.verify_url)
    def register(self,session,data):
        return session.post(url=self.register_url,data=data)
class Login_Api:
    def __init__(self):
        self.login_verify_url="http://127.0.0.1/index.php?m=Home&c=User&a=verify"
        self.login_url="http://127.0.0.1/index.php?m=Home&c=User&a=do_login"
    def get_verify(self,session):
        return session.get(url=self.login_verify_url)
    def login(self,session,data):
        return session.post(url=self.login_url,data=data)
