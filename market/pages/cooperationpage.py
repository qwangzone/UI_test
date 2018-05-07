'''合作机构'''
from basepage import BasePage
class CooperationPage(BasePage):
    url = "/information/trustMec"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")
