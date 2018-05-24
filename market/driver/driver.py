from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time, sys

def my_driver():
    if sys.platform.startswith("win"):
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif sys.platform.startswith("linux"):
        capabilities = DesiredCapabilities.CHROME.copy()
        # 设置测试名称
        # capabilities['name'] = "mytest_baidu"
        # 设置本次构建名称
        # capabilities['build'] = "myTestBuild_baidu"
        driver = webdriver.Remote(command_executor="http://115.159.43.181:5555/wd/hub",
                                  desired_capabilities=capabilities)

    #capabilities = DesiredCapabilities.CHROME.copy()
    # 设置测试名称
    # capabilities['name'] = "mytest_baidu"
    # 设置本次构建名称
    # capabilities['build'] = "myTestBuild_baidu"
    #driver = webdriver.Remote(command_executor="http://115.159.43.181:5555/wd/hub",
                              #desired_capabilities=capabilities)

    return driver


if __name__ == '__main__':
    try:
        dr = my_driver()
       # dr.maximize_window()
        #dr.get("http://115.159.43.181:5555/grid/console")
        dr.get("http://www.baidu.com/")
        #dr.find_element_by_link_text("view config").click()
        print(dr.title)
        print(dr.current_url)
        time.sleep(5)
    except Exception as msg:
        print(msg)
    finally:
        dr.quit()
