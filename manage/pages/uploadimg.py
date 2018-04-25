#coding=utf-8
from basepage import BasePage
from selenium.webdriver.common.keys import Keys
class UploadImg(BasePage):

	#身份证正面上传
	@property
	def CardFrond(self):
		return self.by_id("uploadLocallyCardFrond")

	#身份证反面上传
	@property
	def CardBack(self):
		return self.by_id("uploadLocallyCardBack")

	#借款人头像上传
	@property
	def LocallyHead(self):
		return self.by_id("uploadLocallyHead")

	#上传图片
	@property
	def sendimg(self):
		return self.by_id("uploadImageLocalInputCardFrond")

	#弹框上保存按钮
	@property
	def submit_save_btn(self):
		return self.by_id("saveFileBtnCardFrond")


	def uploadimg(self):
		self.CardFrond.send_keys(Keys.ENTER)
		self.sendimg.send_keys("C:\Users\Administrator\Desktop\图片文件夹\劳动节.png")
		self.submit_save_btn.click()
		driver.switch_to_alert().accept()



