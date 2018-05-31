#coding=utf-8
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
class BasePage:
    base_url = "http://192.168.3.105:88"

    def __init__(self, webdriver, domain=base_url):
        self.driver = webdriver
        self.domain = domain

    def _open(self, url):
        url = self.domain + url
        self.driver.get(url)

    def open(self):
        self._open(self.url)

    def by_id(self, id):
        return self.driver.find_element_by_id(id)

    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    def by_css(self, css_loc):
        return self.driver.find_element_by_css_selector(css_loc)

    def by_csses(self, css_loc):
        return self.driver.find_elements_by_css_selector(css_loc)

    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def by_class_name(self, classname):
        return self.driver.find_element_by_class_name(classname)

    def by_tag_name(self, tagname):
        return self.driver.find_element_by_tag_name(tagname)

    def select_by_text(self, element, text):
        return Select(element).select_by_visible_text(text)

    def js_execute(self, js):
        return self.driver.execute_script(js)

    def by_link(self, link_text):
        return self.driver.find_element_by_link_text(link_text)

    def switch_alert(self):
        return self.driver.switch_to.alert

    # 竖向滚动条拉动
    def scroll(self, size):
        js = "document.body.scrollTop=\'%s\'" % size
        self.js_execute(js)

    # 封装显式等待元素是否出现
    def ele_wait_present(self, locate):
        # if by == 'id':
        #     locate = self.by_id(value)
        # elif by == 'name':
        #     locate = self.by_name(value)
        # elif by == 'classname':
        #     locate = self.by_class_name(value)
        # elif by == 'xpath':
        #     locate = self.by_xpath(value)
        # elif by == 'css':
        #     locate = self.by_css(value)

        return WebDriverWait(self.driver, 20, 1).until(EC.presence_of_element_located(locate))

    # 封装显示等待元素是否可见

    def ele_wait_visible(self, locate):
        return WebDriverWait(self.driver, 20, 1).until(EC.visibility_of_element_located(locate))

    # 封装显式等待元素是否而可点击
    def ele_wait_clickable(self, locate):
        return WebDriverWait(self.driver, 20, 1).until(EC.element_to_be_clickable(locate))

    #     # 封装键盘操作
    #
    # def keyboard(self, WebElement, keyboard="ENTER"):
    #     return WebElement.send_keys(Keys.keyboard)

    # 封装鼠标悬停操作
    def mouse_stop(self, locate):
        return ActionChains(self.driver).move_to_element(locate).perform()
