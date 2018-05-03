#coding=utf-8
import unittest
from selenium import webdriver
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
print(dir)
sys.path.append(dir + "/test_data/")
sys.path.append(dir + "/pages")
from projectinfopage import ProjetInfo
import create_data
class ProjectInfoTest(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        project_id = create_data.createdata(self.dr)
        self.proinfo_p = ProjetInfo(self.dr)
        self.dr.get(self.proinfo_p.url + project_id)

    def testa(self):
        print("test")

    def tearDown(self):
        print("end")
if __name__ == '__main__':
    unittest.main()

