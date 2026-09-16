from locators.send_receipt_locators import SendReceiptLocators as L
from pages.base_page import BasePage


class SendReceiptPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "SendReceiptPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Send receipt sheet not shown"
        assert self.is_visible(L.INPUT_EMAIL, timeout=5), "Send receipt email field not shown"
        assert self.is_visible(L.BTN_SEND, timeout=5), "Send receipt submit button not shown"
        self.capture_step("send_receipt")
        return self

    def enter_email(self, email):
        self.capture_step("enter_email")
        self.type(L.INPUT_EMAIL, email, hide_keyboard=True)

    def clear_email(self):
        self.capture_step("clear_email")
        self.clear(L.INPUT_EMAIL)

    def email_value(self):
        return self.value_of(L.INPUT_EMAIL)

    def tap_send(self):
        self.capture_step("tap_send")
        self.click(L.BTN_SEND)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def dismiss(self):
        self.capture_step("dismiss")
        self.click(L.TXT_SCRIM)
