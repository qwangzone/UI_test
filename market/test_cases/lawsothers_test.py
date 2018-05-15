'''相关法律法规'''
from basepage import BasePage
class LawerOtherPage(BasePage):
    url = "/risktip/xgfl"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")
