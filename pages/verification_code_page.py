from locators.verification_code_locators import VerificationCodeLocators as L
from pages.base_page import BasePage


class VerificationCodePage(BasePage):
    ROOT_LOCATOR = L.TXT_DESCRIPTION
    PAGE_NAME = "VerificationCodePage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_DESCRIPTION, timeout=20), "Verification code screen not shown"
        assert self.is_visible(L.INPUT_CODE, timeout=5), "Verification code field not shown"
        # assert self.is_visible(L.BTN_SEND_AGAIN, timeout=5), "Send again button not shown"
        assert self.is_visible(L.BTN_BACK, timeout=5), "Verification code back button not shown"
        self.capture_step("Verify verification code page")
        return self

    def description_text(self):
        return self.text_of(L.TXT_DESCRIPTION)

    def has_title(self, method, timeout=5):
        return self.is_visible(L.TXT_TITLE.format(method), timeout)

    def enter_code(self, code):
        self.capture_step("Enter code", code)
        self.type(L.INPUT_CODE, code, hide_keyboard=False)

    def clear_code(self):
        self.capture_step("clear_code")
        self.clear(L.INPUT_CODE)

    def code_value(self):
        return self.value_of(L.INPUT_CODE)

    def tap_send_again(self):
        self.capture_step("tap_send_again")
        self.click(L.BTN_SEND_AGAIN)

    def tap_try_other_method(self):
        self.capture_step("tap_try_other_method")
        self.click(L.LINK_TRY_OTHER_METHOD)

    def tap_try_method(self, method):
        self.capture_step("tap_try_method")
        self.click(L.LINK_TRY_METHOD.format(method))

    def other_method_text(self):
        return self.text_of(L.LINK_TRY_OTHER_METHOD)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)
