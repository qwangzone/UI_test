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

    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def by_class_name(self, classname):
        return self.driver.find_element_by_class_name(classname)

    def by_tag_name(self, tagname):
        return self.driver.find_element_by_tag_name(tagname)

