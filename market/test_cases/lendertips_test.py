'''出借人提示'''
from basepage import BasePage
class LenderTipsPage(BasePage):
    url = "/risktip/tzts"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")