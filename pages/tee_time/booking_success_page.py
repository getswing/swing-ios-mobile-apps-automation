from locators.tee_time.booking_success_locators import TeeTimeBookingSuccessLocators as L
from pages.base_page import BasePage


class TeeTimeBookingSuccessPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "TeeTimeBookingSuccessPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Tee time booking success screen not shown"
        assert self.is_visible(L.TXT_SUBTITLE, timeout=5), "Tee time booking success subtitle not shown"
        assert self.is_visible(L.TXT_BOOKING_CODE, timeout=5), "Tee time booking code not shown"
        assert self.is_visible(L.BTN_SEE_BOOKING_DETAILS, timeout=5), "Tee time see booking details button not shown"
        self.capture_step("tee_time_booking_success")
        return self

    def open_booking_details(self):
        self.capture_step("open_booking_details")
        self.click(L.BTN_SEE_BOOKING_DETAILS)

    def tap_finish(self):
        self.capture_step("tap_finish")
        self.click(L.BTN_FINISH)

    def title_text(self):
        return self.label_of(L.TXT_TITLE)

    def venue_name_text(self, name):
        return self.label_of(L.TXT_VENUE_NAME.format(name))

    def venue_text(self):
        return self.label_of(L.TXT_VENUE)

    def booking_code_text(self):
        return self.label_of(L.TXT_BOOKING_CODE)

    def value_of_label(self, label):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format(label))

    def booking_date_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Date"))

    def session_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Session"))

    def preferred_time_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Preferred tee time"))

    def players_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("No. of players"))

    def total_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Total"))

    def payment_method_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Payment method"))

    def earned_credits_text(self):
        return self.label_of(L.EL_EARNED_CREDITS)

    def has_earned_credits(self, timeout=5):
        return self.is_visible(L.EL_EARNED_CREDITS, timeout)

    def has_swing_pass_banner(self, timeout=5):
        return self.is_visible(L.EL_SWING_PASS_BANNER, timeout)

    def payment_information(self, used_credit="0"):
        payment_info = {
            "total_payment": self.total_text(),
            "earned_credit": self.earned_credits_text(),
            "payment_method": self.payment_method_text(),
        }
        return payment_info
