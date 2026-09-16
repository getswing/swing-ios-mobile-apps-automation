from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers.logger import get_logger

log = get_logger("alert")


def is_present(driver, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(EC.alert_is_present())
        return True
    except TimeoutException:
        return False


def text(driver):
    try:
        return driver.switch_to.alert.text
    except NoAlertPresentException:
        return None


ACCEPT_LABELS = (
    "Allow While Using App",
    "Allow Once",
    "Allow",
    "While Using the App",
    "OK",
    "Yes",
    "Continue",
    "Turn On",
)


def preferred_button(driver, candidates=ACCEPT_LABELS):
    try:
        available = buttons(driver) or []
    except Exception as exc:
        log.info(f"alert buttons not readable: {exc}")
        return None
    labels = [str(item).strip() for item in available]
    for wanted in candidates:
        for label in labels:
            if label.casefold() == wanted.casefold():
                return label
    log.info(f"no preferred accept button among {labels}")
    return None


def accept(driver, button_label=None):
    label = button_label or preferred_button(driver)
    params = {"action": "accept"}
    if label:
        params["buttonLabel"] = label
    driver.execute_script("mobile: alert", params)
    return label


def dismiss(driver, button_label=None):
    params = {"action": "dismiss"}
    if button_label:
        params["buttonLabel"] = button_label
    driver.execute_script("mobile: alert", params)


def buttons(driver):
    return driver.execute_script("mobile: alert", {"action": "getButtons"})


def accept_if_present(driver, timeout=3, button_label=None):
    if is_present(driver, timeout):
        message = text(driver)
        tapped = accept(driver, button_label)
        log.info(f"accepted alert: {message} via {tapped or 'default button'}")
        return True
    return False


def dismiss_if_present(driver, timeout=3, button_label=None):
    if is_present(driver, timeout):
        label = text(driver)
        dismiss(driver, button_label)
        log.info(f"dismissed alert: {label}")
        return True
    return False


def handle_all(driver, accept_alerts=True, max_alerts=5, timeout=2):
    handled = 0
    for _ in range(max_alerts):
        if not is_present(driver, timeout):
            break
        message = text(driver)
        if accept_alerts:
            tapped = accept(driver)
            log.info(f"accepted alert: {message} via {tapped or 'default button'}")
        else:
            dismiss(driver)
        handled += 1
    return handled
