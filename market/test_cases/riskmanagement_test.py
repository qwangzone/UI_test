'''风险管理'''
from basepage import BasePage


class RiskManegePage(BasePage):
    url = "/information/riskManagement"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")