from locators.onboarding.nationality_picker_locators import NationalityPickerLocators as L
from pages.base_page import BasePage


class NationalityPickerPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "NationalityPickerPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Nationality picker screen not shown"
        assert self.is_visible(L.EL_SEARCH_COUNTRY, timeout=5), "Nationality search field not shown"
        assert self.is_visible(L.BTN_BACK, timeout=5), "Nationality picker back button not shown"
        self.capture_step("Verify nationality picker page")
        return self

    def enter_search(self, text):
        self.type(L.INPUT_SEARCH, text)
        self.capture_step("Type Search", text)

    def select_country(self, name):
        self.capture_step("Select country", name)
        self.click(L.TXT_COUNTRY_BY_NAME.format(name))

    def scroll_to_country(self, name):
        self.capture_step("scroll_to_country")
        self.scroll_to(L.TXT_COUNTRY_BY_NAME.format(name))

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def title_text(self):
        return self.text_of(L.TXT_TITLE)

    def has_country(self, name, timeout=5):
        return self.is_visible(L.TXT_COUNTRY_BY_NAME.format(name), timeout)

    def country_items(self):
        return self.texts_of(L.LIST_COUNTRIES)

    def country_count(self):
        return self.count(L.LIST_COUNTRIES)
