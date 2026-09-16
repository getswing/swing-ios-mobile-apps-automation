from locators.booking_summary_locators import BookingSummaryLocators as L
from pages.base_page import BasePage


class BookingSummaryPage(BasePage):
    ROOT_LOCATOR = L.EL_TITLE
    PAGE_NAME = "BookingSummaryPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_TITLE, timeout=20), "Booking summary screen not shown"
        assert self.is_visible(L.TXT_NOTES_TITLE, timeout=5), "Booking notes section not shown"
        assert self.is_visible(L.TXT_PRICE_DETAILS_TITLE, timeout=5), "Price details section not shown"
        self.capture_step("booking_summary")
        return self

    def field_text(self, name):
        return self.text_of(L.TXT_FIELD.format(name))

    def notes_text(self):
        return self.text_of(L.TXT_NOTES_VALUE)

    def total_payment_text(self):
        return self.text_of(L.TXT_TOTAL_PAYMENT)

    def scroll_to_price_details(self):
        self.capture_step("scroll_to_price_details")
        self.scroll_to(L.TXT_PRICE_DETAILS_TITLE)

    def tap_processing_fee(self):
        self.capture_step("tap_processing_fee")
        self.click(L.EL_PROCESSING_FEE)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)
