'''运营报告'''
from basepage import BasePage
class OperRportPage(BasePage):
    url = "/information/operationReport"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")