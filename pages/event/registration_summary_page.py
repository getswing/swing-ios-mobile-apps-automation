from locators.event.registration_summary_locators import RegistrationSummaryLocators as L
from pages.base_page import BasePage


class RegistrationSummaryPage(BasePage):
    ROOT_LOCATOR = L.EL_HEADER
    PAGE_NAME = "RegistrationSummaryPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_HEADER, timeout=20), "Registration summary screen not shown"
        assert self.is_visible(L.BTN_BACK, timeout=5), "Registration summary back button not shown"
        assert self.is_visible(L.TXT_NOTES_TITLE, timeout=5), "Registration summary notes section not shown"
        self.capture_step("registration_summary")
        return self

    def open_player_details(self):
        self.capture_step("open_player_details")
        self.click(L.EL_SEE_PLAYER_DETAILS)

    def open_leaderboard(self):
        self.capture_step("open_leaderboard")
        self.click(L.EL_LEADERBOARD_BANNER)

    def scroll_to_price_details(self):
        self.capture_step("scroll_to_price_details")
        self.scroll_to(L.TXT_PRICE_DETAILS_TITLE)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def event_name_text(self, name):
        return self.label_of(L.TXT_EVENT_NAME.format(name))

    def value_of_label(self, label):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format(label))

    def date_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Date"))

    def starting_time_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Starting time"))

    def venue_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Venue"))

    def registration_type_text(self):
        return self.label_of(L.TXT_REGISTRATION_TYPE)

    def player_text(self, name):
        return self.label_of(L.IMG_PLAYER_BY_NAME.format(name))

    def player_count(self):
        return self.count(L.LIST_PLAYERS)

    def player_items(self):
        return self.texts_of(L.LIST_PLAYERS)

    def package_line_text(self):
        return self.value_after_label(L.TXT_PACKAGE_LINE)

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
