from locators.tee_time.tee_time_search_locators import TeeTimeSearchLocators as L
from pages.base_page import BasePage


class TeeTimeSearchPage(BasePage):
    ROOT_LOCATOR = L.INPUT_SEARCH
    PAGE_NAME = "TeeTimeSearchPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.INPUT_SEARCH, timeout=20), "Tee time search screen not shown"
        assert self.is_visible(L.EL_COUNTRY, timeout=5), "Tee time search country selector not shown"
        assert self.is_visible(L.BTN_BACK, timeout=5), "Tee time search back button not shown"
        self.capture_step("tee_time_search")
        return self

    def search(self, text):
        self.capture_step("search")
        self.type(L.INPUT_SEARCH, text)

    def submit_search(self):
        self.capture_step("submit_search")
        self.click(L.BTN_KEYBOARD_SEARCH)

    def clear_search(self):
        self.capture_step("clear_search")
        self.click(L.BTN_CLEAR)

    def open_result(self, name):
        self.capture_step("open_result")
        self.click(L.EL_RESULT_BY_NAME.format(name))

    def open_recent_search(self, name):
        self.capture_step("open_recent_search")
        self.click(L.BTN_RECENT_BY_NAME.format(name))

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def search_value(self):
        return self.value_of(L.INPUT_SEARCH)

    def result_count_text(self):
        return self.label_of(L.TXT_RESULT_COUNT)

    def has_result(self, name, timeout=5):
        return self.is_visible(L.EL_RESULT_BY_NAME.format(name), timeout)

    def has_recent_searches(self, timeout=5):
        return self.is_visible(L.TXT_RECENT_SEARCHES, timeout)

    def recent_search_items(self):
        return self.texts_of(L.LIST_RECENT_SEARCHES)
