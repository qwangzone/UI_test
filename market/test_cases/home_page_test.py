#coding=utf-8
import os, sys
import time
#from selenium import webdriver
import unittest
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
from homepage import HomePage
from driver import my_driver

class HomePageTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.dr = my_driver()
        self.hp = HomePage(self.dr)
        self.hp.open()
        self.hp.layerclose()

    #新浪微博
    # def test1_websina(self):
    #     self.hp.websina()
    #     time.sleep(3)
    #     text1 = self.dr.current_url
    #     self.assertIn('https://weibo.com/apengdai', text1)
    #     self.dr.close()

    def test2_weqq(self):
        """页面顶部QQ群不为空"""
        self.hp.open()
        text2 = self.hp.weqq()
        self.assertIsNotNone(text2, '页面顶部qq群此处为空') #msg此处为fail时打印的信息

    def test3_wechat(self):
        """页面顶部微信公众号不为空"""
        self.hp.open()
        text3 = self.hp.wechat()
        self.assertIsNotNone(text3, '页面顶部微信公众号不为空')

    def test4_borrow_right_head(self):
        """我要借款"""
        self.hp.borrow_right_head()
        time.sleep(3)
        text4 = self.dr.current_url
        self.dr.back()
        text = "/" + text4.split('/', 3)[3]  #获取url后缀路径
        print(text)
        self.assertEqual(text, '/lend/index')

    def test5_helpcenter(self):
        """页面顶部帮助中心"""
        self.hp.helpcenter()
        time.sleep(3)
        text5 = self.dr.current_url
        text = "/" + text5.split('/', 3)[3]
        self.assertEqual(text, '/help/js')  #获取帮助中心路径
        #self.dr.back()

    def test6_lend_link(self):
        """导航栏-我要出借"""
        self.hp.open()
        self.hp.lend_link()
        text6 = self.dr.current_url
        text = "/" + text6.split('/', 3)[3] #获取我要出借路径
        self.assertEqual(text, '/licai/')

    def test7_information_link(self):
        """导航栏-信息披露"""
        self.hp.information_link()
        text7 = self.dr.current_url
        text = "/" + text7.split('/', 3)[3]  #获取信息披露路径
        self.assertEqual(text, '/information/safeController')

    def test8_riskedc_link(self):
        """导航栏-风险教育"""
        self.hp.riskedc_link()
        text8 = self.dr.current_url
        text = "/" + text8.split('/', 3)[3]  #获取风险教育路径
        self.assertEqual(text, '/risktip/fxjy')

    def test9_aboutUs_link(self):
        """导航栏-关于我们"""
        self.hp.aboutUs_link()
        text9 = self.dr.current_url
        text = "/" + text9.split('/', 3)[3]  #获取关于我们路径
        self.assertEqual(text, '/information/informationPublic')

    def test10_invitefriends(self):
        """邀请好友"""
        self.hp.open()
        self.hp.invitefriends()
        text10 = self.dr.current_url
        self.dr.back()
        text = "/" + text10.split('/', 3)[3]  #获取邀请好友路径
        self.assertEqual(text, '/special/invitefriends')

    def test11_transfer(self):
        """转让专区"""
        self.hp.transfer()
        text11 = self.dr.current_url
        print("text11=" + text11)
        self.dr.back()
        print("转让=" + self.dr.current_url)
        text = "/" + text11.split('/', 3)[3]  #获取转让专区路径
        self.assertEqual(text, '/creditAssignList/list-0-0-0-1')

    def test12_activities(self):
        """活动专区"""
        self.hp.activities()
        text12 = self.dr.current_url
        text = "/" + text12.split('/', 3)[3]  #获取活动专区路径
        self.assertEqual(text, '/help/activity?status=1')

    def test13_exchange(self):
        """兑换专区"""
        self.hp.open()
        self.hp.exchange()
        text13 = self.dr.current_url
        self.dr.back()
        text = "/" + text13.split('/', 3)[3]  #获取兑换专区路径
        self.assertEqual(text, '/pointsshop/goodsList')

    def test14_Newbie(self):
        """新手专区"""
        self.hp.Newbie()
        text14 = self.dr.current_url
        text = "/" + text14.split('/', 3)[3]  #获取新手专区路径
        self.assertEqual(text, '/special/newGuide')

    def test15_accumulated_amount(self):
        """累计交易额不为0"""
        self.hp.open()
        time.sleep(3)
        text15 = self.hp.accumulated_amount()
        self.assertGreaterEqual(text15, 1892907)

    def test16_accumulated_number(self):
        """累计注册人数大于等于当前"""
        text16 = self.hp.accumulated_number()
        self.assertGreaterEqual(text16, 9072)

    @classmethod
    def tearDownClass(self):
        self.dr.quit()

if __name__ == '__main__':
    suit = unittest.TestSuite()
    #suit.addTest(HomePageTest('test11_transfer'))
    suit.addTest(HomePageTest('test12_activities'))
    suit.addTest(HomePageTest('test13_exchange'))
    suit.addTest(HomePageTest('test14_Newbie'))
    runner = unittest.TextTestRunner()
    runner.run(suit)