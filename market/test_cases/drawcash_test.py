import os, sys
import unittest
import time
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
from driver import my_driver
from loginpage import LoginPage
from myaccountpage import MyacountPage
from drawcashpage import DrawcashPage

class DrawcashTest(unittest.TestCase):

    def setUp(self):
        self.dr = my_driver()
        self.lg = LoginPage(self.dr)
        self.lg.login(username='13658524695', password='123456', yanzhengma='1')
        self.mp = MyacountPage(self.dr)
        self.mp.draw_btn()
        self.dp = DrawcashPage(self.dr)

    def test1_drawcash_success(self):
        """提现成功"""
        self.dp.drawcash(drawamount='10')
        self.dp.huishang_queren()
        time.sleep(3)
        text = self.dp.drawsuccess_text()
        print(text)
        self.assertEqual(text, '交易成功！')

    def test2_drawcash_less10(self):
        """提现低于最少提现金额10元"""
        self.dp.drawcash(drawamount='3')
        text_error = self.dp.drawfail_text()
        print(text_error)
        self.assertEqual(text_error, '提现申请失败！单笔提现金额最低10.0元!')

if __name__ == '__main__':
    #unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(DrawcashTest('test2_drawcash_less10'))
    runner = unittest.TextTestRunner()
    runner.run(suit)



