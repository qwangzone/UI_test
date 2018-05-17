'''收费标准'''
from basepage import BasePage
class ChargingPage(BasePage):

    url = "/information/rates"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")