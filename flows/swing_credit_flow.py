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

    def credit_amount_for(self, payment_information, player):
        lines = (payment_information or {}).get("players") or {}
        return lines.get(player, {}).get("used_credit", "")

    def verify_used_credit_by_player(self, booking_code, player, expected_amount):
        self.history.scroll_to_booking_player(booking_code, player)
        self.history.verify_credit_by_booking_code_player(booking_code, player)
        used = abs(self.history.booking_amount_number_for_player(booking_code, player))
        expected = abs(amounts.to_number(expected_amount))
        assert used == expected, (
            f"used credits for {amounts.booking_tag(booking_code)} and {player} do not match: "
            f"expected {expected}, found {used}")

    def used_credits_applied(self, payment_information):
        return bool(amounts.to_number((payment_information or {}).get("used_credit", "")))

    def verify_used_credit_booking_code_players(self, booking_code, payment_information,
                                                players=None, host=""):
        if not self.used_credits_applied(payment_information):
            self.log.info("swing credits were not used on this booking, skipping the history check")
            return
        self.history.open_usage_tab()
        lines = (payment_information or {}).get("players") or {}
        names = self.payment_player_names(players, host) or list(lines)
        rows = [player for player in names if self.history.has_booking_for_player(booking_code, player)]
        if rows:
            for player in rows:
                self.verify_used_credit_by_player(booking_code, player,
                                                  self.credit_amount_for(payment_information, player))
            missing = [player for player in names if player not in rows]
            assert not missing, (
                f"no swing credit row for {amounts.booking_tag(booking_code)} and {missing}")
            return
        total = sum(abs(amounts.to_number(self.credit_amount_for(payment_information, player)))
                    for player in names)
        self.verify_used_credit_booking_code(
            booking_code, total or payment_information.get("used_credit", ""))

    def verify_earn_credit_booking_code_players(self, booking_code, total_amount,
                                                players=None, host=""):
        self.history.open_earned_tab()
        names = self.payment_player_names(players, host)
        rows = [player for player in names if self.history.has_booking_for_player(booking_code, player)]
        if not rows:
            return self.verify_earn_credit_booking_code(booking_code, total_amount)
        earned = sum(abs(self.history.booking_amount_number_for_player(booking_code, player))
                     for player in rows)
        expected = abs(amounts.to_number(total_amount))
        assert earned == expected, (
            f"earned credits for {amounts.booking_tag(booking_code)} across {rows} do not match: "
            f"expected {expected}, found {earned}")
