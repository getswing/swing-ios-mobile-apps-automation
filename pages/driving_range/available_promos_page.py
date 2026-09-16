from locators.driving_range.available_promos_locators import AvailablePromosLocators as L
from pages.base_page import BasePage


class AvailablePromosPage(BasePage):
    ROOT_LOCATOR = L.EL_HEADER
    PAGE_NAME = "AvailablePromosPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_HEADER, timeout=20), "Available promos screen not shown"
        assert self.is_visible(L.EL_SEARCH, timeout=5), "Available promos search field not shown"
        assert self.is_visible(L.BTN_ADD_PROMO_CODE, timeout=5), "Available promos add promo code button not shown"
        self.capture_step("available_promos")
        return self

    def enter_search(self, text):
        self.type(L.INPUT_SEARCH, text)
        self.capture_step("Type search", text)

    def apply_promo(self, name):
        self.capture_step("Apply promo", name)
        self.scroll_and_click(L.BTN_APPLY_BY_PROMO.format(name))

    def remove_promo(self):
        self.capture_step("Remove promo")
        self.click(L.BTN_REMOVE_PROMO)

    def open_add_promo_code(self):
        self.capture_step("open_add_promo_code")
        self.click(L.BTN_ADD_PROMO_CODE)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def applied_promo_text(self):
        return self.label_of(L.EL_APPLIED_PROMO)

    def quota_text(self, name):
        return self.label_of(L.TXT_QUOTA_BY_PROMO.format(name))

    def has_promo(self, name, timeout=5):
        return self.is_visible(L.IMG_PROMO_BY_NAME.format(name), timeout)
