from locators.cancel_booking_dialog_locators import CancelBookingDialogLocators as L
from pages.base_page import BasePage


class CancelBookingDialogPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "CancelBookingDialogPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Cancel booking sheet not shown"
        assert self.is_visible(L.BTN_CONFIRM, timeout=5), "Cancel booking confirm button not shown"
        assert self.is_visible(L.BTN_GO_BACK, timeout=5), "Cancel booking go back button not shown"
        self.capture_step("Verify cancel booking sheet")
        return self

    def tap_confirm(self):
        self.capture_step("Tap cancel booking")
        self.click(L.BTN_CONFIRM)

    def tap_go_back(self):
        self.capture_step("Tap go back")
        self.click(L.BTN_GO_BACK)

    def dismiss(self):
        self.capture_step("Dismiss cancel booking sheet")
        self.click(L.TXT_SCRIM)

    def title_text(self):
        return self.text_of(L.TXT_TITLE)

    def description_text(self):
        return self.text_of(L.TXT_DESCRIPTION)

    def is_shown(self, timeout=5):
        return self.is_visible(L.TXT_TITLE, timeout)
