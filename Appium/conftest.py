import pytest
from appium import webdriver
import os
from datetime import datetime
import allure
from logging_config import logger


@pytest.fixture(scope='class')
def appium_driver(request):
    desired_caps = {
        "platformName": "Android",
        "deviceName": "RZCW90JT09E",
        "platformVersion": "14",
        "app": "C:\\Users\\admin\\Downloads\\ApiDemos-debug.apk",
        "appPackage": "io.appium.android.apis",
        "appActivity": ".ApiDemos",
        "noReset": True
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=desired_caps)

    yield driver

    if driver:
        driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(node, report):
    if report.failed:
        driver = node.funcargs.get('appium_driver')
        if driver:
            screenshot_path = f"screenshots/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_failure.png"
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            driver.save_screenshot(screenshot_path)
            logger.error(f"Screenshot saved to {screenshot_path}")
            allure.attach.file(screenshot_path, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
        logger.error(f"Test failed: {report.nodeid}")

