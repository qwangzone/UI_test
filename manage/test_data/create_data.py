#coding=utf-8
import os, sys

dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages/")
from createprojectpage import CreateNew
from loginpage import LoginPage
from selenium import webdriver
from datetime import datetime
import random


# from loanuserinfopage import LoanUserInfo
# from uploadimgpage import UploadImg
# from projectstatuspage import ProjectSta
def num():
    for i in range(1, 1000):
        yield i
def projectname():
    now = datetime.now().strftime("%m%d")
    f = num()
    return now + str(next(f))




def createdata(driver):
    login_p = LoginPage(driver)
    create_p = CreateNew(driver)

    # 登录操作
    login_p.open()
    login_p.login()

    # 创建标的
    create_p.open()
    create_p.createnewproject(project_name="testwq")

    # 填写借款人信息
    loanuser_p = create_p.loanuserinfo()
    loanuser_p.submitform()

    # 上传图片
    upload_p = create_p.uploadimgb()
    upload_p.uploadimage()

    # 改变项目状态
    prosta_p = create_p.projectstatus()
    prosta_p.changeprosta_yianpai()
    prosta_p.changeprosta_kaifang()

    # 获取标id
    url = driver.current_url
    project_id = url.split("/")[-1]
    return project_id


if __name__ == '__main__':
    dr = webdriver.Chrome()
    dr.maximize_window()
    #dr.implicitly_wait(20)
    createdata(dr)
