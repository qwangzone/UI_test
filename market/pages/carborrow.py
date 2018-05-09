'''我要借款-我有车'''
from basepage import BasePage
import time


class CarBorrowPage(BasePage):
    url = "/lend/index"

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
    def carType(self):
        return self.by_id("carType")

    @property
    def carPrice(self):
        return self.by_id("carPrice")

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
                    carType="保时捷", carPrice="100000",lendAmount="20000", lendTerm="12",
                    captchaCode="www"):
        self.username.send_keys(username)
        self.mobileNo.send_keys(mobileNo)
        self.provinceCode(provinceCode)
        self.cityCode(cityCode)
        self.carType.send_keys(carType)
        self.carPrice.send_keys(carPrice)
        self.lendAmount.send_keys(lendAmount)
        self.lendTerm.send_keys(lendTerm)
        time.sleep(5)
        self.captchaCode.send_keys(captchaCode)