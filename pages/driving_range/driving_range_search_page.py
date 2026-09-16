from locators.driving_range.driving_range_search_locators import DrivingRangeSearchLocators as L
from pages.base_page import BasePage


class DrivingRangeSearchPage(BasePage):
    ROOT_LOCATOR = L.INPUT_SEARCH
    PAGE_NAME = "DrivingRangeSearchPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.INPUT_SEARCH, timeout=20), "Driving range search screen not shown"
        assert self.is_visible(L.EL_COUNTRY, timeout=5), "Driving range search country selector not shown"
        self.capture_step("Verify driving range search page")
        return self

    def enter_search(self, text):
        self.type(L.INPUT_SEARCH, text)
        self.capture_step("Type Search", text)

    def submit_search(self):
        self.capture_step("Submit search")
        self.click(L.BTN_KEYBOARD_SEARCH)
    
    def verify_result_search(self, name, timeout=5):
        assert self.is_visible(L.EL_RESULT_BY_NAME.format(name), timeout), ("self.is visible(L.EL RESULT BY NAME.format(name), timeout) is false")
        self.capture_step("Verify result search", f"{name}, {timeout}")

    def clear_search(self):
        self.capture_step("clear_search")
        self.click(L.BTN_CLEAR)

    def open_result(self, name):
        self.capture_step("Open result", name)
        self.click(L.EL_RESULT_BY_NAME.format(name))

    def search_value(self):
        return self.value_of(L.INPUT_SEARCH)

    def result_count_text(self):
        return self.label_of(L.TXT_RESULT_COUNT)

    def has_result(self, name, timeout=5):
        return self.is_visible(L.EL_RESULT_BY_NAME.format(name), timeout)
