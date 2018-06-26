import logging
from common.common_fun import Common, NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class LoginView(Common):
    username_type = (By.ID, 'com.huatec.myapplication:id/edt_1')
    password_type = (By.ID, 'com.huatec.myapplication:id/edt_2')
    loginBtn = (By.ID, 'com.huatec.myapplication:id/btn_login')
    webView = (By.CLASS_NAME, 'android.webkit.WebView')

    # 登录
    def login_action(self, username, password):
        self.check_cancelBtn()  # 点击取消升级

        logging.info('==========login_action==========')
        self.find_element(*self.username_type).send_keys(username)
        logging.info('username is:%s' % username)

        self.find_element(*self.password_type).send_keys(password)
        logging.info('password is:%s' % password)

        self.find_element(*self.loginBtn).click()
        logging.info('login finished!')

    # 检查登录状态
    def check_loginStatus(self):
        logging.info('==========check_loginStatus==========')
        try:
            WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_class_name('android.webkit.WebView'))
        except TimeoutException:
            logging.error('login fail!')  # 错误日志
            self.getScreenShot('login fail!')  # 截图
            return False  # 返回false
        else:
            logging.info('login success!')
            return True

    # 退出登录


# 用于调试
if __name__ == '__main__':
    driver = appium_desired()
    loginview = LoginView(driver)
    loginview.login_action('zxw', '1234')
    loginview.check_loginStatus()
