from locators.select_date_locators import SelectDateLocators as L
from pages.base_page import BasePage


class SelectDatePage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "SelectDatePage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Select date screen not shown"
        assert self.is_visible(L.TXT_MONTH_RANGE, timeout=5), "Calendar month range not shown"
        self.capture_step("select_date")
        return self

    def month_range_text(self):
        return self.text_of(L.TXT_MONTH_RANGE)

    def select_date(self, date_label):
        self.capture_step("select_date")
        self.click(L.TXT_DATE.format(date_label))

    def select_date_containing(self, text):
        self.capture_step("select_date_containing")
        self.click(L.TXT_DATE_CONTAINS.format(text))

    def scroll_to_date(self, date_label):
        self.capture_step("scroll_to_date")
        self.scroll_to(L.TXT_DATE.format(date_label))

    def has_date(self, date_label, timeout=5):
        return self.is_visible(L.TXT_DATE.format(date_label), timeout)

    def date_is_disabled(self, date_label, timeout=5):
        return self.is_visible(L.TXT_DATE_CONTAINS.format(date_label + ", Disabled date"), timeout)

    def disabled_date_count(self):
        return self.count(L.LIST_DISABLED_DATES)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)
