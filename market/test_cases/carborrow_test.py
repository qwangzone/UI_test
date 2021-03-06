#coding=utf-8
import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from carborrow import CarBorrowPage


class CarborrowTest(unittest.TestCase):
    """我要借款-车贷"""
    def setUp(self):
        self.dr = my_driver()
        self.carborrow_p = CarBorrowPage(self.dr)
        self.carborrow_p.open()

    def test1_success(self):
        """提交借款信息成功"""
        self.carborrow_p.form_submit()
        success_text = self.carborrow_p.get_msg()
        print(success_text)
        self.assertIn("借款请求提交成功", success_text)

    def test2_codeerror(self):
        """验证码位数错误，前端判断"""
        self.carborrow_p.form_submit(captchaCode="222")
        error_text = self.carborrow_p.error_msg_list()[6].text
        print(error_text)
        self.assertIn("请填写有效的验证码", error_text)

    def test3_codeinput_error(self):
        """验证码输入错误，后台判断"""
        self.carborrow_p.form_submit(captchaCode="2222")
        error_text = self.carborrow_p.get_msg()
        print(error_text)
        self.assertIn("验证码不正确", error_text)

    def test4_all_null(self):
        """所有输入为空"""
        self.carborrow_p.button.click()
        name_error = self.carborrow_p.error_msg_list()[0].text
        phone_error = self.carborrow_p.error_msg_list()[1].text
        cartype_error = self.carborrow_p.error_msg_list()[2].text
        carprice_error = self.carborrow_p.error_msg_list()[3].text
        lendamount_error = self.carborrow_p.error_msg_list()[4].text
        lendterm_error = self.carborrow_p.error_msg_list()[5].text
        code_error = self.carborrow_p.error_msg_list()[6].text
        self.assertIn("请输入真实姓名", name_error)
        self.assertIn("请填写手机号码", phone_error)
        self.assertIn("请输入车辆型号", cartype_error)
        self.assertIn("请输入购车价格", carprice_error)
        self.assertIn("请输入借款金额", lendamount_error)
        self.assertIn("请输入借款期限", lendterm_error)
        self.assertIn("请输入验证码", code_error)

    def test5_name_error(self):
        """姓名输入不合法"""
        self.carborrow_p.form_submit(username="www")
        name_error = self.carborrow_p.error_msg_list()[0].text
        self.assertIn("请填写正确信息", name_error)

    def test6_phone_error(self):
        """手机号输入不合法"""
        self.carborrow_p.form_submit(mobileNo="125")
        phone_error = self.carborrow_p.error_msg_list()[1].text
        self.assertIn("请填写有效的手机号码", phone_error)

    def test7_cartype_error(self):
        """汽车型号输入不合法"""
        self.carborrow_p.form_submit(carType="@#q")
        cartype_error = self.carborrow_p.error_msg_list()[2].text
        self.assertIn("请填写正确信息", cartype_error)

    def test8_carprice_error(self):
        """汽车价格输入不合法"""
        self.carborrow_p.form_submit(carPrice="aer")
        carprice_error = self.carborrow_p.error_msg_list()[3].text
        self.assertIn("请填写正确信息", carprice_error)

    def test9_lendamount_error(self):
        """借款金额输入不合法"""
        self.carborrow_p.form_submit(lendAmount="aer")
        lendamount_error = self.carborrow_p.error_msg_list()[4].text
        self.assertIn("请填写正确信息", lendamount_error)

    def test10_lendterm_error(self):
        """借款期限输入不合法"""
        self.carborrow_p.form_submit(lendTerm="aer")
        lendterm_error = self.carborrow_p.error_msg_list()[5].text
        self.assertIn("请填写正确信息", lendterm_error)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    # suit = unittest.TestSuite()
    # suit.addTest(CarborrowTest('test4_all_null'))
    # runner = unittest.TextTestRunner()
    # runner.run(suit)
    unittest.main()