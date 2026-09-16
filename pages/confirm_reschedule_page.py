from locators.confirm_reschedule_locators import ConfirmRescheduleLocators as L
from pages.base_page import BasePage


class ConfirmReschedulePage(BasePage):
    ROOT_LOCATOR = L.EL_TITLE
    PAGE_NAME = "ConfirmReschedulePage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_TITLE, timeout=20), "Confirm reschedule screen not shown"
        assert self.is_visible(L.TXT_REASON_TITLE, timeout=5), "Reschedule reason section not shown"
        assert self.is_visible(L.BTN_CONFIRM_AND_PAY, timeout=5), "Confirm reschedule and pay button not shown"
        self.capture_step("confirm_reschedule")
        return self

    def select_reason(self, reason):
        self.capture_step("select_reason")
        self.click(L.BTN_REASON.format(reason))

    def reason_is_selected(self, reason):
        return self.is_selected(L.BTN_REASON.format(reason))

    def scroll_to_reason(self, reason):
        self.capture_step("scroll_to_reason")
        self.scroll_to(L.BTN_REASON.format(reason))

    def field_text(self, name):
        return self.text_of(L.TXT_FIELD.format(name))

    def date_change_text(self):
        return self.label_of(L.IMG_DATE_CHANGE)

    def has_payment_method(self, name, timeout=5):
        return self.is_visible(L.IMG_PAYMENT_METHOD.format(name), timeout)

    def scroll_to_payment_details(self):
        self.capture_step("scroll_to_payment_details")
        self.scroll_to(L.TXT_PAYMENT_DETAILS)

    def tap_confirm_and_pay(self):
        self.capture_step("tap_confirm_and_pay")
        self.click(L.BTN_CONFIRM_AND_PAY)

    def confirm_is_enabled(self):
        return self.is_enabled(L.BTN_CONFIRM_AND_PAY)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)
