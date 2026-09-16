from locators.reschedule_booking_locators import RescheduleBookingLocators as L
from pages.base_page import BasePage


class RescheduleBookingPage(BasePage):
    ROOT_LOCATOR = L.EL_TITLE
    PAGE_NAME = "RescheduleBookingPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_TITLE, timeout=20), "Reschedule booking screen not shown"
        assert self.is_visible(L.TXT_WEEK_RANGE, timeout=5), "Reschedule week range not shown"
        assert self.is_visible(L.BTN_CONFIRM_DATETIME, timeout=5), "Confirm new date button not shown"
        self.capture_step("reschedule_booking")
        return self

    def field_text(self, name):
        return self.text_of(L.TXT_FIELD.format(name))

    def week_range_text(self):
        return self.text_of(L.TXT_WEEK_RANGE)

    def tap_previous_week(self):
        self.capture_step("tap_previous_week")
        self.click(L.BTN_PREV_WEEK)

    def tap_next_week(self):
        self.capture_step("tap_next_week")
        self.click(L.BTN_NEXT_WEEK)

    def open_calendar(self):
        self.capture_step("open_calendar")
        self.click(L.BTN_OPEN_CALENDAR)

    def select_day(self, day):
        self.capture_step("select_day")
        self.click(L.BTN_DAY.format(day))

    def day_is_enabled(self, day):
        return self.is_enabled(L.BTN_DAY.format(day))

    def select_time(self, time_slot):
        self.capture_step("select_time")
        self.click(L.TXT_TIME_SLOT.format(time_slot))

    def scroll_to_time(self, time_slot):
        self.capture_step("scroll_to_time")
        self.scroll_to(L.TXT_TIME_SLOT.format(time_slot))

    def time_slots(self):
        return self.texts_of(L.LIST_TIME_SLOTS)

    def tap_confirm_datetime(self):
        self.capture_step("tap_confirm_datetime")
        self.click(L.BTN_CONFIRM_DATETIME)

    def confirm_is_enabled(self):
        return self.is_enabled(L.BTN_CONFIRM_DATETIME)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)
