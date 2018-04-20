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
