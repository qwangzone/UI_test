#coding=utf-8
import os, sys
import time
from selenium import webdriver
import unittest
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
from homepage import HomePage

class HomePageTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
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

    #页面顶部QQ群不为空
    def test2_weqq(self):
        self.hp.open()
        text2 = self.hp.weqq()
        self.assertIsNotNone(text2, '页面顶部qq群此处为空') #msg此处为fail时打印的信息

    #页面顶部微信公众号不为空
    def test3_wechat(self):
        self.hp.open()
        text3 = self.hp.wechat()
        self.assertIsNotNone(text3, '页面顶部微信公众号不为空')

    #我要借款
    def test4_borrow_right_head(self):
        self.hp.borrow_right_head()
        time.sleep(3)
        text4 = self.dr.current_url
        self.assertEqual(text4, 'http://192.168.3.105/lend/index')
        self.dr.back()

    #页面顶部帮助中心
    def test5_helpcenter(self):
        self.hp.helpcenter()
        time.sleep(3)
        text5 = self.dr.current_url
        self.assertEqual(text5, 'http://192.168.3.105/help/js')
        #self.dr.back()

    #导航栏-我要出借
    def test6_lend_link(self):
        self.hp.open()
        self.hp.lend_link()
        text6 = self.dr.current_url
        self.assertEqual(text6, 'http://192.168.3.105/licai/')

    #导航栏-信息披露
    def test7_information_link(self):
        self.hp.information_link()
        text7 = self.dr.current_url
        self.assertEqual(text7, 'http://192.168.3.105/information/safeController')

    #导航栏-风险教育
    def test8_riskedc_link(self):
        self.hp.riskedc_link()
        text8 = self.dr.current_url
        self.assertEqual(text8, 'http://192.168.3.105/risktip/fxjy')

    #导航栏-关于我们
    def test9_aboutUs_link(self):
        self.hp.aboutUs_link()
        text9 = self.dr.current_url
        self.assertEqual(text9, 'http://192.168.3.105/information/informationPublic')

    #邀请好友
    def test10_invitefriends(self):
        self.hp.invitefriends()
        text10 = self.dr.current_url
        self.assertEqual(text10, 'http://192.168.3.105/special/invitefriends')
        self.dr.back()

    #转让专区
    def test11_transfer(self):
        self.hp.transfer()
        text11 = self.dr.current_url
        self.assertEqual(text11, 'http://192.168.3.105/creditAssignList/list-0-0-0-1')
        self.dr.back()

    #活动专区
    def test12_activities(self):
        self.hp.activities()
        text12 = self.dr.current_url
        self.assertEqual(text12, 'http://192.168.3.105/help/activity?status=1')
        self.dr.back()

    #兑换专区
    def test13_exchange(self):
        self.hp.exchange()
        text13 = self.dr.current_url
        self.assertEqual(text13, 'http://192.168.3.105/pointsshop/goodsList')
        self.dr.back()

    #新手专区
    def test14_Newbie(self):
        self.hp.Newbie()
        text14 = self.dr.current_url
        self.assertEqual(text14, 'http://192.168.3.105/special/newGuide')

    #累计交易额不为0
    def test15_accumulated_amount(self):
        self.hp.open()
        time.sleep(3)
        text15 = self.hp.accumulated_amount()
        self.assertGreaterEqual(text15, 1892907)

    #累计注册人数大于等于当前
    def test16_accumulated_number(self):
        text16 = self.hp.accumulated_number()
        self.assertGreaterEqual(text16, 9072)

    @classmethod
    def tearDownClass(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()