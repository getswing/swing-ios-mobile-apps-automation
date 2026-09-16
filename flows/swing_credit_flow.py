from flows.base_flow import BaseFlow
from pages.homepage.home_page import HomePage
from pages.swing_credits.swing_credits_page import SwingCreditsPage
from pages.swing_credits.credits_history_page import CreditsHistoryPage
from helpers import amounts


class SwingCreditFlow(BaseFlow):
    FLOW_NAME = "SwingCreditFlow"

    def __init__(self, driver, reporter=None):
        super().__init__(driver, reporter)
        self.home = self.page(HomePage)
        self.credits = self.page(SwingCreditsPage)
        self.history = self.page(CreditsHistoryPage)

    def open_swing_credits(self):
        self.home.wait_until_loaded()
        self.home.open_credits()
        self.credits.verify_screen()

    def verify_swing_credits(self):
        self.credits.verify_screen()

    def open_history(self):
        self.credits.open_history()
        self.history.verify_screen()

    def open_all_history(self):
        self.history.open_all_tab()
        self.history.verify_screen()

    def open_earned_history(self):
        self.history.open_earned_tab()
        self.history.verify_screen()

    def open_usage_history(self):
        self.history.open_usage_tab()
        self.history.verify_screen()

    def find_booking(self, code):
        self.history.scroll_to_booking(code)

    def open_booking(self, code):
        self.history.open_booking(code)

    def back_to_swing_credits(self):
        self.history.tap_back()
        self.credits.verify_screen()
    

    def verify_earn_credit_booking_code(self, booking_code: str, total_amount):
        self.history.open_earned_tab()
        self.history.verify_credit_by_booking_code(booking_code)
        earned = abs(self.history.booking_amount_number(booking_code))
        expected = abs(amounts.to_number(total_amount))
        assert earned == expected, (
            f"earned credits for {amounts.booking_tag(booking_code)} do not match: "
            f"expected {expected}, found {earned}")

    def verify_used_credit_booking_code(self, booking_code, total_amount):
        self.history.open_usage_tab()
        self.history.verify_credit_by_booking_code(booking_code)
        used = abs(self.history.booking_amount_number(booking_code))
        expected = abs(amounts.to_number(total_amount))
        assert used == expected, (
            f"used credits for {amounts.booking_tag(booking_code)} do not match: "
            f"expected {expected}, found {used}")
        
        
