from locators.tee_time.booking_summary_locators import TeeTimeBookingSummaryLocators as L
from pages.base_page import BasePage


class TeeTimeBookingSummaryPage(BasePage):
    ROOT_LOCATOR = L.EL_HEADER
    PAGE_NAME = "TeeTimeBookingSummaryPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_HEADER, timeout=20), "Tee time booking summary screen not shown"
        assert self.is_visible(L.BTN_BACK, timeout=5), "Tee time booking summary back button not shown"
        assert self.is_visible(L.TXT_NOTES_TITLE, timeout=5), "Tee time booking summary notes section not shown"
        self.capture_step("tee_time_booking_summary")
        return self

    def show_more_terms(self):
        self.capture_step("show_more_terms")
        self.scroll_and_click(L.BTN_SHOW_MORE)

    def scroll_to_price_details(self):
        self.capture_step("scroll_to_price_details")
        self.scroll_to(L.TXT_PRICE_DETAILS_TITLE)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def venue_name_text(self, name):
        return self.label_of(L.TXT_VENUE_NAME.format(name))

    def value_of_label(self, label):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format(label))

    def booking_date_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Date"))

    def session_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Session"))

    def preferred_time_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Preferred time"))

    def booking_type_text(self):
        return self.label_of(L.TXT_BOOKING_TYPE)

    def player_text(self, name):
        return self.label_of(L.IMG_PLAYER_BY_NAME.format(name))

    def player_count(self):
        return self.count(L.LIST_PLAYERS)

    def player_items(self):
        return self.texts_of(L.LIST_PLAYERS)

    def published_rate_text(self):
        return self.value_after_label(L.TXT_PUBLISHED_RATE)

    def promo_line_text(self, name):
        return self.value_after_label(L.TXT_PROMO_LINE_BY_NAME.format(name))

    def notes_text(self):
        return self.label_of(L.TXT_NOTES_VALUE)

    def price_line_text(self, player):
        return self.label_of(L.IMG_PRICE_LINE_BY_PLAYER.format(player))

    def processing_fee_text(self):
        return self.label_of(L.EL_PROCESSING_FEE)

    def total_payment_text(self):
        return self.value_after_label(L.TXT_TOTAL_PAYMENT)

    def has_player(self, name, timeout=5):
        return self.is_visible(L.IMG_PLAYER_BY_NAME.format(name), timeout)
