from selenium import webdriver
import unittest, os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
import createproject_page, login_page

class CreateProTest(unittest.TestCase):
    def setUp(self):
        self.diver = webdriver.Chrome()
        self.diver.maximize_window()
        self.diver.implicitly_wait(10)
        #后台建标需先登录，登录操作
        self.lgpg = login_page.LoginPage(self.diver)
        self.lgpg.open()
        self.lgpg.login()
        #引用后台新建标的page
        self.create_page = createproject_page.CreateNew(self.diver)

    def test_create_new(self):
        self.create_page.open()
        self.create_page.createnewproject()

    def tearDown(self):
        print("end")

if __name__ == '__main__':
    unittest.main()

