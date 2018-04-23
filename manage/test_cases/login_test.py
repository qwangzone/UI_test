import unittest, os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
import login_page
from selenium import webdriver

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.lgpg = login_page.LoginPage(self.dr)

    def test_username_error(self):
        self.lgpg.login(username="errorusername")
        self.error_msg = self.lgpg.get_error_msg()
        self.assertEqual(self.error_msg, "用户名或密码不正确")

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()