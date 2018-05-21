import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
#print(dir)
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
import loginpage
import myaccountpage
#from selenium import webdriver
from driver import my_driver
import unittest, time

class LoginTest(unittest.TestCase):
    '''测试前台登录'''

    @classmethod
    def setUpClass(self):
        self.dr = my_driver()
        self.lg = loginpage.LoginPage(self.dr)
        self.mp = myaccountpage.MyacountPage(self.dr)
        self.lg.open()

    def test1_username_error(self):
        """用户名错误"""
        self.lg.login(username='11111', password='123456', yanzhengma='1')
        time.sleep(3)
        text1 = self.lg.mobilem_error_text()
        self.assertEqual(text1, u'*该账户不存在')

    def test2_password_error(self):
        """登录密码错误"""
        self.lg.login(username='13658524695', password='111111', yanzhengma='1')
        time.sleep(3)
        text2 = self.lg.loginPassm_error_text()
        print(text2)
        self.assertEqual(text2, u'*密码与账户不匹配')

    def test3_login_success(self):
        """登录成功"""
        self.lg.login(username='13658524695', password='123456', yanzhengma='1')
        text3 = self.mp.login_user()
        print(text3)
        self.assertIn(u'您好', text3)


    @classmethod
    def tearDownClass(self):
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()




