'''我有信用-我要借款'''
from basepage import BasePage
import time

class CreditBorrowPage(BasePage):
    url = "/lend/lend"

    @property
    def username(self):
        return self.by_id("lendName")

    @property
    def mobileNo(self):
        return self.by_id("mobileNo")

    def provinceCode(self, text="北京市"):
        ele = self.by_id("provinceCode")
        return self.select_by_text(ele, text)

    def city_Code(self, text="北京市"):
        ele = self.by_id("cityCode")
        return self.select_by_text(ele, text)

    @property
    def lendAmount(self):
        return self.by_id("lendAmount")

    @property
    def lendTerm(self):
        return self.by_id("lendTerm")

    @property
    def captchaCode(self):
        return self.by_id("captchaCode")

    @property
    def btn(self):
        return self.by_tag_name("button")

    # 提交表单信息
    def form_submit(self, username=u"李逵", mobileNo="15811507615", provinceCode="北京市", cityCode="北京市",
                    lendAmount="20000", lendTerm="12",captchaCode="1111"):
        self.username.send_keys(username)
        self.mobileNo.send_keys(mobileNo)
        self.provinceCode(provinceCode)
        self.city_Code(cityCode)
        self.lendAmount.send_keys(lendAmount)
        self.lendTerm.send_keys(lendTerm)
        self.captchaCode.send_keys(captchaCode)
        self.btn.click()


    #信用借款错误信息提示
    def credit_errormsg_list(self):
        """下标0-6对应如下0-姓名，1-手机号码，2-借款金额，3-借款期限，4-验证码"""
        #return self.by_csses("div.register_tis>span")
        return self.by_xpaths("//div[@class = 'register_tis dis_ib']/span")

    #提交后服务器返回信息
    def credit_msg(self):
        return self.ele_wait_present(("css selector", "li.mb1>span")).text



