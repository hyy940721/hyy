# # 导包
# import time
# import unittest
# from BeautifulReport import BeautifulReport
# # 测试套件
#
# suite= unittest.TestLoader().discover("./script",pattern="test_enroll*.py")
# # 定义报告名
# file_name="test-{}.html".format(time.strftime("%Y%m%d%H%M%S"))
# # 运行生成测试报告
# BeautifulReport(suite).report(filename=file_name,description="tpshop注册与登录",log_path="./report")


# 导包
import time
import unittest
from BeautifulReport import BeautifulReport
# 测试套件
suite=unittest.TestLoader().discover("./script",pattern="test_register*.py")
# 定义报告名
report_name="test-{}.html".format(time.strftime("%Y%m%d%H%M%S"))
# 生成测试报告
BeautifulReport(suite).report(filename=report_name,description="tpshop注册与登陆",log_path="./report")