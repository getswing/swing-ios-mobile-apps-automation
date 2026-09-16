from locators.confirm_reschedule_dialog_locators import ConfirmRescheduleDialogLocators as L
from pages.base_page import BasePage


class ConfirmRescheduleDialogPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "ConfirmRescheduleDialogPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Confirm reschedule dialog not shown"
        assert self.is_visible(L.BTN_CONFIRM, timeout=5), "Dialog confirm button not shown"
        assert self.is_visible(L.BTN_GO_BACK, timeout=5), "Dialog go back button not shown"
        self.capture_step("confirm_reschedule_dialog")
        return self

    def title_text(self):
        return self.text_of(L.TXT_TITLE)

    def description_text(self):
        return self.text_of(L.TXT_DESCRIPTION)

    def tap_confirm(self):
        self.capture_step("tap_confirm")
        self.click(L.BTN_CONFIRM)

    def tap_go_back(self):
        self.capture_step("tap_go_back")
        self.click(L.BTN_GO_BACK)

    def is_shown(self, timeout=5):
        return self.is_visible(L.TXT_TITLE, timeout)
