import unittest
import HTMLTestRunner
import time
import os, sys
#dir = os.path.dirname(__file__)
dir = os.path.dirname(os.path.abspath(__file__))
print(dir)
from multiprocessing import Process
# sys.path.append(dir + "/manage")
# sys.path.append(dir + "/market")

def run_market():
    star_dir = dir + "/market/test_cases"
    discover = unittest.defaultTestLoader.discover(start_dir=star_dir, pattern="carborrow_test.py", top_level_dir=None)
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = dir + "/report/" + 'apdtest_market_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="阿朋贷测试报告", description="阿朋贷前台",
                                           verbosity=2)
    runner.run(discover)
    fp.close()

def run_manage():
    star_dir = dir + "/manage/test_cases"
    discover = unittest.defaultTestLoader.discover(start_dir=star_dir, pattern="createproject_test.py", top_level_dir=None)
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = dir + "/report/" + 'apdtest_manage_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="阿朋贷测试报告", description="阿朋贷后台",
                                           verbosity=2)
    runner.run(discover)
    fp.close()

if __name__ == '__main__':
    p1 = Process(target=run_market)
    p2 = Process(target=run_manage)
    p1.start()
    p2.start()
    p1.join()
    p2.join()




