'''平台数据'''
from basepage import BasePage
class PlateDatePage(BasePage):
    url = "/data"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")