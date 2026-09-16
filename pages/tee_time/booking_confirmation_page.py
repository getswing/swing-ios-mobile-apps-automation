from locators.tee_time.booking_confirmation_locators import TeeTimeBookingConfirmationLocators as L
from pages.base_page import BasePage


class TeeTimeBookingConfirmationPage(BasePage):
    ROOT_LOCATOR = L.EL_HEADER
    PAGE_NAME = "TeeTimeBookingConfirmationPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_HEADER, timeout=20), "Tee time booking confirmation screen not shown"
        assert self.is_visible(L.BTN_BACK, timeout=5), "Tee time booking confirmation back button not shown"
        assert self.is_visible(L.BTN_PAY_NOW, timeout=5), "Tee time booking confirmation pay now button not shown"
        self.capture_step("tee_time_booking_confirmation")
        return self

    def open_booking_method(self):
        self.capture_step("open_booking_method")
        self.click(L.BTN_CHANGE_BOOKING_TYPE)

    def open_promos(self, player):
        self.capture_step("open_promos")
        self.click(L.EL_PROMO_BY_PLAYER.format(player))

    def open_addons(self, player):
        self.capture_step("open_addons")
        self.click(L.EL_ADDONS_BY_PLAYER.format(player))

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

    def show_more_terms(self):
        self.capture_step("show_more_terms")
        self.scroll_and_click(L.BTN_SHOW_MORE)

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
    

    def booking_date_text(self):
        return self.value_after_label(L.TXT_DATE_ROW)

    def session_text(self):
        return self.value_after_label(L.TXT_SESSION_ROW)

    def preferred_time_text(self):
        return self.value_after_label(L.TXT_PREFERRED_TIME_ROW)

    def booking_type_text(self):
        return self.label_of(L.TXT_BOOKING_TYPE)

    def player_text(self, player):
        return self.label_of(L.IMG_PLAYER_BY_NAME.format(player))

    def player_promo_text(self, player):
        return self.label_of(L.EL_PROMO_BY_PLAYER.format(player))

    def player_addons_text(self, player):
        return self.label_of(L.EL_ADDONS_BY_PLAYER.format(player))

    def open_credits_earnings(self):
        self.capture_step("Open Swing Credits earnings")
        self.click(L.EL_EARNED_CREDITS)

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

    def payment_information(self, used_credit="0"):
        payment_info = {
            "total_payment": self.total_payment_text(),
            "earned_credit": self.earned_credits_text(),
        }
        if str(used_credit) == "1":
            payment_info["used_credit"] = self.used_credits_text()
        return payment_info

    def earned_credits_text(self):
        return self.label_of(L.EL_EARNED_CREDITS)

    def used_credits_text(self):
        return self.label_of(L.SWITCH_USE_CREDITS)

    def payment_method_text(self, name):
        return self.label_of(L.IMG_PAYMENT_METHOD.format(name))

    def has_player(self, player, timeout=5):
        return self.is_visible(L.IMG_PLAYER_BY_NAME.format(player), timeout)

    def has_used_credits(self, timeout=5):
        return self.is_visible(L.SWITCH_USE_CREDITS, timeout)

    def used_credits_is_on(self):
        return self.is_selected(L.SWITCH_USE_CREDITS)

    def has_payment_method(self, name, timeout=5):
        return self.is_visible(L.IMG_PAYMENT_METHOD.format(name), timeout)

    def pay_now_is_enabled(self):
        return self.is_enabled(L.BTN_PAY_NOW)