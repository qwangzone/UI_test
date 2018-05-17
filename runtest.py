import unittest
import HTMLTestRunner
#from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os, sys
dir = os.path.dirname(__file__)
print(dir)
sys.path.append(dir + "/manage")
sys.path.append(dir + "/market")
star_dir = "test_cases"
discover = unittest.defaultTestLoader.discover(start_dir=star_dir, pattern="*_test.py", top_level_dir=None)
# dr = webdriver.Remote(command_executor="http://115.159.43.181:5555/wd/hub",
#                       desired_capabilities=DesiredCapabilities.CHROME)
# dr.get("http://58.135.80.52:9380/")
# print(dr.current_url)
# print(dr.title)
# #print(dr.page_source)
# dr.quit()

if __name__ == '__main__':

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + 'apd_test.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="test report", description="apd_test market or manager")
    runner.run(discover)
    fp.close()




