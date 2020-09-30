import time
import unittest
import sys
import os
import HtmlTestRunner
sys.path.append(os.path.join(os.path.dirname(__file__), "...", ".."))
from Projects.POMProjectDemo.pages.landingPage import LandingPage
from Projects.POMProjectDemo.common.base import BaseClass


class FoactorialForInvalidInputTest(BaseClass):
    url = "https://qainterview.pythonanywhere.com/"
    def test_FactorialWithNegativeInteger(self):
        inputValue = "-5"
        driver = self.driver
        driver.get(self.url)
        landingPage = LandingPage(driver)
        landingPage.factorial_textFeild_xpath(inputValue)
        landingPage.calculate_xpath()
        message = LandingPage.checkOutputMessage()
        self.assertEqual("Please enter a positive integer")
        time.sleep(2)

    def test_FactorialWithFraction(self):
        inputValue = "5.5"
        driver = self.driver
        driver.get(self.url)
        landingPage = LandingPage(driver)
        landingPage.factorial_textFeild_xpath(inputValue)
        landingPage.calculate_xpath()
        message = LandingPage.checkOutputMessage()
        self.assertEqual("Please enter an integer")
        time.sleep(2)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./reports"))