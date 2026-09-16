from locators.verification_method_locators import VerificationMethodLocators as L
from pages.base_page import BasePage


class VerificationMethodPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "VerificationMethodPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Verification method sheet not shown"
        assert self.is_visible(L.IMG_SMS, timeout=5), "SMS verification option not shown"
        assert self.is_visible(L.IMG_WHATSAPP, timeout=5), "WhatsApp verification option not shown"
        assert self.is_visible(L.BTN_CONFIRM, timeout=5), "Verification confirm button not shown"
        self.capture_step("Verify verification method page")
        return self

    def title_text(self):
        return self.text_of(L.TXT_TITLE)

    def select_sms(self):
        self.capture_step("Select SMS")
        self.click(L.IMG_SMS)

    def select_whatsapp(self):
        self.capture_step("Select WhatsApp")
        self.click(L.IMG_WHATSAPP)

    def select_method(self, name):
        self.capture_step("select_method")
        self.click(L.IMG_METHOD.format(name))

    def has_method(self, name, timeout=5):
        return self.is_visible(L.IMG_METHOD.format(name), timeout)

    def method_items(self):
        return self.texts_of(L.LIST_METHODS)

    def method_count(self):
        return self.count(L.LIST_METHODS)

    def tap_confirm(self):
        self.capture_step("tap_confirm")
        self.click(L.BTN_CONFIRM)

    def confirm_is_enabled(self):
        return self.is_enabled(L.BTN_CONFIRM)

    def dismiss(self):
        self.capture_step("dismiss")
        self.click(L.TXT_SCRIM)
