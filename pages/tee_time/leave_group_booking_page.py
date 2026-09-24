from locators.tee_time.leave_group_booking_locators import LeaveGroupBookingLocators as L
from pages.base_page import BasePage


class LeaveGroupBookingPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "LeaveGroupBookingPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Leave group booking sheet not shown"
        assert self.is_visible(L.TXT_MESSAGE, timeout=5), "Leave group booking message not shown"
        assert self.is_visible(L.BTN_LEAVE, timeout=5), "Leave group booking button not shown"
        assert self.is_visible(L.BTN_STAY, timeout=5), "Stay in the booking button not shown"
        self.capture_step("leave_group_booking")
        return self

    def tap_leave(self):
        self.capture_step("tap_leave_group_booking")
        self.click(L.BTN_LEAVE)

    def tap_stay(self):
        self.capture_step("tap_stay_in_booking")
        self.click(L.BTN_STAY)

    def has_sheet(self, timeout=3):
        return self.is_visible(L.TXT_TITLE, timeout)
