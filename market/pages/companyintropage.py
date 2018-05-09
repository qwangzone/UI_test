'''公司简介'''
from basepage import BasePage


class CompanyInfoPage(BasePage):
    url = "/information/informationPublic"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")
