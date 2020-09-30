from appium import webdriver
import unittest

class BaseClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        capabilities = {
            'platformName': 'Android',
            'platformVersion': '10.0',
            'deviceName': 'Pixel 3 API 29',
            'automationName': 'UIAutomator2',
            'browserName': 'Chrome'
        }
        #Appium webdriver
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")