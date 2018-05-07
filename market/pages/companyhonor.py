'''公司荣誉'''
from basepage import BasePage
class CompanyHrPage(BasePage):
    url = "/data/transcript"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")

