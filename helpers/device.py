import time

from helpers.logger import get_logger

log = get_logger("device")


def lock(driver, seconds=None):
    if seconds:
        driver.execute_script("mobile: lock", {"seconds": seconds})
    else:
        driver.execute_script("mobile: lock")


def unlock(driver):
    driver.execute_script("mobile: unlock")


def is_locked(driver):
    return driver.execute_script("mobile: isLocked")


def shake(driver):
    driver.execute_script("mobile: shake")


def rotate(driver, orientation="LANDSCAPE"):
    driver.orientation = orientation.upper()


def get_orientation(driver):
    return driver.orientation


def press_home(driver):
    driver.execute_script("mobile: pressButton", {"name": "home"})


def press_button(driver, name):
    driver.execute_script("mobile: pressButton", {"name": name})


def background_app(driver, seconds=5):
    driver.background_app(seconds)


def open_deeplink(driver, url, bundle_id=None):
    params = {"url": url}
    if bundle_id:
        params["bundleId"] = bundle_id
    driver.execute_script("mobile: deepLink", params)


def open_url(driver, url):
    driver.get(url)


def set_geolocation(driver, latitude, longitude, altitude=0):
    driver.set_location(latitude, longitude, altitude)


def get_geolocation(driver):
    return driver.location


def device_info(driver):
    return driver.execute_script("mobile: deviceInfo")


def battery_info(driver):
    return driver.execute_script("mobile: batteryInfo")


def device_time(driver):
    return driver.device_time


def screen_info(driver):
    return driver.execute_script("mobile: deviceScreenInfo")


def get_clipboard(driver):
    return driver.get_clipboard_text()


def set_clipboard(driver, text):
    driver.set_clipboard_text(text)


def set_biometric_enrollment(driver, enabled=True):
    driver.execute_script("mobile: enrollBiometric", {"isEnabled": enabled})


def match_biometric(driver, match_type="touchId", should_match=True):
    driver.execute_script(
        "mobile: sendBiometricMatch", {"type": match_type, "match": should_match}
    )


def set_permission(driver, bundle_id, permissions):
    driver.execute_script(
        "mobile: setPermission", {"bundleId": bundle_id, "access": permissions}
    )


def get_permission(driver, bundle_id, service):
    return driver.execute_script(
        "mobile: getPermission", {"bundleId": bundle_id, "service": service}
    )


def siri_command(driver, text):
    driver.execute_script("mobile: siriCommand", {"text": text})


def get_settings(driver):
    return driver.get_settings()


def update_settings(driver, values):
    driver.update_settings(values)


def source(driver):
    return driver.page_source


def save_source(driver, path):
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(driver.page_source)
    log.info(f"page source saved to {path}")
    return path


def wait_seconds(seconds):
    time.sleep(seconds)


def get_contexts(driver):
    return driver.contexts


def switch_to_webview(driver, index=0):
    webviews = [ctx for ctx in driver.contexts if "WEBVIEW" in ctx.upper()]
    if not webviews:
        raise AssertionError("no webview context available")
    target = webviews[index]
    driver.switch_to.context(target)
    log.info(f"switched to {target}")
    return target


def switch_to_native(driver):
    driver.switch_to.context("NATIVE_APP")


def current_context(driver):
    return driver.current_context
