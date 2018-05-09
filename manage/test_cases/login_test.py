#coding=utf-8
import unittest, os, sys
import time

dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
import loginpage
from selenium import webdriver


class LoginTest(unittest.TestCase):
    '''测试后台登录'''
    @classmethod
    def setUpClass(self):
        self.dr = webdriver.Chrome()
        self.lgpg = loginpage.LoginPage(self.dr)
        self.lgpg.open()

    # 登录失败（用户名或密码错误）
    def test1_username_error(self):
        '''用户名或密码错误'''
        self.lgpg.login(username="errorusername")
        self.error_msg = self.lgpg.get_error_msg()
        self.assertEqual(self.error_msg, "用户名或密码不正确")

    # 登录成功
    def test2_login_success(self):
        '''登录成功'''
        self.lgpg.login(username="caihongguang")
        self.success = self.lgpg.get_login_success_msg()
        time.sleep(5)

        # print(self.success)
        self.assertIn("欢迎", self.success)

    @classmethod
    def tearDownClass(self):
        self.dr.quit()
        self.dr.title


if __name__ == '__main__':
    unittest.main()
