from locators.cancellation_success_locators import CancellationSuccessLocators as L
from pages.base_page import BasePage


class CancellationSuccessPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "CancellationSuccessPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Cancellation success screen not shown"
        assert self.is_visible(L.TXT_BOOKING_ID, timeout=5), "Booking id not shown on the cancellation screen"
        assert self.is_visible(L.BTN_SEE_BOOKING_DETAILS, timeout=5), "See booking details button not shown"
        self.capture_step("Verify cancellation success page")
        return self

    def tap_finish(self):
        self.capture_step("Tap finish")
        self.click(L.BTN_FINISH)

    def tap_see_booking_details(self):
        self.capture_step("Tap see booking details")
        self.click(L.BTN_SEE_BOOKING_DETAILS)

    def title_text(self):
        return self.text_of(L.TXT_TITLE)

    def booking_id_text(self):
        return self.text_of(L.TXT_BOOKING_ID)

    def venue_text(self):
        return self.text_of(L.TXT_VENUE)

    def field_text(self, name):
        return self.text_of(L.TXT_FIELD.format(name))

    def value_of_label(self, label):
        return self.text_of(L.TXT_VALUE_BY_LABEL.format(label))

    def refund_text(self):
        return self.text_of(L.TXT_REFUND_LABEL)

    def has_refund(self, timeout=5):
        return self.is_visible(L.TXT_REFUND_LABEL, timeout)
