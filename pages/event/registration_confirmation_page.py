from locators.event.registration_confirmation_locators import RegistrationConfirmationLocators as L
from pages.base_page import BasePage


class RegistrationConfirmationPage(BasePage):
    ROOT_LOCATOR = L.EL_HEADER
    PAGE_NAME = "RegistrationConfirmationPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_HEADER, timeout=20), "Registration confirmation screen not shown"
        assert self.is_visible(L.BTN_BACK, timeout=5), "Registration confirmation back button not shown"
        assert self.is_visible(L.BTN_PAY_NOW, timeout=5), "Registration confirmation pay now button not shown"
        self.capture_step("registration_confirmation")
        return self

    def open_registration_method(self):
        self.capture_step("open_registration_method")
        self.click(L.BTN_CHANGE_REGISTRATION_TYPE)

    def open_promos(self, player):
        self.capture_step("open_promos")
        self.click(L.EL_PROMO_BY_PLAYER.format(player))

    def open_player_details(self, player):
        self.capture_step("open_player_details")
        self.click(L.EL_PLAYER_DETAILS_BY_PLAYER.format(player))

    def toggle_swing_credits(self):
        self.capture_step("toggle_swing_credits")
        self.click(L.SWITCH_USE_CREDITS)

    def add_player(self):
        self.capture_step("add_player")
        self.scroll_and_click(L.BTN_ADD_PLAYER)

    def change_player(self, player):
        self.capture_step("change_player")
        self.click(L.IMG_CHANGE_PLAYER_BY_NAME.format(player))

    def remove_player(self, player):
        self.capture_step("remove_player")
        self.click(L.IMG_REMOVE_PLAYER_BY_NAME.format(player))

    def enter_note(self, text):
        self.capture_step("enter_note")
        self.type(L.IMG_NOTE_INPUT, text, hide_keyboard=True)

    def select_flight(self, name):
        self.capture_step("select_flight")
        self.scroll_and_click(L.SWITCH_FLIGHT_BY_NAME.format(name))

    def toggle_organizer_arrange(self):
        self.capture_step("toggle_organizer_arrange")
        self.scroll_and_click(L.SWITCH_ORGANIZER_ARRANGE)

    def scroll_to_total_payment(self):
        self.capture_step("scroll_to_total_payment")
        self.scroll_to(L.TXT_TOTAL_PAYMENT)

    def change_payment_method(self):
        self.capture_step("change_payment_method")
        self.scroll_and_click(L.BTN_CHANGE_PAYMENT)

    def tap_pay_now(self):
        self.capture_step("tap_pay_now")
        self.click(L.BTN_PAY_NOW)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def event_name_text(self, name):
        return self.label_of(L.TXT_EVENT_NAME.format(name))

    def date_text(self):
        return self.value_after_label(L.TXT_DATE_ROW)

    def starting_time_text(self):
        return self.value_after_label(L.TXT_STARTING_TIME_ROW)

    def venue_text(self):
        return self.value_after_label(L.TXT_VENUE_ROW)

    def players_text(self):
        return self.value_after_label(L.TXT_PLAYER_ROW)

    def registration_type_text(self):
        return self.label_of(L.TXT_REGISTRATION_TYPE)

    def player_text(self, player):
        return self.label_of(L.IMG_PLAYER_BY_NAME.format(player))

    def player_promo_text(self, player):
        return self.label_of(L.EL_PROMO_BY_PLAYER.format(player))

    def player_count(self):
        return self.count(L.LIST_PLAYERS)

    def player_items(self):
        return self.texts_of(L.LIST_PLAYERS)

    def price_line_text(self, player):
        return self.label_of(L.IMG_PRICE_LINE_BY_PLAYER.format(player))

    def processing_fee_text(self):
        return self.value_after_label(L.TXT_PROCESSING_FEE)

    def total_payment_text(self):
        return self.value_after_label(L.TXT_TOTAL_PAYMENT)

    def earned_credits_text(self):
        return self.label_of(L.EL_EARNED_CREDITS)

    def used_credits_text(self):
        return self.label_of(L.SWITCH_USE_CREDITS)

    def payment_method_text(self, name):
        return self.label_of(L.IMG_PAYMENT_METHOD.format(name))

    def unassigned_slot_count(self):
        return self.count(L.LIST_UNASSIGNED_SLOTS)

    def has_player(self, player, timeout=5):
        return self.is_visible(L.IMG_PLAYER_BY_NAME.format(player), timeout)

    def has_flight(self, name, timeout=5):
        return self.is_visible(L.EL_FLIGHT_BY_NAME.format(name), timeout)

    def has_used_credits(self, timeout=5):
        return self.is_visible(L.SWITCH_USE_CREDITS, timeout)

    def used_credits_is_on(self):
        return self.is_selected(L.SWITCH_USE_CREDITS)

    def flight_is_selected(self, name):
        return self.is_selected(L.SWITCH_FLIGHT_BY_NAME.format(name))

    def organizer_arrange_is_on(self):
        return self.is_selected(L.SWITCH_ORGANIZER_ARRANGE)

    def has_payment_method(self, name, timeout=5):
        return self.is_visible(L.IMG_PAYMENT_METHOD.format(name), timeout)

    def pay_now_is_enabled(self):
        return self.is_enabled(L.BTN_PAY_NOW)
