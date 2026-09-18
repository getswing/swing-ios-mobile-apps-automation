import time

from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.settings import settings
from locators.base_locator import to_tuple
from helpers.logger import get_logger

log = get_logger("wait")

IGNORED = (NoSuchElementException, StaleElementReferenceException)


def _wait(driver, timeout=None, poll=None):
    return WebDriverWait(
        driver,
        timeout if timeout is not None else settings.EXPLICIT_WAIT,
        poll_frequency=poll if poll is not None else settings.POLL_FREQUENCY,
        ignored_exceptions=IGNORED,
    )


def _until(driver, locator, timeout, condition, expected):
    seconds = timeout if timeout is not None else settings.EXPLICIT_WAIT
    try:
        return _wait(driver, timeout).until(condition(to_tuple(locator)))
    except TimeoutException:
        raise TimeoutException(f"element not {expected} after {seconds}s: {locator}") from None


def wait_present(driver, locator, timeout=None):
    return _until(driver, locator, timeout, EC.presence_of_element_located, "found")


def wait_visible(driver, locator, timeout=None):
    return _until(driver, locator, timeout, EC.visibility_of_element_located, "visible")


def wait_clickable(driver, locator, timeout=None):
    return _until(driver, locator, timeout, EC.element_to_be_clickable, "clickable")


def wait_all_visible(driver, locator, timeout=None):
    return _until(driver, locator, timeout, EC.visibility_of_all_elements_located, "visible")


def wait_invisible(driver, locator, timeout=None):
    return _until(driver, locator, timeout, EC.invisibility_of_element_located, "gone")


def wait_text_present(driver, locator, text, timeout=None):
    return _wait(driver, timeout).until(
        EC.text_to_be_present_in_element(to_tuple(locator), text)
    )


def wait_attribute(driver, locator, attribute, expected, timeout=None):
    def _check(drv):
        element = drv.find_element(*to_tuple(locator))
        return element.get_attribute(attribute) == expected

    return _wait(driver, timeout).until(_check)


def wait_condition(driver, condition, timeout=None, message=""):
    return _wait(driver, timeout).until(condition, message)


def wait_until_true(callback, timeout=None, interval=0.5, message="condition not met"):
    limit = timeout if timeout is not None else settings.EXPLICIT_WAIT
    deadline = time.time() + limit
    last_error = None
    while time.time() < deadline:
        try:
            if callback():
                return True
        except WebDriverException as exc:
            last_error = exc
        time.sleep(interval)
    raise TimeoutException(f"{message} after {limit}s ({last_error})")


def is_present(driver, locator, timeout=3):
    try:
        wait_present(driver, locator, timeout)
        return True
    except TimeoutException:
        return False


def is_visible(driver, locator, timeout=3):
    try:
        wait_visible(driver, locator, timeout)
        return True
    except TimeoutException:
        return False


def is_gone(driver, locator, timeout=None):
    try:
        wait_invisible(driver, locator, timeout)
        return True
    except TimeoutException:
        return False


def retry(action, attempts=None, delay=0.5):
    total = attempts if attempts is not None else settings.COMMAND_RETRY + 1
    last_error = None
    for index in range(total):
        try:
            return action()
        except (StaleElementReferenceException, WebDriverException) as exc:
            last_error = exc
            log.warning(f"retry {index + 1}/{total}: {type(exc).__name__}")
            time.sleep(delay)
    raise last_error
