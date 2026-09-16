from locators.tee_time.available_promos_locators import TeeTimeAvailablePromosLocators as L
from pages.base_page import BasePage


class TeeTimeAvailablePromosPage(BasePage):
    ROOT_LOCATOR = L.EL_HEADER
    PAGE_NAME = "TeeTimeAvailablePromosPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_HEADER, timeout=20), "Tee time available promos screen not shown"
        assert self.is_visible(L.EL_SEARCH, timeout=5), "Tee time available promos search field not shown"
        assert self.is_visible(L.BTN_ADD_PROMO_CODE, timeout=5), "Tee time available promos add promo code button not shown"
        assert self.is_visible(L.BTN_BACK, timeout=5), "Tee time available promos back button not shown"
        self.capture_step("tee_time_available_promos")
        return self

    def search_promo(self, text):
        self.capture_step("search_promo")
        self.type(L.INPUT_SEARCH, text)

    def apply_promo(self):
        self.capture_step("apply_promo")
        self.click(L.BTN_APPLY)

    def remove_promo(self):
        self.capture_step("remove_promo")
        self.scroll_and_click(L.BTN_REMOVE_PROMO)

    def open_add_promo_code(self):
        self.capture_step("open_add_promo_code")
        self.click(L.BTN_ADD_PROMO_CODE)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def featured_title_text(self):
        return self.label_of(L.TXT_FEATURED_TITLE)

    def applied_promo_text(self):
        return self.label_of(L.EL_APPLIED_PROMO)

    def quota_text(self):
        return self.label_of(L.TXT_QUOTA)

    def has_applied_promo(self, timeout=5):
        return self.is_visible(L.EL_APPLIED_PROMO, timeout)

    def has_promo(self, name, timeout=5):
        return self.is_visible(L.EL_PROMO_BY_NAME.format(name), timeout)
