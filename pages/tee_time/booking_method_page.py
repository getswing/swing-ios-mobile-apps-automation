from locators.tee_time.booking_method_locators import BookingMethodLocators as L
from pages.base_page import BasePage


class BookingMethodPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "BookingMethodPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Booking method sheet not shown"
        assert self.is_visible(L.EL_GROUP_BOOKING, timeout=5), "Booking method group booking option not shown"
        assert self.is_visible(L.EL_STANDARD_BOOKING, timeout=5), "Booking method standard booking option not shown"
        assert self.is_visible(L.BTN_LEARN_MORE, timeout=5), "Booking method learn more button not shown"
        self.capture_step("booking_method")
        return self

    def choose_group_booking(self):
        self.capture_step("choose_group_booking")
        self.click(L.EL_GROUP_BOOKING)

    def choose_standard_booking(self):
        self.capture_step("choose_standard_booking")
        self.click(L.EL_STANDARD_BOOKING)

    def choose_method(self, name):
        self.capture_step("choose_method")
        self.click(L.EL_METHOD_BY_NAME.format(name))

    def open_learn_more(self):
        self.capture_step("open_learn_more")
        self.click(L.BTN_LEARN_MORE)

    def tap_close(self):
        self.capture_step("tap_close")
        self.click(L.BTN_CLOSE)

    def title_text(self):
        return self.label_of(L.TXT_TITLE)

    def group_booking_text(self):
        return self.label_of(L.EL_GROUP_BOOKING)

    def standard_booking_text(self):
        return self.label_of(L.EL_STANDARD_BOOKING)

    def has_method(self, name, timeout=5):
        return self.is_visible(L.EL_METHOD_BY_NAME.format(name), timeout)
