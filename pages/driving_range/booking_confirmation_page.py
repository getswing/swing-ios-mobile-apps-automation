from locators.driving_range.booking_confirmation_locators import BookingConfirmationLocators as L
from pages.base_page import BasePage


class BookingConfirmationPage(BasePage):
    ROOT_LOCATOR = L.EL_HEADER
    PAGE_NAME = "BookingConfirmationPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_HEADER, timeout=20), "Booking confirmation screen not shown"
        assert self.is_visible(L.TXT_DATE_ROW, timeout=5), "Booking confirmation date row not shown"
        assert self.is_visible(L.TXT_BOOKING_TIME_ROW, timeout=5), "Booking confirmation booking time row not shown"
        assert self.is_visible(L.BTN_PAY_NOW, timeout=5), "Booking confirmation pay now button not shown"
        self.capture_step("Verify booking confirmation page")
        return self

    def add_balls(self, option):
        self.capture_step("add_balls", option)
        self.click(L.BTN_ITEM_INCREASE.format(option))

    def remove_balls(self, option):
        self.capture_step("remove_balls", option)
        self.click(L.BTN_ITEM_DECREASE.format(option))

    def set_balls(self, option, count):
        self.capture_step("set_balls", f"{option} = {count}")
        self.step_to(count, self.item_quantity(option), L.BTN_ITEM_INCREASE.format(option),
                     L.BTN_ITEM_DECREASE.format(option))

    def add_addon(self, name):
        self.capture_step("add_addon", name)
        self.click(L.BTN_ITEM_INCREASE.format(name))

    def remove_addon(self, name):
        self.capture_step("remove_addon", name)
        self.click(L.BTN_ITEM_DECREASE.format(name))

    def set_addon(self, name, count):
        self.capture_step("set_addon", f"{name} = {count}")
        self.step_to(count, self.item_quantity(name), L.BTN_ITEM_INCREASE.format(name),
                     L.BTN_ITEM_DECREASE.format(name))

    def set_items(self, items):
        self.capture_step("Set items", items)
        self.set_quantities(items, L.EL_ITEM_BY_NAME, L.BTN_ITEM_INCREASE, L.BTN_ITEM_DECREASE)

    def scroll_to_addons(self):
        self.capture_step("scroll_to_addons")
        self.scroll_to(L.TXT_ADDONS_TITLE)

    def enter_note(self, text):
        self.capture_step("enter_note")
        self.type(L.IMG_NOTE_INPUT, text, hide_keyboard=True)

    def open_reschedule_policy(self):
        self.capture_step("open_reschedule_policy")
        self.click(L.TXT_TAB_RESCHEDULE)

    def open_cancellation_policy(self):
        self.capture_step("open_cancellation_policy")
        self.click(L.TXT_TAB_CANCELLATION)

    def toggle_swing_credits(self):
        self.capture_step("toggle_swing_credits")
        self.click(L.SWITCH_USE_CREDITS)

    def open_promos(self):
        self.capture_step("open_promos")
        self.scroll_and_click(L.BTN_PROMO)
    
    def get_promo_in_btn_promo(self):
        self.scroll_to(L.BTN_PROMO)
        return self.text_of(L.BTN_PROMO)

    def open_payment_method(self):
        self.capture_step("open_payment_method")
        self.scroll_and_click(L.BTN_SELECT_PAYMENT)

    def change_payment_method(self):
        self.capture_step("change_payment_method")
        self.click(L.BTN_CHANGE_PAYMENT)

    def scroll_to_total_payment(self):
        self.capture_step("scroll_to_total_payment")
        self.scroll_to(L.TXT_TOTAL_PAYMENT)

    def tap_pay_now(self):
        self.capture_step("Tap pay now")
        self.click(L.BTN_PAY_NOW)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def item_quantity(self, name):
        return self.quantity_of(L.EL_ITEM_BY_NAME.format(name))

    def item_text(self, name):
        return self.label_of(L.EL_ITEM_BY_NAME.format(name))

    def ball_option_items(self):
        return self.texts_of(L.LIST_BALL_OPTIONS)

    def addon_items(self):
        return self.texts_of(L.LIST_ADDONS)

    def minimum_balls_text(self):
        return self.label_of(L.TXT_MINIMUM_BALLS)

    def has_balls_section(self, timeout=5):
        return self.is_visible(L.TXT_BALLS_TITLE, timeout)

    def has_addons_section(self, timeout=5):
        return self.is_visible(L.TXT_ADDONS_TITLE, timeout)

    def can_remove_item(self, name):
        return self.is_enabled(L.BTN_ITEM_DECREASE.format(name))

    def booking_date_text(self):
        return self.value_after_label(L.TXT_DATE_ROW)

    def booking_time_text(self):
        return self.value_after_label(L.TXT_BOOKING_TIME_ROW)

    def duration_text(self):
        return self.value_after_label(L.TXT_DURATION_ROW)

    def number_of_bays_text(self):
        return self.value_after_label(L.TXT_NUMBER_OF_BAYS_ROW)

    def bay_type_text(self):
        return self.value_after_label(L.TXT_BAY_TYPE_ROW)

    def player_name_text(self):
        return self.value_after_label(L.TXT_PLAYER_NAME_ROW)
            
    def total_payment_text(self):
        return self.value_after_label(L.TXT_TOTAL_PAYMENT)

    def price_line_text(self, label):
        return self.value_after_label(L.TXT_PRICE_LINE_BY_LABEL.format(label))

    def earned_credits_text(self):
        earning_credits = self.label_of(L.EL_EARNED_CREDITS) if self.is_visible(L.EL_EARNED_CREDITS) else ""
        return earning_credits

    def used_credits_text(self):
        used_credits = self.value_after_label(L.LBL_USED_CREDITS) if self.is_visible(L.LBL_USED_CREDITS) else ""
        return used_credits

    def has_bay_type(self, timeout=5):
        return self.is_visible(L.TXT_BAY_TYPE_ROW, timeout)

    def has_used_credits(self, timeout=5):
        return self.is_visible(L.SWITCH_USE_CREDITS, timeout)

    def used_credits_is_on(self):
        return self.is_selected(L.SWITCH_USE_CREDITS)

    def pay_now_is_enabled(self):
        return self.is_enabled(L.BTN_PAY_NOW)
    
    def button_increased_is_disabled(self, items):
        for item in items:
            return self.is_disabled(L.BTN_ITEM_INCREASE.format(item[""]))
    
    def button_decreased_is_disabled(self, name):
        return self.is_disabled(L.BTN_ITEM_DECREASE.format(name))
    
    def button_balls_increase_is_disabled(self, name):
        return self.is_disabled(L.BTN_ITEM_INCREASE.format(name))
    
    def get_duration(self, start_time, end_time):
        return self.duration_between(start_time, end_time)

    def is_visible_minimum_toaster(self):
        return self.is_visible(L.LBL_MINIMUM_BALLS_TOASTER)
    
    def booking_information(self):
        booking_info = {
            "player_name" : self.player_name_text(),
            "booking_date" : self.booking_date_text(),
            "booking_time" : self.booking_time_text(),
            "duration" : self.duration_text()
        }
        return booking_info

    def bay_type_information(self, bay_name: str = ""):
        bay_information = {}
        if bay_name:
            bay_information["bay_type"] = self.bay_type_text()
        return bay_information

    def payment_information(self, used_credit):
        payment_info = {
            "total_payment" : self.total_payment_text(),
            "earned_credit" : self.earned_credits_text()
        }
        if used_credit == "1":
            payment_info["used_credit"] = self.used_credits_text()
        
        return payment_info
        