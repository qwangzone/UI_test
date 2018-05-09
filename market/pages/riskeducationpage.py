'''风险教育'''
from basepage import BasePage


class RiskEducationPage(BasePage):
    url = "/risktip/fxjy"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")
