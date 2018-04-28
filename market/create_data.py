import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir+"/manage/pages")
from createprojectpage import CreateNew
from loginpage import LoginPage
from selenium import webdriver
# from loanuserinfopage import LoanUserInfo
# from uploadimgpage import UploadImg
# from projectstatuspage import ProjectSta

def createdata(driver):
    login_p = LoginPage(driver)
    create_p = CreateNew(driver)

    #登录操作
    login_p.open()
    login_p.login()

    # 创建标的
    create_p.open()
    create_p.createnewproject()

    # 填写借款人信息
    loanuser_p = create_p.loanuserinfo()
    loanuser_p.submitform()

    # 上传图片
    upload_p = create_p.uploadimgb()
    upload_p.uploadimage()

    # 改变项目状态
    prosta_p = create_p.projectstatus()
    prosta_p.changeprosta()

if __name__ == '__main__':
    dr = webdriver.Chrome()
    dr.maximize_window()
    dr.implicitly_wait(20)
    createdata(dr)
