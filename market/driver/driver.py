from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def my_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver = webdriver.Remote(command_executor="http://115.159.43.181:5555/wd/hub",
                              #desired_capabilities=DesiredCapabilities.CHROME)
    return driver


if __name__ == '__main__':
    try:
        dr = my_driver()
       # dr.maximize_window()
        dr.get("http://www.baidu.com/")
        #dr.get("http://www.baidu.com/")
        print(dr.title)
        print(dr.current_url)
    except Exception as msg:
        print(msg)
    finally:
        dr.quit()
