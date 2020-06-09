class Enroll:
    def __init__(self):
        self.verify_url="http://127.0.0.1/index.php/Home/User/verify/type/user_reg.html"
        self.enroll_url="http://127.0.0.1/index.php/Home/User/reg.html"
    def get_verify(self,session):
        return session.get(self.verify_url)
    def enroll(self,session,data):
        return session.post(self.enroll_url,data=data)


class Login:
    def __init__(self):
        self.login_verify_url = "http://127.0.0.1/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://127.0.0.1/index.php?m=Home&c=User&a=do_login"
    def get_verify(self,session):
        return session.get(self.login_verify_url)
    def login(self,session,data):
        return  session.post(self.login_url,data=data)