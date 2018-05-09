# coding=utf-8
import unittest
from selenium import webdriver
import os, sys
from datetime import datetime, timedelta
import time

dir = os.path.dirname(os.path.dirname(__file__))
print(dir)
sys.path.append(dir + "/test_data/")
sys.path.append(dir + "/pages")
from projectinfopage import ProjetInfo
from createprojectpage import CreateNew
import create_data


class ProjectInfoTest(unittest.TestCase):
    """测试前台项目详情"""
    @classmethod
    def setUpClass(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        project_id = create_data.createdata(self.dr)
        self.proinfo_p = ProjetInfo(self.dr)
        self.dr.get(self.proinfo_p.url + project_id)
        #self.dr.get("http://192.168.3.105/licai/60232")
        time.sleep(10)
        self.create_p = CreateNew(self.dr)

    # 前台项目信息填写成功
    def test1_projecttype_success(self):
        pt = self.proinfo_p.project_type().text
        self.assertEqual(pt, u'信易融')

    def test2_prodeadline_success(self):
        pd = self.proinfo_p.project_deadline().text
        self.assertEqual(pd, u'12个月')

    def test3_proamount_success(self):
        pa = self.proinfo_p.project_amount().text
        self.assertEqual(pa, '5000.00')

    def test4_prouse_success(self):
        pu = self.proinfo_p.project_use().text
        self.assertEqual(pu, u'资金用途测试')

    def test5_proAddr_success(self):
        pA = self.proinfo_p.project_Addr().text
        self.assertEqual(pA, u'签约地址测试')

    def test6_prosartt_success(self):
        ps = self.proinfo_p.project_sartt().text
        self.st = self.create_p.start_time()
        self.assertIn(ps, self.st)

    def test7_valuedate_success(self):
        vd = self.proinfo_p.value_date().text
        vt = self.st + timedelta(days=1)
        self.assertIn(vd, vt)

    def test8_bidamount_success(self):
        ba = int(self.proinfo_p.bid_amount().text)
        self.assertIn(100, ba)

    def test9_repaytype_success(self):
        rt = self.proinfo_p.repayment_type().text
        self.assertIn(u'等额本息', rt)

    def test10_repayorigin_success(self):
        ro = self.proinfo_p.repayment_origin().text
        self.assertEqual(ro, u'还款来源测试')

    def test11_repayassurance_success(self):
        ra = self.proinfo_p.repayment_assurance().text
        self.assertEqual(ra, u'还款保障措施测试')

    def test12_riskrating_success(self):
        rr = self.proinfo_p.risk_rating().text
        self.assertIn('AAA', rr)

    def test13_edubackground(self):
        eb = self.proinfo_p.education_background().text
        self.assertEqual(eb, u'本科')

    def test14_marriagestatus_success(self):
        ms = self.proinfo_p.marriage_status().text
        self.assertEqual(ms, u'未婚')

    def test15_industryinfo_success(self):
        ii = self.proinfo_p.industry_info().text
        self.assertEqual(ii, u'创造业')

    def test16_enterproperty_success(self):
        ep = self.proinfo_p.enterprise_property().text
        self.assertEqual(ep, u'国有企业')

    def test17_positioninfo_success(self):
        pi = self.proinfo_p.position_info().text
        self.assertEqual(pi, u'股东')

    def test18_incomemonthly_success(self):
        im = self.proinfo_p.income_monthly().text
        self.assertEqual(im, u'30000元以上')

    def test19_houseRadios_success(self):
        hR = self.proinfo_p.house_Radios().text
        self.assertEqual(hR, u'有')

    def test20_houseloan_success(self):
        hl = self.proinfo_p.house_loan().text
        self.assertEqual(hl, u'有')

    def test21_carRadios_success(self):
        cR = self.proinfo_p.car_Radios().text
        self.assertEqual(cR, u'有')

    def test22_carloan_success(self):
        cl = self.proinfo_p.car_loan().text
        self.assertEqual(cl, u'有')

    def test23_livingcity_success(self):
        lc = self.proinfo_p.living_city().text
        self.assertEqual(lc, u'签约地址测试')

    @classmethod
    def tearDownClass(self):
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
