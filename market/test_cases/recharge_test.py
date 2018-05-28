import os, sys
import unittest
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
from myaccountpage import MyacountPage
from rechargepage import RechargePage
from loginpage import LoginPage
from driver import my_driver
from sumapaypage import SumapayPage
import time
from selenium import webdriver

class RechargeTest(unittest.TestCase):

    def setUp(self):
        self.dr = my_driver()
        self.lg = LoginPage(self.dr)
        self.mp = MyacountPage(self.dr)
        self.rp = RechargePage(self.dr)
        self.sp = SumapayPage(self.dr)

    def test1_recharge_success(self):
        """充值成功"""
        self.lg.login(username='13658524695', password='123456', yanzhengma='1')
        amount_before = float(self.mp.avaliable_amount().replace(',', ''))
        print(amount_before)
        self.mp.account_pay()
        sreach_windows = self.dr.current_window_handle #获取当前窗口句柄
        print(sreach_windows)
        self.rp.recharge(money='10')
        all_handles = self.dr.window_handles #获取所有窗口句柄
        #进入输入测试卡号窗口
        for handle in all_handles:
            if handle != sreach_windows:
                self.dr.switch_to.window(handle)
        self.sp.sumapay()
        time.sleep(8)
        #self.dr.switch_to.window(sreach_windows) #返回主窗口
        self.mp.open()
        amount_after = float(self.mp.avaliable_amount().replace(',', ''))
        print(amount_after)
        recharge_amount = int(amount_after - amount_before)
        self.assertEqual(recharge_amount, 10)


if __name__ == '__main__':
    unittest.main()

