from locators.driving_range.dr_booking_details_locators import DrBookingDetailsLocators as L
from pages.base_page import BasePage


class DrBookingDetailsPage(BasePage):
    ROOT_LOCATOR = L.EL_HEADER
    PAGE_NAME = "DrBookingDetailsPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_HEADER, timeout=20), "Booking details screen not shown"
        assert self.is_visible(L.TXT_SUMMARY_TITLE, timeout=5), "Booking details summary title not shown"
        assert self.is_visible(L.TXT_BOOKING_CODE, timeout=5), "Booking details booking code not shown"
        assert self.is_visible(L.TXT_PAYMENT_SUMMARY_TITLE, timeout=5), "Booking details payment summary not shown"
        self.capture_step("Verify driving range booking details page")
        return self

    def open_breakdown(self):
        self.capture_step("open_breakdown")
        self.click(L.BTN_SEE_BREAKDOWN)

    def open_receipt(self):
        self.capture_step("open_receipt")
        self.click(L.BTN_SEE_RECEIPT)

    def scroll_to_total_payment(self):
        self.capture_step("scroll_to_total_payment")
        self.scroll_to(L.IMG_TOTAL_PAYMENT)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def status_text(self):
        return self.label_of(L.TXT_STATUS)

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
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Number of bays"))

    def bay_type_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Bay type"))

    def player_name_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Player name"))

    def total_payment_text(self):
        return self.value_after_label(L.IMG_TOTAL_PAYMENT)

    def subtotal_text(self):
        return self.value_after_label(L.TXT_SUBTOTAL)

    def price_line_text(self, label):
        return self.value_after_label(L.TXT_PRICE_LINE_BY_LABEL.format(label))

    def earned_credits_text(self):
        return self.label_of(L.EL_EARNED_CREDITS)

    def has_bay_type(self, timeout=5):
        return self.is_visible(L.TXT_LABEL_BAY_TYPE, timeout)

    def has_earned_credits(self, timeout=5):
        return self.is_visible(L.EL_EARNED_CREDITS, timeout)
    
    def used_credit_text(self):
        return self.value_after_label(L.LBL_USED_CREDITS)
