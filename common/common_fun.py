from baseView.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
import time, os, logging, csv


class Common(BaseView):
    cancelBtn = (By.ID, 'android:id/button2')

    def check_cancelBtn(self):
        logging.info('check_cancelBtn')
        try:
            cancelBtn = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('no check_cancelBtn')
        else:
            cancelBtn.click()

    # 获取屏幕宽高
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 向左滑动<--
    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_size()
        startX = int(l[0] * 0.9)
        startY = int(l[1] * 0.5)
        endX = int(l[0] * 0.1)
        endY = int(l[1] * 0.5)
        self.swipe(startX, startY, endX, endY, 2000)

    # 向右滑动-->
    def swipeRight(self):
        logging.info('swipeRight')
        l = self.get_size()
        startX = int(l[0] * 0.1)
        startY = int(l[1] * 0.5)
        endX = int(l[0] * 0.9)
        endY = int(l[1] * 0.5)
        self.swipe(startX, startY, endX, endY, 2000)

    # 向上滑动
    def swipeUp(self):
        logging.info('swipeUp')
        l = self.get_size()
        startX = int(l[0] * 0.5)
        startY = int(l[1] * 0.65)
        endX = int(l[0] * 0.5)
        endY = int(l[1] * 0.35)
        self.swipe(startX, startY, endX, endY, 2000)

    # 向下滑动(幅度不要太大，按住标题就无法滑动了)
    def swipeDown(self):
        logging.info('swipeDown')
        l = self.get_size()
        startX = int(l[0] * 0.5)
        startY = int(l[1] * 0.35)
        endX = int(l[0] * 0.5)
        endY = int(l[1] * 0.65)
        self.swipe(startX, startY, endX, endY, 2000)

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    # 截图
    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)
        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)

    # 返回指定行的数据，从1开始
    def get_csv_data(self, csv_file, line):
        logging.info('get_csv_data')
        # 支持中文编码
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row


if __name__ == '__main__':
    # driver = appium_desired()  # 启动APP
    # com = Common(driver)
    # sleep(1)
    # driver.find_element_by_id('com.huatec.myapplication:id/btn_skip').click()
    # sleep(1)
    # com.swipeLeft()
    # sleep(1)
    # driver.find_element_by_id('com.huatec.myapplication:id/btn_hello1').click()
    # sleep(1)
    # com.swipeRight()
    # sleep(1)
    # com.swipeUp()
    # sleep(1)
    # driver.find_element_by_id('com.huatec.myapplication:id/btn_hello2').click()
    # sleep(1)
    # com.swipeDown()
    # sleep(1)
    # com.getScreenShot('swipe')
    image_file = os.path.dirname(os.path.dirname(__file__))
    print(image_file)
