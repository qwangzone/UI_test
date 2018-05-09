'''产品介绍'''
from basepage import BasePage


class ProductPage(BasePage):
    url = "/information/productInstro"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")
