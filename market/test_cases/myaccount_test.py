import unittest
import os, sys
import time
dir = os.path.dirname(os.path.dirname(__file__))
print(dir)
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
from driver import my_driver
from myaccountpage import MyacountPage
from loginpage import LoginPage

class MyaccountTest(unittest.TestCase):
    '''我的账户-账户总览'''

    @classmethod
    def setUpClass(self):
        self.dr = my_driver()
        self.lg = LoginPage(self.dr)
        self.mp = MyacountPage(self.dr)
        self.lg.open()
        self.lg.login(username='13658524695', password='123456',yanzhengma='1')
        time.sleep(3)

    def test1_overview_success(self):
        '''登录至账户总览标签成功'''
        text1 = self.mp.login_success_text()
        self.assertEqual(text1, "账户总览")

    def test2_total_assets(self):
        '''账户总资产>= 0'''
        text = self.mp.total_assets()
        print(text)
        text2 = float(text.replace(',', ''))
        print(text2)
        self.assertGreaterEqual(text2, 0)

    def test3_due_income(self):
        '''待收收入>=0'''
        text = self.mp.due_income()
        print(text)
        text3 = float(text.replace(',', ''))
        print(text3)
        self.assertGreaterEqual(text3, 0)

    def test4_due_prinple(self):
        '''待收本金>=0'''
        text = self.mp.due_prinple()
        print(text)
        text4 = float(text.replace(',', ''))
        print(text4)
        self.assertGreaterEqual(text4, 0)

    def test5_earned_income(self):
        '''已赚收入>=0'''
        text = self.mp.earned_income()
        print(text)
        text5 = float(text.replace(',', ''))
        print(text5)
        self.assertGreaterEqual(text5, 0)

    def test6_amount_in_process(self):
        '''处理中金额'''
        text = self.mp.amount_in_process()
        print(text)
        text6 = float(text.replace(',', ''))
        print(text6)
        self.assertGreaterEqual(text6, 0)

    def test7_avaliable_amount(self):
        '''可用余额'''
        text = self.mp.avaliable_amount()
        print(text)
        text7 = float(text.replace(',', ''))
        print(text7)
        self.assertGreaterEqual(text7, 0)

    @classmethod
    def tearDownClass(self):
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()

