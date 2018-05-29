import os, sys
import unittest
import time
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(dir)
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
sys.path.append(dir + "/db")
from registerpage import RegisterPage
from driver import my_driver
from registersuccesspage import RegisterSuccessPage
from mysql_db import DB

class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.dr = my_driver()
        self.rp = RegisterPage(self.dr)
        self.rs = RegisterSuccessPage(self.dr)

    def test1_mobile_exist(self):
        """手机号码存在"""
        self.rp.register_error()
        text_error = self.rp.mobile_error()
        print(text_error)
        self.assertIn('该手机号存在', text_error)

    def test2_captchaCode_error(self):
        """图形验证码输入有误"""
        self.rp.register_error(mobile='12345678914', code='0')
        text_error = self.rp.captchaCode_error()
        self.assertEqual(text_error, '*图形验证码不正确，请重新输入')

    def test3_sms_error(self):
        """短信验证码输入错误"""
        self.rp.register(yanzheng='000')
        text_error = self.rp.sms_error()
        self.assertEqual(text_error, '*短信验证码错误')

    def test4_register_success(self):
        """注册成功"""
        self.rp.register()
        time.sleep(3)
        text = self.rs.register_success().text
        self.assertIn('用户，恭喜您注册成功！', text)
        # db = DB()
        # db.delete_user()
        # db.close()

    def tearDown(self):
        self.dr.quit()


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(RegisterTest("test4_register_success"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main()
    db = DB()
    db.delete_user()
    db.close()