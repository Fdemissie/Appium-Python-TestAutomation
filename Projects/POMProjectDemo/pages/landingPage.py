from Projects.POMProjectDemo.locators.locators import Locators


class LandingPage():
    def __init__(self, driver):
        self.driver = driver
        self.factorial_textFeild_xpath = Locators.factorial_textFeild_xpath
        self.calculate_xpath = Locators.calculate_xpath
        self.outputMessage = Locators.outnput_message_xpath

    def enterInteger(self, postiveInteger):
        self.driver.find_element_by_xpath(self.factorial_textFeild_xpath).clear()
        self.driver.find_element_by_xpath(self.factorial_textFeild_xpath).send_keys(postiveInteger)

    def clickCalcualteButton(self):
        self.driver.find_element_by_link_text(self.calculate_xpath).click()

    def checkOutputMessage(self):
        msg = self.driver.find_element_by_xpath(self.outputMessage).text
        return msg
