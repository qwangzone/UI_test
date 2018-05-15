"""我有信用我要借款"""
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

    @property
    def cityCode(self, text="北京市"):
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

    # 提交表单信息
    def form_submit(self, username="李逵", mobileNo="110", provinceCode="北京市", cityCode="北京市",
                    lendAmount="20000", lendTerm="12",captchaCode="www"):
        self.username.send_keys(username)
        self.mobileNo.send_keys(mobileNo)
        self.provinceCode(provinceCode)
        self.cityCode(cityCode)
        self.lendAmount.send_keys(lendAmount)
        self.lendTerm.send_keys(lendTerm)
        time.sleep(5)
        self.captchaCode.send_keys(captchaCode)