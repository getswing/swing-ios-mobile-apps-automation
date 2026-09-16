from appium import webdriver
from appium.options.ios import XCUITestOptions

from config.capabilities import build_capabilities
from config.settings import settings
from helpers.logger import get_logger

log = get_logger("driver")


def create_driver(capability_overrides=None):
    caps = build_capabilities(capability_overrides)
    options = XCUITestOptions().load_capabilities(caps)
    url = settings.server_url()
    log.info(f"connecting to {url} target={settings.TARGET} device={settings.DEVICE_NAME}")
    driver = webdriver.Remote(command_executor=url, options=options)
    if settings.IMPLICIT_WAIT:
        driver.implicitly_wait(settings.IMPLICIT_WAIT)
    log.info(f"session started {driver.session_id}")
    return driver


def quit_driver(driver):
    if driver is None:
        return
    try:
        log.info(f"closing session {driver.session_id}")
        driver.quit()
    except Exception as exc:
        log.warning(f"driver quit failed: {exc}")
