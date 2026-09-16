from locators.event.group_registration_info_locators import GroupRegistrationInfoLocators as L
from pages.base_page import BasePage


class GroupRegistrationInfoPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "GroupRegistrationInfoPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Group registration info sheet not shown"
        assert self.is_visible(L.BTN_SWITCH_TO_GROUP, timeout=5), "Group registration switch button not shown"
        assert self.is_visible(L.BTN_LEARN_MORE, timeout=5), "Group registration learn more button not shown"
        self.capture_step("group_registration_info")
        return self

    def switch_to_group_registration(self):
        self.capture_step("switch_to_group_registration")
        self.click(L.BTN_SWITCH_TO_GROUP)

    def open_learn_more(self):
        self.capture_step("open_learn_more")
        self.click(L.BTN_LEARN_MORE)

    def tap_close(self):
        self.capture_step("tap_close")
        self.click(L.BTN_CLOSE)

    def title_text(self):
        return self.label_of(L.TXT_TITLE)

    def bullet_text(self, text):
        return self.label_of(L.TXT_BULLET_BY_TEXT.format(text))

    def has_bullet(self, text, timeout=5):
        return self.is_visible(L.TXT_BULLET_BY_TEXT.format(text), timeout)
