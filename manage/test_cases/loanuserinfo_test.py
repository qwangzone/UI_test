#coding=utf-8
from selenium import webdriver
import unittest, os, sys

dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
from loginpage import LoginPage
from createprojectpage import CreateNew

class LoanUserInfoTest(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.implicitly_wait(10)
        # 后台需先登录
        self.login_p = LoginPage(self.dr)
        self.login_p.open()
        self.login_p.login()
        # 创建新标
        self.createpro_p = CreateNew(self.dr)
        self.createpro_p.open()
        self.createpro_p.createnewproject()

    def test_loanuserinfo(self):
        self.loanuserinfo_p = self.createpro_p.loanuserinfo()
        self.loanuserinfo_p.submitform()

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()


