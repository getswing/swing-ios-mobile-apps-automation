from locators.country_picker_locators import CountryPickerLocators as L
from pages.base_page import BasePage


class CountryPickerPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "CountryPickerPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Country picker screen not shown"
        assert self.is_visible(L.EL_SEARCH_BAR, timeout=5), "Country search bar not shown"
        assert self.is_visible(L.BTN_BACK, timeout=5), "Country picker back button not shown"
        self.capture_step("Show Country Picker")
        return self

    def title_text(self):
        return self.text_of(L.TXT_TITLE)

    def tap_search_bar(self):
        self.capture_step("tap_search_bar")
        self.click(L.EL_SEARCH_BAR)

    def enter_search(self, text):
        self.type(L.INPUT_SEARCH, text)
        self.capture_step("Type Search", text)

    def clear_search(self):
        self.capture_step("clear_search")
        self.clear(L.INPUT_SEARCH)

    def select_country(self, name):
        self.capture_step("select_country")
        self.click(L.TXT_COUNTRY.format(name))

    def select_country_containing(self, text):
        self.capture_step("Select country", text)
        self.click(L.TXT_COUNTRY_CONTAINS.format(text))

    def select_country_at(self, index):
        self.capture_step("select_country_at")
        self.click(L.TXT_COUNTRY_BY_INDEX.format(index))

    def scroll_to_country(self, name):
        self.capture_step("scroll_to_country")
        self.scroll_to(L.TXT_COUNTRY.format(name))

    def has_country(self, name, timeout=5):
        return self.is_visible(L.TXT_COUNTRY.format(name), timeout)

    def country_items(self):
        return self.texts_of(L.LIST_COUNTRY_ROWS)

    def country_count(self):
        return self.count(L.LIST_COUNTRY_ROWS)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)
