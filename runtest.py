import unittest
import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
star_dir = "test_cases"
fp = open("pathxx", 'wr')
discover = unittest.defaultTestLoader.discover(start_dir=star_dir, pattern="*_test.py")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="xxxx", description="xxxxxx")
dr = webdriver.Remote(command_executor="http://115.159.43.181:5555/wd/hub",
                      desired_capabilities=DesiredCapabilities.CHROME)
dr.get("http://58.135.80.52:9380/")
print(dr.current_url)
print(dr.title)
#print(dr.page_source)
dr.quit()