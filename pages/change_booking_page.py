from locators.change_booking_locators import ChangeBookingLocators as L
from pages.base_page import BasePage


class ChangeBookingPage(BasePage):
    ROOT_LOCATOR = L.EL_TITLE
    PAGE_NAME = "ChangeBookingPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_TITLE, timeout=20), "Change booking screen not shown"
        assert self.is_visible(L.TAB_RESCHEDULE, timeout=5), "Reschedule tab not shown"
        assert self.is_visible(L.TAB_CANCELLATION, timeout=5), "Cancellation tab not shown"
        self.capture_step("change_booking")
        return self

    def open_reschedule_tab(self):
        self.capture_step("open_reschedule_tab")
        self.click(L.TAB_RESCHEDULE)

    def open_cancellation_tab(self):
        self.capture_step("open_cancellation_tab")
        self.click(L.TAB_CANCELLATION)

    def policy_hint_text(self):
        return self.text_of(L.TXT_POLICY_HINT)

    def policy_rules(self):
        return self.texts_of(L.LIST_POLICY_RULES)

    def has_reschedule_policy(self, timeout=5):
        return self.is_visible(L.TXT_RESCHEDULE_POLICY, timeout)

    def has_cancellation_policy(self, timeout=5):
        return self.is_visible(L.TXT_CANCELLATION_POLICY, timeout)

    def tap_continue_reschedule(self):
        self.capture_step("tap_continue_reschedule")
        self.click(L.BTN_CONTINUE_RESCHEDULE)

    def tap_continue_cancel(self):
        self.capture_step("tap_continue_cancel")
        self.click(L.BTN_CONTINUE_CANCEL)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)
