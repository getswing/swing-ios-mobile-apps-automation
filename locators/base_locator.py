from appium.webdriver.common.appiumby import AppiumBy


def to_tuple(locator):
    if isinstance(locator, (tuple, list)) and len(locator) == 2:
        return locator[0], locator[1]
    return AppiumBy.XPATH, str(locator)


def fmt(template, *args, **kwargs):
    return template.format(*args, **kwargs)


def by_name(value, element_type="*"):
    return f'//{element_type}[@name="{value}"]'


def by_label(value, element_type="*"):
    return f'//{element_type}[@label="{value}"]'


def by_value(value, element_type="*"):
    return f'//{element_type}[@value="{value}"]'


def by_type(element_type):
    return f"//{element_type}"


def contains_label(value, element_type="*"):
    return f'//{element_type}[contains(@label,"{value}")]'


def contains_name(value, element_type="*"):
    return f'//{element_type}[contains(@name,"{value}")]'


def visible(xpath):
    return f'{xpath}[@visible="true"]'


def enabled(xpath):
    return f'{xpath}[@enabled="true"]'


def nth(xpath, index):
    return f"({xpath})[{index}]"


def first(xpath):
    return nth(xpath, 1)


def last(xpath):
    return f"({xpath})[last()]"


def child(parent_xpath, element_type="*", index=None):
    path = f"{parent_xpath}/{element_type}"
    return f"{path}[{index}]" if index else path


def descendant(parent_xpath, element_type="*"):
    return f"{parent_xpath}//{element_type}"


def sibling_after(xpath, element_type="*"):
    return f"{xpath}/following-sibling::{element_type}"


def parent(xpath):
    return f"{xpath}/.."
