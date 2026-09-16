from locators.booking_details_locators import BookingDetailsLocators as L
from pages.base_page import BasePage


class BookingDetailsPage(BasePage):
    ROOT_LOCATOR = L.EL_TITLE
    PAGE_NAME = "BookingDetailsPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_TITLE, timeout=20), "Booking details screen not shown"
        assert self.is_visible(L.TXT_SUMMARY_TITLE, timeout=5), "Booking summary section not shown"
        assert self.is_visible(L.TXT_BOOKING_ID, timeout=5), "Booking id not shown"
        self.capture_step("booking_details")
        return self

    def booking_id_text(self):
        return self.text_of(L.TXT_BOOKING_ID)

    def status_text(self):
        return self.text_of(L.TXT_STATUS_UPCOMING)

    def has_status(self, status, timeout=5):
        return self.is_visible(L.TXT_STATUS.format(status), timeout)

    def field_text(self, name):
        return self.text_of(L.TXT_FIELD.format(name))

    def has_field(self, name, timeout=5):
        return self.is_visible(L.TXT_FIELD.format(name), timeout)

    def total_payment_text(self):
        return self.label_of(L.IMG_TOTAL_PAYMENT)

    def tap_see_breakdown(self):
        self.capture_step("tap_see_breakdown")
        self.click(L.BTN_SEE_BREAKDOWN)

    def tap_see_receipt(self):
        self.capture_step("tap_see_receipt")
        self.click(L.BTN_SEE_RECEIPT)

    def tap_see_details(self):
        self.capture_step("tap_see_details")
        self.click(L.BTN_SEE_DETAILS)

    def scroll_to_history(self):
        self.capture_step("scroll_to_history")
        self.scroll_to(L.TXT_HISTORY)

    def open_history_entry(self, text):
        self.capture_step("open_history_entry")
        self.click(L.EL_HISTORY_ENTRY.format(text))

    def has_history_entry(self, text, timeout=5):
        return self.is_visible(L.IMG_HISTORY_ENTRY.format(text), timeout)

    def tap_more(self):
        self.capture_step("tap_more")
        self.click(L.BTN_MORE)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)
