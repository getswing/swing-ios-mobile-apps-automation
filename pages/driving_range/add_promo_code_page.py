from locators.driving_range.add_promo_code_locators import AddPromoCodeLocators as L
from pages.base_page import BasePage


class AddPromoCodePage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "AddPromoCodePage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Add promo code screen not shown"
        assert self.is_visible(L.INPUT_PROMO_CODE, timeout=5), "Add promo code input not shown"
        assert self.is_visible(L.BTN_ADD, timeout=5), "Add promo code button not shown"
        self.capture_step("add_promo_code")
        return self

    def enter_promo_code(self, code):
        self.capture_step("enter_promo_code")
        self.type(L.INPUT_PROMO_CODE, code, hide_keyboard=True, dismiss_with=L.TXT_FIELD_LABEL)

    def tap_add(self):
        self.capture_step("tap_add")
        self.click(L.BTN_ADD)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def dismiss(self):
        self.capture_step("dismiss")
        self.click(L.TXT_SCRIM)

    def promo_code_value(self):
        return self.value_of(L.INPUT_PROMO_CODE)

    def add_is_enabled(self):
        return self.is_enabled(L.BTN_ADD)
