# 注册
# 导包
import requests
# 实例化session
session=requests.Session()
# 用session获取验证码的接口请求
verify_url="http://127.0.0.1/index.php/Home/User/verify/type/user_reg.html"
session.get(url=verify_url)
# 用session发送注册的接口请求
enroll_url="http://127.0.0.1/index.php/Home/User/reg.html"
data={"auth_code":"TPSHOP","scene":"1","username":"13445201413","verify_code":"8888",
      "password":"519475228fe35ad067744465c42a19b2","password2":"519475228fe35ad067744465c42a19b2"}
response_enroll=session.post(url=enroll_url,data=data)
# 输出注册结果
print("注册结果为: ",response_enroll.json())
# 关闭session
session.close()

# 登录
# 导包
import requests
# 实例化session
session=requests.Session()
# 获取登录的验证码接口
login_verify_url="http://127.0.0.1/index.php?m=Home&c=User&a=verify"
session.get(login_verify_url)
# 用session发送登录的接口请求
login_url="http://127.0.0.1/index.php?m=Home&c=User&a=do_login"
data={"username":"13800138006","password":"123456","verify_code":"8888"}
response_login=session.post(url=login_url,data=data)
print("登录的结果为: ",response_login.json())
# 关闭session
session.close()













