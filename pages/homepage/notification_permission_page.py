from locators.notification_permission_locators import NotificationPermissionLocators as L
from pages.base_page import BasePage


class NotificationPermissionPage(BasePage):
    ROOT_LOCATOR = L.TXT_DESCRIPTION
    PAGE_NAME = "NotificationPermissionPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_DESCRIPTION, timeout=20), "Notification permission screen not shown"
        assert self.is_visible(L.BTN_ENABLE, timeout=5), "Enable notifications button not shown"
        assert self.is_visible(L.BTN_LATER, timeout=5), "I'll do it later button not shown"
        self.capture_step("Verify notification permission page")
        return self

    def description_text(self):
        return self.text_of(L.TXT_DESCRIPTION)

    def tap_enable(self):
        self.capture_step("Tap enable")
        self.click(L.BTN_ENABLE)

    def tap_later(self):
        self.capture_step("tap_later")
        self.click(L.BTN_LATER)

    def tap_unlabeled(self):
        self.capture_step("tap_unlabeled")
        self.click(L.BTN_UNLABELED)

    def is_shown(self, timeout=5):
        return self.is_visible(L.BTN_ENABLE, timeout)

    def dismiss(self):
        self.capture_step("dismiss")
        self.click(L.TXT_SCRIM)
