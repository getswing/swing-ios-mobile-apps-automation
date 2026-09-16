from locators.tee_time.tt_booking_details_locators import TeeTimeBookingDetailsLocators as L
from pages.base_page import BasePage


class TeeTimeBookingDetailsPage(BasePage):
    ROOT_LOCATOR = L.EL_HEADER
    PAGE_NAME = "TeeTimeBookingDetailsPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_HEADER, timeout=20), "Tee time booking details screen not shown"
        assert self.is_visible(L.TXT_SUMMARY_TITLE, timeout=5), "Tee time booking summary section not shown"
        assert self.is_visible(L.TXT_BOOKING_CODE, timeout=5), "Tee time booking code not shown"
        assert self.is_visible(L.BTN_SEE_BREAKDOWN, timeout=5), "Tee time see complete breakdown button not shown"
        self.capture_step("tee_time_booking_details")
        return self

    def open_breakdown(self):
        self.capture_step("open_breakdown")
        self.click(L.BTN_SEE_BREAKDOWN)

    def open_receipt(self):
        self.capture_step("open_receipt")
        self.scroll_and_click(L.BTN_SEE_RECEIPT)

    def open_more(self):
        self.capture_step("open_more")
        self.click(L.BTN_MORE)

    def scroll_to_history(self):
        self.capture_step("scroll_to_history")
        self.scroll_to(L.TXT_HISTORY_TITLE)

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

    def session_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Session"))

    def preferred_time_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Preferred time"))

    def players_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("No. of players"))

    def subtotal_text(self):
        return self.value_after_label(L.TXT_SUBTOTAL)

    def processing_fee_text(self):
        return self.value_after_label(L.EL_PROCESSING_FEE)

    def total_payment_text(self):
        return self.value_after_label(L.IMG_TOTAL_PAYMENT)

    def earned_credits_text(self):
        return self.label_of(L.EL_EARNED_CREDITS)

    def history_item_text(self, name):
        return self.label_of(L.IMG_HISTORY_ITEM_BY_NAME.format(name))

    def history_item_count(self):
        return self.count(L.LIST_HISTORY_ITEMS)

    def payment_information(self, used_credit="0"):
        payment_info = {
            "subtotal": self.subtotal_text(),
            "processing_fee": self.processing_fee_text(),
            "total_payment": self.total_payment_text(),
            "earned_credit": self.earned_credits_text(),
        }
        return payment_info

    def has_credits_note(self, timeout=5):
        return self.is_visible(L.TXT_CREDITS_NOTE, timeout)

    def has_status(self, name, timeout=5):
        return self.is_visible(L.TXT_STATUS_BY_NAME.format(name), timeout)
