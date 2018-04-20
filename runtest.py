import unittest
import HTMLTestRunner
star_dir = "pathxx"
fp = open("pathxx", 'wr')
discover = unittest.defaultTestLoader.discover(start_dir=star_dir, pattern="*_test.py")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="xxxx", description="xxxxxx")