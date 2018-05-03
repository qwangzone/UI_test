#coding=utf-8
from selenium import webdriver
import unittest, os, sys

dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
import createprojectpage, loginpage


class CreateProTest(unittest.TestCase):
    '''创建标的测试'''

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.implicitly_wait(10)
        # 后台建标需先登录，登录操作
        self.lgpg = loginpage.LoginPage(self.dr)
        self.lgpg.open()
        self.lgpg.login()
        # 引用后台新建标的page
        self.create_page = createprojectpage.CreateNew(self.dr)

    def test_create_new(self):
        self.create_page.open()
        self.create_page.createnewproject()
        success_msg = self.create_page.get_save_success_msg()
        self.assertIn("项目保存成功", success_msg)

    def tearDown(self):
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
