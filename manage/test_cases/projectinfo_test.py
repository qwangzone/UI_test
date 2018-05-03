#coding=utf-8
import unittest
from selenium import webdriver
import os, sys
from datetime import datetime, timedelta
dir = os.path.dirname(os.path.dirname(__file__))
print(dir)
sys.path.append(dir + "/test_data/")
sys.path.append(dir + "/pages")
from projectinfopage import ProjetInfo
import create_data
class ProjectInfoTest(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        #project_id = create_data.createdata(self.dr)
        self.proinfo_p = ProjetInfo(self.dr)
        #self.dr.get(self.proinfo_p.url + project_id)
        self.dr.get("http://192.168.3.105/licai/60232")

    #前台项目信息填写成功
    def test1_projectinfo_success(self):
        pt = self.proinfo_p.project_type().text  #项目类型
        pd = self.proinfo_p.project_deadline().text  #借款期限
        pa = self.proinfo_p.project_amount().text  #借款金额
        pu = self.proinfo_p.project_use().text  #借款用途
        pA = self.proinfo_p.project_Addr().text  #签约地址
        ps = self.proinfo_p.project_sartt().text  #募集开始时间
        now = self.proinfo_p.start_time()
        self.assertEqual(pt, '信易融' )
        self.assertEqual(pd, '12个月')
        self.assertEqual(pa, '5000')
        self.assertEqual(pu, '资金用途测试')
        self.assertEqual(pA, '签约地址测试')
        self.assertIn(ps, now)

    def tearDown(self):
        print("end")
if __name__ == '__main__':
    unittest.main()

