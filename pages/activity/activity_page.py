from locators.activity.activity_locators import ActivityLocators as L
from pages.base_page import BasePage


class ActivityPage(BasePage):
    ROOT_LOCATOR = L.EL_TITLE
    PAGE_NAME = "ActivityPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_TITLE, timeout=20), "Activity screen not shown"
        assert self.is_visible(L.IMG_TAB_DRIVING_RANGE, timeout=5), "Activity category tabs not shown"
        assert self.is_visible(L.TAB_ACTIVITY, timeout=5), "Activity tab bar not shown"
        self.capture_step("activity")
        return self

    def open_category_tab(self, name):
        self.capture_step("open_category_tab")
        self.click(L.IMG_CATEGORY_TAB.format(name))

    def open_driving_range_tab(self):
        self.capture_step("open_driving_range_tab")
        self.click(L.IMG_TAB_DRIVING_RANGE)

    def open_tee_time_tab(self):
        self.capture_step("open_tee_time_tab")
        self.click(L.IMG_TAB_TEE_TIME)

    def open_booking(self, text):
        self.capture_step("open_booking")
        self.click(L.CELL_BOOKING.format(text))

    def scroll_to_booking(self, text):
        self.capture_step("scroll_to_booking")
        self.scroll_to(L.CELL_BOOKING.format(text))

    def has_booking(self, text, timeout=5):
        return self.is_visible(L.CELL_BOOKING.format(text), timeout)

    def booking_items(self):
        return self.texts_of(L.LIST_BOOKING_CARDS)

    def booking_count(self):
        return self.count(L.LIST_BOOKING_CARDS)

    def upcoming_count(self):
        return self.count(L.LIST_UPCOMING)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def open_notifications(self):
        self.capture_step("open_notifications")
        self.click(L.BTN_NOTIFICATION)

    def open_home_tab(self):
        self.capture_step("open_home_tab")
        self.click(L.TAB_HOME)

    def open_account_tab(self):
        self.capture_step("open_account_tab")
        self.click(L.TAB_ACCOUNT)
