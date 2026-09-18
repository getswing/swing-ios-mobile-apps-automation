from locators.tee_time.group_booking_info_locators import GroupBookingInfoLocators as L
from pages.base_page import BasePage


class GroupBookingInfoPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "GroupBookingInfoPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Group booking info sheet not shown"
        assert self.is_visible(L.BTN_SWITCH_TO_GROUP, timeout=5), "Group booking switch button not shown"
        assert self.is_visible(L.BTN_LEARN_MORE, timeout=5), "Group booking learn more button not shown"
        assert self.is_visible(L.BTN_CLOSE, timeout=5), "Group booking close button not shown"
        self.capture_step("group_booking_info")
        return self

    def switch_to_group_booking(self):
        self.capture_step("switch_to_group_booking")
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

    def has_sheet(self, timeout=3):
        return self.is_visible(L.TXT_TITLE, timeout)

    def has_close_button(self, timeout=3):
        return self.is_visible(L.BTN_CLOSE, timeout)

    def bullet_items(self):
        return self.texts_of(L.LIST_BULLETS)
