import unittest
from BSTestRunner import BSTestRunner
import time
import logging
import sys, os

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

# 执行之前需要在run.py脚本添加如下内容：
# import sys
# path='D:\\kyb_testProject\\'
# sys.path.append(path)

# 指定测试用例路径
test_dir = '../test_case'
# 测试报告路径
report_dir = '../reports'
# 定义报告的文件名格式
now = time.strftime("%Y-%m-%d %H_%M_%S")

# 加载test_login测试用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py')
report_name = report_dir + '/' + now + ' test_report.html'

# 核心：运行用例并生成测试报告
with open(report_name, 'wb') as f:
    # 定义标题与描述
    runner = BSTestRunner(stream=f, title="Kyb Test Report", description="kyb Andriod app Test Report")
    logging.info("start run testcase...")
    runner.run(discover)

# 注意：
# pattern参数可以控制运行不同模块的用例，如下所示表示运行指定路径以test开头的模块
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
