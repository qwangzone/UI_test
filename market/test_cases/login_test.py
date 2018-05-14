#coding=utf-8
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
#print(dir)
sys.path.append(dir + "/pages")
import loginpage
from selenium import webdriver
import unittest, time

class LoginTest(unittest.TestCase):
    '''测试前台登录'''

    @classmethod
    def setUpClass(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.lg = loginpage.LoginPage(self.dr)
        self.lg.open()

    #用户名错误
    def test1_username_error(self):
        self.lg.login(username='11111', password='123456')
        time.sleep(3)
        text1 = self.lg.mobilem_error_text()
        self.assertEqual(text1, u'*该账户不存在')

    #登录密码错误
    def test2_password_error(self):
        self.lg.login(username='13658524695', password='111111')
        time.sleep(3)
        text2 = self.lg.loginPassm_error_text()
        print(text2)
        self.assertEqual(text2, u'*密码与账户不匹配')

    #登录成功
    def test3_login_success(self):
        self.lg.login(username='13658524695', password='123456')
        time.sleep(5)
        text3 = self.lg.user_success_text()
        #print(text3)
        self.assertIn(u'您好', text3)


    @classmethod
    def tearDownClass(self):
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()




