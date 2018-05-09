'''借款人提示'''
from basepage import BasePage
from selenium import webdriver


class BorrowTipPage(BasePage):
    url = "/risktip/jkts"

    def content(self):
        return self.by_class_name("panel-body")

    # 获取页面内容
    def get_content(self):
        return self.content().get_attribute("innerHTML")

if __name__ == '__main__':
    dr = webdriver.Chrome()
    dr.maximize_window()
    dr.get("http://192.168.3.105/risktip/jkts")
    a = dr.find_element_by_class_name("panel-body").get_attribute("innerHTML")
    print(a)
