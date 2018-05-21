#coding=utf-8
import sys, os
import time
import unittest
#from selenium import webdriver
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
from loginpage import LoginPage
from zhitouxqpage import ZhitouXqPage
from zhitouzfpage import InvestzfPage
from driver import my_driver


class InvestTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.dr = my_driver()
        self.lg = LoginPage(self.dr)
        self.lg.login(username='13658524695', password='123456', yanzhengma='1')
        time.sleep(5)
        self.iv = ZhitouXqPage(self.dr)
        self.zhifu = InvestzfPage(self.dr)

    def test1_invest_success(self):
        """投资成功"""
        self.iv.open()
        remain1 = self.iv.remain_text()
        #print(remain1)
        remain1_text = float(remain1.replace(',', ''))
        #print(remain1_text)
        self.iv.invest(money='100')
        self.zhifu.zhifu_btn()
        time.sleep(5)
        self.zhifu.huishang(password='123456')
        time.sleep(5)
        self.iv.open()
        remain2 = self.iv.remain_text()
        #print(remain2)
        remain2_text = float(remain2.replace(',', ''))
        #print(remain2_text)
        remain_text = int(remain1_text-remain2_text)
        self.assertEqual(100, remain_text)

    def test2_less100(self):
        """投资金额小于100"""
        self.iv.invest_error(money='10')
        error_text = self.iv.input_error_text()
        self.assertEqual(error_text, u'最小出借金额为100元！')

    def test3_typerror(self):
        """输入格式不正确"""
        self.iv.invest_error(money='##3')
        error_text = self.iv.input_error_text()
        self.assertEqual(error_text, u'输入的金额格式不正确')

    def test4_lessremain(self):
        """投资金额大于账户余额"""
        self.iv.invest_error(money='1000000')
        error_text = self.iv.input_error_text()
        self.assertEqual(error_text, u'余额不足请进行充值')

    def test5_maxbid(self):
        """投资金额大于剩余可投"""
        self.iv.open()
        balance = self.iv.remain_invest_text()
        #print(balance)
        balance_f = float(balance.replace(',', ''))
        #print(balance_f)
        input_amount = balance_f + 1
        input_amount_f = int(input_amount)
        self.iv.invest_error(input_amount_f)
        error_text = self.iv.input_error_text()
        self.assertIn(u'最大可投余额为', error_text)

    @classmethod
    def tearDownClass(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()





