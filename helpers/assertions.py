from helpers.logger import get_logger
from helpers.waits import is_visible

log = get_logger("assert")


def assert_visible(driver, locator, timeout=None, message=None):
    assert is_visible(driver, locator, timeout or 10), (
        message or f"expected visible: {locator}"
    )


def assert_not_visible(driver, locator, timeout=3, message=None):
    assert not is_visible(driver, locator, timeout), (
        message or f"expected not visible: {locator}"
    )


def assert_text_equals(actual, expected, message=None):
    assert actual == expected, message or f"expected '{expected}' but got '{actual}'"


def assert_text_contains(actual, fragment, message=None):
    assert fragment in (actual or ""), (
        message or f"expected '{fragment}' inside '{actual}'"
    )


def assert_true(condition, message="expected condition to be true"):
    assert condition, message


def assert_false(condition, message="expected condition to be false"):
    assert not condition, message


def assert_enabled(element, message=None):
    assert element.is_enabled(), message or "expected element to be enabled"


def assert_selected(element, message=None):
    assert element.get_attribute("value") in ("1", "true", True), (
        message or "expected element to be selected"
    )


def assert_count(elements, expected, message=None):
    assert len(elements) == expected, (
        message or f"expected {expected} elements but found {len(elements)}"
    )
