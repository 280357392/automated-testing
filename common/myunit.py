import unittest, logging
from common.desired_caps import appium_desired
from time import sleep


# 被测试用例类继承
class StartEnd(unittest.TestCase):
    # 用例开始前执行
    def setUp(self):
        logging.info('setUp')
        self.driver = appium_desired()

    # 用例结束后执行
    def tearDown(self):
        sleep(5)
        logging.info('tearDown')
        self.driver.close_app()  # 退出app
