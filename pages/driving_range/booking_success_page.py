from locators.driving_range.booking_success_locators import BookingSuccessLocators as L
from pages.base_page import BasePage


class BookingSuccessPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "BookingSuccessPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Booking success screen not shown"
        assert self.is_visible(L.TXT_BOOKING_CODE, timeout=5), "Booking success booking code not shown"
        assert self.is_visible(L.BTN_FINISH, timeout=5), "Booking success finish button not shown"
        assert self.is_visible(L.BTN_SEE_BOOKING_DETAILS, timeout=5), "Booking success see booking details button not shown"
        self.capture_step("booking_success")
        return self

    def tap_finish(self):
        self.capture_step("tap_finish")
        self.click(L.BTN_FINISH)

    def open_booking_details(self):
        self.capture_step("Open booking details")
        self.click(L.BTN_SEE_BOOKING_DETAILS)

    def scroll_to_earned_credits(self):
        self.capture_step("scroll_to_earned_credits")
        self.scroll_to(L.TXT_EARNED_CREDITS_LABEL)

    def booking_code_text(self):
        return self.label_of(L.TXT_BOOKING_CODE)

    def value_of_label(self, label):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format(label))

    def booking_date_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Date"))

    def booking_time_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Booking time"))

    def duration_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Duration"))

    def number_of_bays_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Bays"))

    def bay_type_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Bay type"))

    def player_name_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Player name"))

    def total_payment_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Total"))

    def payment_method_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Payment method"))

    def earned_credits_text(self):
        return self.label_of(L.EL_EARNED_CREDITS)

    def has_bay_type(self, timeout=5):
        return self.is_visible(L.TXT_LABEL_BAY_TYPE, timeout)

    def has_earned_credits(self, timeout=5):
        return self.is_visible(L.EL_EARNED_CREDITS, timeout)
