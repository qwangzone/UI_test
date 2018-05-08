'''禁止性行为'''
from basepage import BasePage


class ProhibitedbvPage(BasePage):
    url = "/risktip/jzxw"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")
