import time
import unittest
import sys
import os
import HtmlTestRunner
sys.path.append(os.path.join(os.path.dirname(__file__), "...", ".."))
from Projects.POMProjectDemo.pages.landingPage import LandingPage
from Projects.POMProjectDemo.common.base import BaseClass


class FactorialForValidInputTest(BaseClass):

    def test_FactorialWithPositiveInput(self):
        inputValue = "5"
        driver = self.driver
        driver.get("https://qainterview.pythonanywhere.com/")
        landingPage = LandingPage(driver)
        landingPage.factorial_textFeild_xpath(inputValue)
        landingPage.calculate_xpath()
        message = LandingPage.checkOutputMessage()
        self.assertEqual("The factorial of " + inputValue + " is:")
        time.sleep(2)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./reports"))