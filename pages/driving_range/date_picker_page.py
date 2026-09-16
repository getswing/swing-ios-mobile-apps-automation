from locators.driving_range.date_picker_locators import DatePickerLocators as L
from pages.base_page import BasePage


class DatePickerPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "DatePickerPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Date picker screen not shown"
        assert self.is_visible(L.TXT_MONTH_RANGE, timeout=5), "Date picker month range not shown"
        assert self.is_visible(L.BTN_BACK, timeout=5), "Date picker back button not shown"
        self.capture_step("Verify date picker page")
        return self

    def select_day(self, label):
        self.capture_step("Select day", label)
        self.scroll_and_click(L.TXT_DAY_BY_LABEL.format(label))

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def dismiss(self):
        self.capture_step("dismiss")
        self.click(L.TXT_SCRIM)

    def month_range_text(self):
        return self.label_of(L.TXT_MONTH_RANGE)

    def has_day(self, label, timeout=5):
        return self.is_visible(L.TXT_DAY_BY_LABEL.format(label), timeout)

    def enabled_day_count(self):
        return self.count(L.LIST_ENABLED_DAYS)

    def disabled_day_count(self):
        return self.count(L.TXT_DISABLED_DAY)
