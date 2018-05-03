#coding=utf-8
from selenium import webdriver
import unittest, os, sys

dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
import copyprojectpage, loginpage, createprojectpage


class CopyProTest(unittest.TestCase):
    '''测试复制标的'''

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
        self.create_page.open()
        self.copy_page = self.create_page.createnewproject()

    def test_copypro(self):
        self.copy_page.save_proinfo()
        success_msg = self.copy_page.get_save_success_msg()
        self.assertIn("项目保存成功", success_msg)

    def tearDown(self):
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
