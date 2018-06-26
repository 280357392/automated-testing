from appium import webdriver
import logging.config
import yaml
import os

# 日志配置
CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def appium_desired():
    # 读取配置文件
    with open('../config/kyb_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file)

    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['appName'])

    # 配置
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['automationName'] = data['automationName']
    desired_caps['app'] = app_path
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    logging.info('Start App......')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(8)
    return driver


if __name__ == '__main__':
    appium_desired()

# 启动APP
