'''平台公告'''
from basepage import BasePage
class PlateNoticePage(BasePage):
    url = "/notice/notice"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")