from locators.swing_credits.redeem_credits_locators import RedeemCreditsLocators as L
from pages.base_page import BasePage


class RedeemCreditsPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "RedeemCreditsPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Redeem credits screen not shown"
        assert self.is_visible(L.INPUT_CODE, timeout=5), "Redeem credits code field not shown"
        assert self.is_visible(L.BTN_REDEEM, timeout=5), "Redeem credits button not shown"
        self.capture_step("redeem_credits")
        return self

    def enter_code(self, code):
        self.capture_step("enter_code")
        self.type(L.INPUT_CODE, code, hide_keyboard=True, dismiss_with=L.TXT_TITLE)

    def tap_redeem(self):
        self.capture_step("tap_redeem")
        self.click(L.BTN_REDEEM)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def dismiss(self):
        self.capture_step("dismiss")
        self.click(L.TXT_SCRIM)

    def code_value(self):
        return self.value_of(L.INPUT_CODE)

    def redeem_is_enabled(self):
        return self.is_enabled(L.BTN_REDEEM)
