from flows.base_flow import BaseFlow
from pages.homepage.home_page import HomePage
from pages.driving_range.driving_range_list_page import DrivingRangeListPage
from pages.driving_range.driving_range_search_page import DrivingRangeSearchPage
from pages.driving_range.driving_range_details_page import DrivingRangeDetailsPage
from pages.driving_range.featured_promos_page import FeaturedPromosPage
from pages.driving_range.date_picker_page import DatePickerPage
from pages.driving_range.bay_picker_page import BayPickerPage
from pages.driving_range.booking_confirmation_page import BookingConfirmationPage
from pages.driving_range.available_promos_page import AvailablePromosPage
from pages.driving_range.add_promo_code_page import AddPromoCodePage
from pages.driving_range.payment_method_page import PaymentMethodPage
from pages.driving_range.payment_gateway_page import PaymentGatewayPage
from pages.driving_range.booking_success_page import BookingSuccessPage
from pages.driving_range.dr_booking_details_page import DrBookingDetailsPage
from pages.swing_credits.swing_credits_page import SwingCreditsPage
from pages.swing_credits.credits_history_page import CreditsHistoryPage
from helpers import amounts


class DrivingRangeFlow(BaseFlow):
    FLOW_NAME = "DrivingRangeFlow"

    def __init__(self, driver, reporter=None):
        super().__init__(driver, reporter)
        self.home = self.page(HomePage)
        self.list = self.page(DrivingRangeListPage)
        self.search = self.page(DrivingRangeSearchPage)
        self.details = self.page(DrivingRangeDetailsPage)
        self.featured = self.page(FeaturedPromosPage)
        self.calendar = self.page(DatePickerPage)
        self.bays = self.page(BayPickerPage)
        self.confirm = self.page(BookingConfirmationPage)
        self.promos = self.page(AvailablePromosPage)
        self.promo_code = self.page(AddPromoCodePage)
        self.payment = self.page(PaymentMethodPage)
        self.gateway = self.page(PaymentGatewayPage)
        self.success = self.page(BookingSuccessPage)
        self.booking = self.page(DrBookingDetailsPage)
        self.credits = self.page(SwingCreditsPage)
        self.history = self.page(CreditsHistoryPage)

    def open_home_tab(self):
        self.home.open_home_tab()
        
    def open_driving_range(self, member_type = ""):
        self.home.open_driving_range()
        self.list.verify_screen(member_type)
    
    def open_swing_credits(self):
        self.home.wait_until_loaded()
        self.home.open_credits()
        self.credits.verify_screen()
    
    def open_swing_credit_history(self):
        self.credits.open_history()
        self.history.verify_screen()
    
    def verify_earn_credit_booking_code(self, booking_code: str, total_amount):
        self.history.open_earned_tab()
        self.history.verify_credit_by_booking_code(booking_code)
        earned = abs(self.history.booking_amount_number(booking_code))
        expected = abs(amounts.to_number(total_amount))
        assert earned == expected, (
            f"earned credits for {amounts.booking_tag(booking_code)} do not match: "
            f"expected {expected}, found {earned}")
        
    def only_swing_pass_partners(self, member_type = ""):
        self.list.scroll_to_swing_pass_filter()
        self.list.enable_swing_pass_filter()
        self.list.verify_screen(member_type)

    def all_partners(self, member_type = ""):
        self.list.scroll_to_swing_pass_filter()
        self.list.disable_swing_pass_filter()
        self.list.verify_screen(member_type)

    def open_search(self):
        self.list.open_search()
        self.search.verify_screen()

    def search_driving_range(self, name):
        self.search.enter_search(name)
        self.search.submit_search()
        self.search.verify_result_search(name)

    def open_result(self, name):
        self.search.open_result(name)
        self.details.verify_screen()

    def see_all_details_sections(self):
        self.details.verify_all_sections()

    def open_featured_promos(self):
        self.details.open_featured_promos()
        self.featured.verify_screen()

    def find_featured_promo(self, name):
        self.featured.scroll_to_promo(name)

    def open_featured_promo(self, name):
        self.featured.open_promo(name)

    def back_to_details(self):
        self.featured.tap_back()
        self.details.verify_screen()

    def open_calendar(self):
        self.details.open_date_picker()
        self.calendar.verify_screen()

    def choose_date(self, label):
        self.calendar.select_day(label)

    def choose_bay_type(self, name):
        if name:
            self.details.select_bay_type(name)

    def choose_time(self, time, time_end=None):
        self.details.select_time(time, time_end)

    def choose_duration(self, duration):
        self.details.select_duration(duration)

    def book_driving_range(self):
        self.details.tap_book()
        self.bays.verify_screen()

    def add_bay(self):
        self.bays.increase_bays()

    def set_bays(self, count):
        self.bays.set_bays(count)

    def confirm_bays(self):
        self.bays.tap_confirm()
        self.confirm.verify_screen()

    def add_addons(self, addons):
        self.confirm.set_items(addons)

    def set_balls(self, option, count):
        self.confirm.set_balls(option, count)
    
    def set_items(self, items):
        if items:
            self.confirm.set_items(items)

    def add_balls(self, option):
        self.confirm.add_balls(option)

    def set_addon(self, name, count):
        self.confirm.set_addon(name, count)

    def add_addon(self, name):
        self.confirm.add_addon(name)

    def remove_addon(self, name):
        self.confirm.remove_addon(name)

    def enter_note(self, text):
        self.confirm.enter_note(text)

    def use_swing_credits(self):
        self.confirm.toggle_swing_credits()

    def open_promos(self):
        self.confirm.open_promos()
        self.promos.verify_screen()

    def remove_promo(self):
        if self.confirm.get_promo_in_btn_promo() != "Apply promo":
            self.open_promos()
            self.promos.remove_promo()
            self.promos.tap_back()

    def apply_promo(self, promo_name):
        if promo_name not in self.confirm.get_promo_in_btn_promo():
            self.open_promos()
            self.promos.enter_search(promo_name)
            self.promos.apply_promo(promo_name)
    
    def apply_and_redeem_promo(self, promo_name, promo_code):
        self.open_promos()
        self.open_promo_code()
        self.apply_promo_code(promo_code)
        self.promos.enter_search(promo_name)
        self.promos.apply_promo(promo_name)

    def open_promo_code(self):
        self.promos.open_add_promo_code()
        self.promo_code.verify_screen()

    def apply_promo_code(self, code):
        self.promo_code.enter_promo_code(code)
        self.promo_code.tap_add()

    def back_to_confirmation(self):
        self.promos.tap_back()
        self.confirm.verify_screen()

    def choose_payment_method(self, name):
        self.confirm.open_payment_method()
        self.payment.verify_screen()
        self.payment.select_method(name)

    def verify_booking_confirmation(self):
        self.confirm.verify_screen()

    def pay_now(self):
        self.confirm.tap_pay_now()
        self.proceed_to_pay()

    def proceed_to_pay(self):
        self.gateway.tap_proceed_to_pay()

    def verify_payment_success(self):
        self.success.verify_screen()

    def open_booking_details(self):
        self.success.open_booking_details()
        self.booking.verify_screen()
    
    def back_to_activity(self):
        self.booking.tap_back()
        
    
    def verify_button_exclusive_featured_promo(self, member_type):
        self.details.verify_exclusive_swing_pass_promo(member_type)
    
    def verify_maximum_bays_driving_range(self, tot_bays):
        self.bays.set_bays(tot_bays)
        self.bays.verify_maximum_bays(tot_bays)
    
    def verify_maximum_balls(self):
        assert self.confirm.button_balls_increase_is_disabled("balls"), (
            "balls increase button is still enabled at the maximum")
    
    def get_payment_information_before_payment(self, used_credit = "0"):
        return self.confirm.payment_information(used_credit)

    def get_booking_code_after_payment(self):
        return self.success.booking_code_text()
    
    def verify_minimum_balls(self):
        assert self.confirm.is_visible_minimum_toaster(), ("is visible minimum toaster is false")
    
    def verify_auto_applied_promo(self, promo_name):
        promo_auto_applied = self.confirm.get_promo_in_btn_promo()
        assert promo_name in promo_auto_applied and "promo auto applied!" in promo_auto_applied, ( # type: ignore
            f"auto applied promo does not match: expected {promo_name} with 'promo auto applied!', found {promo_auto_applied}")
    
    def verify_booking_information(self, player_name, date, start_time, end_time, bay_type:str = ""):
        assert player_name == self.confirm.player_name_text(), (f"player name does not match player name text: expected {player_name}, found {self.confirm.player_name_text()}")
        assert date in self.confirm.booking_date_text(), (f"booking date text does not contain date: expected {date}, found {self.confirm.booking_date_text()}")
        assert start_time in self.confirm.booking_time_text(), (f"booking time text does not contain start time: expected {start_time}, found {self.confirm.booking_time_text()}")
        assert self.confirm.get_duration(start_time, end_time) in self.confirm.duration_text(), (f"duration text does not contain get duration(start time, end time): expected {self.confirm.get_duration(start_time, end_time)}, found {self.confirm.duration_text()}")
        if bay_type:
            assert bay_type == self.confirm.bay_type_text(), (f"bay type does not match bay type text: expected {bay_type}, found {self.confirm.bay_type_text()}")
    
    def verify_payment_success_driving_range(self, player_name, date, start_time, end_time, number_of_bay ,payment_information, bay_type=""):
        assert player_name == self.success.player_name_text(), (f"player name does not match player name text: expected {player_name}, found {self.success.player_name_text()}")
        assert date in self.success.booking_date_text(), (f"booking date text does not contain date: expected {date}, found {self.success.booking_date_text()}")
        assert start_time in self.success.booking_time_text(), (f"booking time text does not contain start time: expected {start_time}, found {self.success.booking_time_text()}")
        assert self.confirm.get_duration(start_time, end_time) in self.success.duration_text(), (f"duration text does not contain get duration(start time, end time): expected {self.confirm.get_duration(start_time, end_time)}, found {self.success.duration_text()}") # type: ignore
        assert number_of_bay in self.success.number_of_bays_text(), (f"number of bays text does not contain number of bay: expected {number_of_bay}, found {self.success.number_of_bays_text()}")
        if bay_type:
            assert bay_type == self.success.bay_type_text(), (f"bay type does not match bay type text: expected {bay_type}, found {self.success.bay_type_text()}")
        assert amounts.to_number(payment_information["total_payment"]) == amounts.to_number(
                self.success.total_payment_text()), (
            f"total payment on the success screen does not match: expected "
            f"{payment_information['total_payment']}, found {self.success.total_payment_text()}")
        if payment_information["earned_credit"]:
            assert amounts.to_number(payment_information["earned_credit"]) == amounts.to_number(
                    self.success.earned_credits_text()), (
                f"earned credits on the success screen do not match: expected "
                f"{payment_information['earned_credit']}, found {self.success.earned_credits_text()}")
    
    def verify_data_booking_details_with_credit_used(self, booking_code, player_name, date, start_time, end_time, number_of_bay ,payment_information, bay_type=""):
        assert booking_code in self.booking.booking_code_text(), (f"booking code text does not contain booking code: expected {booking_code}, found {self.booking.booking_code_text()}")
        assert player_name == self.booking.player_name_text(), (f"player name does not match player name text: expected {player_name}, found {self.booking.player_name_text()}")
        assert date in self.booking.booking_date_text(), (f"booking date text does not contain date: expected {date}, found {self.booking.booking_date_text()}")
        assert start_time in self.booking.booking_time_text(), (f"booking time text does not contain start time: expected {start_time}, found {self.booking.booking_time_text()}")
        assert self.confirm.get_duration(start_time, end_time) in self.booking.duration_text(), (f"duration text does not contain get duration(start time, end time): expected {self.confirm.get_duration(start_time, end_time)}, found {self.booking.duration_text()}") # type: ignore
        assert number_of_bay in self.booking.number_of_bays_text(), (f"number of bays text does not contain number of bay: expected {number_of_bay}, found {self.booking.number_of_bays_text()}")
        if bay_type:
            assert bay_type == self.booking.bay_type_text(), (f"bay type does not match bay type text: expected {bay_type}, found {self.booking.bay_type_text()}")
        assert amounts.to_number(payment_information["total_payment"]) == amounts.to_number(
                self.booking.total_payment_text()), (
            f"total payment on the booking details does not match: expected "
            f"{payment_information['total_payment']}, found {self.booking.total_payment_text()}")
        if payment_information["earned_credit"]:
            assert amounts.to_number(payment_information["earned_credit"]) == amounts.to_number(
                    self.booking.earned_credits_text()), (
                f"earned credits on the booking details do not match: expected "
                f"{payment_information['earned_credit']}, found {self.booking.earned_credits_text()}")
        assert amounts.to_number(payment_information["used_credit"]) == amounts.to_number(
                self.booking.used_credit_text()), (
            f"used credits on the booking details do not match: expected "
            f"{payment_information['used_credit']}, found {self.booking.used_credit_text()}")
    
    def verify_data_booking_details_without_credit_used(self, booking_code, player_name, date, start_time, end_time, number_of_bay ,payment_information, bay_type=""):
        assert booking_code in self.booking.booking_code_text(), (f"booking code text does not contain booking code: expected {booking_code}, found {self.booking.booking_code_text()}")
        assert player_name == self.booking.player_name_text(), (f"player name does not match player name text: expected {player_name}, found {self.booking.player_name_text()}")
        assert date in self.booking.booking_date_text(), (f"booking date text does not contain date: expected {date}, found {self.booking.booking_date_text()}")
        assert start_time in self.booking.booking_time_text(), (f"booking time text does not contain start time: expected {start_time}, found {self.booking.booking_time_text()}")
        assert self.confirm.get_duration(start_time, end_time) in self.booking.duration_text(), (f"duration text does not contain get duration(start time, end time): expected {self.confirm.get_duration(start_time, end_time)}, found {self.booking.duration_text()}") # type: ignore
        assert number_of_bay in self.booking.number_of_bays_text(), (f"number of bays text does not contain number of bay: expected {number_of_bay}, found {self.booking.number_of_bays_text()}")
        if bay_type:
            assert bay_type == self.booking.bay_type_text(), (f"bay type does not match bay type text: expected {bay_type}, found {self.booking.bay_type_text()}")
        assert amounts.to_number(payment_information["total_payment"]) == amounts.to_number(
                self.booking.total_payment_text()), (
            f"total payment on the booking details does not match: expected "
            f"{payment_information['total_payment']}, found {self.booking.total_payment_text()}")
        if payment_information["earned_credit"]:
            assert amounts.to_number(payment_information["earned_credit"]) == amounts.to_number(
                    self.booking.earned_credits_text()), (
                f"earned credits on the booking details do not match: expected "
                f"{payment_information['earned_credit']}, found {self.booking.earned_credits_text()}")
                    
    def verify_used_credit_booking_code(self, booking_code, total_amount):
        self.history.open_usage_tab()
        self.history.verify_credit_by_booking_code(booking_code)
        used = abs(self.history.booking_amount_number(booking_code))
        expected = abs(amounts.to_number(total_amount))
        assert used == expected, (
            f"used credits for {amounts.booking_tag(booking_code)} do not match: "
            f"expected {expected}, found {used}")
