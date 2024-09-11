import time

import pytest
from appium.webdriver.common.mobileby import MobileBy
import logging


class TestAppFunctionality:

    @pytest.mark.usefixtures("appium_driver")
    def test_element_click(self, appium_driver):
        driver = appium_driver

        # Find the element using the MobileBy class
        driver.find_element(MobileBy.ACCESSIBILITY_ID, "Graphics").click()
        logging.info("Clicked on the element-1")
        time.sleep(3)
        driver.find_element(MobileBy.ACCESSIBILITY_ID, "ColorFilters").click()
        logging.info("Clicked on the element-2")
