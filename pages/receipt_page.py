from locators.receipt_locators import ReceiptLocators as L
from pages.base_page import BasePage


class ReceiptPage(BasePage):
    ROOT_LOCATOR = L.EL_TITLE
    PAGE_NAME = "ReceiptPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_TITLE, timeout=20), "Receipt screen not shown"
        assert self.is_visible(L.TXT_VENUE, timeout=5), "Receipt venue not shown"
        assert self.is_visible(L.BTN_SEND_RECEIPT, timeout=5), "Send receipt button not shown"
        self.capture_step("receipt")
        return self

    def title_text(self):
        return self.label_of(L.EL_TITLE)

    def reschedule_id_text(self):
        return self.text_of(L.TXT_RESCHEDULE_ID)

    def field_text(self, name):
        return self.text_of(L.TXT_FIELD.format(name))

    def tap_see_reschedule_details(self):
        self.capture_step("tap_see_reschedule_details")
        self.click(L.BTN_SEE_RESCHEDULE_DETAILS)

    def tap_contact_support(self):
        self.capture_step("tap_contact_support")
        self.click(L.EL_CONTACT_SUPPORT)

    def tap_send_receipt(self):
        self.capture_step("tap_send_receipt")
        self.click(L.BTN_SEND_RECEIPT)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)
