#coding=utf-8
import os, sys
import unittest
import time
#from selenium import webdriver
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
from driver import my_driver
from creditborrow import CreditBorrowPage

class CreditborrowTest(unittest.TestCase):

    def setUp(self):
        self.dr = my_driver()
        self.creditborrow_p = CreditBorrowPage(self.dr)
        self.creditborrow_p.open()

    def test1_creditbrorrow_success(self):
        '''信用借款信息请求提交成功'''
        self.creditborrow_p.form_submit()
        text1 = self.creditborrow_p.credit_msg()
        self.assertIn(u'借款请求提交成功', text1)

    def test2_codeinput_error(self):
        '''验证码输入错误，后台验证'''
        self.creditborrow_p.form_submit(captchaCode="1234")
        text4 = self.creditborrow_p.credit_msg()
        self.assertIn(u'验证码不正确', text4)

    def test3_allinput_error(self):
        '''所有输入均为空'''
        self.creditborrow_p.btn.click()
        time.sleep(3)
        name_error = self.creditborrow_p.credit_errormsg_list()[0].text
        print(name_error)
        mobile_error = self.creditborrow_p.credit_errormsg_list()[1].text
        amount_error = self.creditborrow_p.credit_errormsg_list()[2].text
        term_error = self.creditborrow_p.credit_errormsg_list()[3].text
        code_error = self.creditborrow_p.credit_errormsg_list()[4].text
        self.assertIn(u'请输入真实姓名', name_error)
        self.assertIn(u'请填写手机号码', mobile_error)
        self.assertIn(u'请输入借款金额', amount_error)
        self.assertIn(u'请输入借款期限', term_error)
        self.assertIn(u'请输入验证码', code_error)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()





