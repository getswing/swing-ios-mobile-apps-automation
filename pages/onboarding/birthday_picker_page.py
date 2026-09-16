from locators.onboarding.birthday_picker_locators import BirthdayPickerLocators as L
from pages.base_page import BasePage


class BirthdayPickerPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "BirthdayPickerPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Birthday picker screen not shown"
        assert self.is_visible(L.BTN_CONFIRM, timeout=5), "Birthday picker confirm button not shown"
        assert self.is_visible(L.BTN_BACK, timeout=5), "Birthday picker back button not shown"
        self.capture_step("Verify birthday picker page")
        return self

    def select_month(self, month):
        self.select_in_wheel(L.TXT_VALUE_BY_NAME.format(month), L.WHEEL_MONTH)
        self.capture_step("Select month", month)

    def select_day(self, day):
        self.select_in_wheel(L.TXT_VALUE_BY_NAME.format(day), L.WHEEL_DAY)
        self.capture_step("Select day", day)

    def select_year(self, year):
        self.select_in_wheel(L.TXT_VALUE_BY_NAME.format(year), L.WHEEL_YEAR)
        self.capture_step("Select year", year)

    def tap_confirm(self):
        self.capture_step("Tap confirm")
        self.click(L.BTN_CONFIRM)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def dismiss(self):
        self.capture_step("dismiss")
        self.click(L.TXT_SCRIM)

    def title_text(self):
        return self.text_of(L.TXT_TITLE)

    def has_value(self, value, timeout=5):
        return self.is_visible(L.TXT_VALUE_BY_NAME.format(value), timeout)

    def wheel_count(self):
        return self.count(L.LIST_WHEELS)
