import unittest
import HTMLTestRunner
import time
import os, sys
#dir = os.path.dirname(__file__)
dir = os.path.dirname(os.path.abspath(__file__))
print(dir)
# sys.path.append(dir + "/manage")
# sys.path.append(dir + "/market")
star_dir = dir + "/market/test_cases"
discover = unittest.defaultTestLoader.discover(start_dir=star_dir, pattern="*_test.py", top_level_dir=None)
now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = dir + "/report/" + now + 'apd_test.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="test report", description="apd_test market or manager")
runner.run(discover)
fp.close()







