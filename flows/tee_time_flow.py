from flows.base_flow import BaseFlow
from pages.homepage.home_page import HomePage
from pages.tee_time.tee_time_list_page import TeeTimeListPage
from pages.tee_time.tee_time_search_page import TeeTimeSearchPage
from pages.tee_time.golf_course_details_page import GolfCourseDetailsPage
from pages.tee_time.featured_promos_page import TeeTimeFeaturedPromosPage
from pages.tee_time.booking_method_page import BookingMethodPage
from pages.tee_time.booking_confirmation_page import TeeTimeBookingConfirmationPage
from pages.tee_time.available_promos_page import TeeTimeAvailablePromosPage
from pages.driving_range.add_promo_code_page import AddPromoCodePage
from pages.tee_time.add_ons_page import AddOnsPage
from pages.tee_time.add_player_page import AddPlayerPage
from pages.country_picker_page import CountryPickerPage
from pages.tee_time.group_booking_info_page import GroupBookingInfoPage
from pages.driving_range.payment_method_page import PaymentMethodPage
from pages.driving_range.payment_gateway_page import PaymentGatewayPage
from pages.tee_time.booking_success_page import TeeTimeBookingSuccessPage
from pages.tee_time.tt_booking_details_page import TeeTimeBookingDetailsPage
from pages.tee_time.booking_summary_page import TeeTimeBookingSummaryPage
from pages.tee_time.credits_earnings_page import TeeTimeCreditsEarningsPage
from helpers import amounts


class TeeTimeFlow(BaseFlow):
    FLOW_NAME = "TeeTimeFlow"

    def __init__(self, driver, reporter=None):
        super().__init__(driver, reporter)
        self.home = self.page(HomePage)
        self.list = self.page(TeeTimeListPage)
        self.search = self.page(TeeTimeSearchPage)
        self.details = self.page(GolfCourseDetailsPage)
        self.featured = self.page(TeeTimeFeaturedPromosPage)
        self.method = self.page(BookingMethodPage)
        self.confirm = self.page(TeeTimeBookingConfirmationPage)
        self.promos = self.page(TeeTimeAvailablePromosPage)
        self.promo_code = self.page(AddPromoCodePage)
        self.addons = self.page(AddOnsPage)
        self.player = self.page(AddPlayerPage)
        self.country = self.page(CountryPickerPage)
        self.group_info = self.page(GroupBookingInfoPage)
        self.payment = self.page(PaymentMethodPage)
        self.gateway = self.page(PaymentGatewayPage)
        self.success = self.page(TeeTimeBookingSuccessPage)
        self.booking = self.page(TeeTimeBookingDetailsPage)
        self.credits = self.page(TeeTimeCreditsEarningsPage)
        self.summary = self.page(TeeTimeBookingSummaryPage)

    def open_tee_time(self, member_type=""):
        self.home.open_tee_time()
        self.list.verify_screen(member_type)

    def only_swing_pass_partners(self, member_type="swing-pass"):
        self.list.scroll_to_swing_pass_filter()
        self.list.enable_swing_pass_filter()
        self.list.verify_screen(member_type)

    def all_partners(self, member_type=""):
        self.list.scroll_to_swing_pass_filter()
        self.list.disable_swing_pass_filter()
        self.list.verify_screen(member_type)

    def find_golf_course(self, text):
        self.list.scroll_to_card(text)

    def open_golf_course(self, text):
        self.list.open_card(text)
        self.details.verify_screen()

    def open_search(self):
        self.list.open_search()
        self.search.verify_screen()

    def search_golf_course(self, name):
        self.search.search(name)
        self.search.submit_search()

    def open_result(self, name):
        self.search.open_result(name)
        self.details.verify_screen()

    def open_recent_search(self, name):
        self.search.open_recent_search(name)

    def open_featured_promos(self):
        self.details.open_featured_promos()
        self.featured.verify_screen()

    def find_featured_promo(self, name):
        self.featured.scroll_to_promo(name)

    def back_to_details(self):
        self.featured.tap_back()
        self.details.verify_screen()

    def choose_date(self, label):
        self.details.open_calendar()
        self.details.select_date(label)

    def choose_session(self, name = ""):
        self.details.select_session(name)

    def choose_tee_time(self, time):
        self.details.select_slot(time)
    def see_all_details_sections(self):
        self.details.verify_all_sections()

    def find_date(self, label):
        self.details.swipe_to_date(label)

    def find_promo_on_details(self, name):
        self.details.swipe_to_promo(name)

    def see_course_information(self):
        self.details.show_more_information()

    def book_tee_time(self):
        self.details.tap_book_tee_time()
        self.method.verify_screen()

    def choose_standard_booking(self):
        self.method.choose_standard_booking()
        self.confirm.verify_screen()

    def choose_group_booking(self):
        self.method.choose_group_booking()
        self.confirm.verify_screen()

    def open_booking_method(self):
        self.confirm.open_booking_method()
        self.method.verify_screen()

    def switch_to_group_booking(self):
        self.group_info.switch_to_group_booking()
        self.confirm.verify_screen()

    def close_group_booking_info(self):
        self.group_info.tap_close()
        self.confirm.verify_screen()

    def open_promos(self, player):
        self.confirm.open_promos(player)
        self.promos.verify_screen()

    def find_promo(self, name):
        self.promos.search_promo(name)

    def apply_promo(self):
        self.promos.apply_promo()
        self.confirm.verify_screen()

    def apply_player_promo(self, player, promo_name):
        self.open_promos(player)
        self.find_promo(promo_name)
        self.apply_promo()

    def apply_player_promos(self, players):
        for player in players or []:
            if player.get("promo_name") and not player.get("promo_code"):
                self.apply_player_promo(player["player"], player["promo_name"])

    def redeem_player_promo(self, player, code):
        self.open_promos(player)
        self.open_promo_code()
        self.apply_promo_code(code)
        self.back_to_confirmation()

    def redeem_player_promos(self, players):
        for player in players or []:
            if player.get("promo_code"):
                self.redeem_player_promo(player["player"], player["promo_code"])

    def remove_promo(self):
        self.promos.remove_promo()

    def open_promo_code(self):
        self.promos.open_add_promo_code()
        self.promo_code.verify_screen()

    def apply_promo_code(self, code):
        self.promo_code.enter_promo_code(code)
        self.promo_code.tap_add()

    def back_to_confirmation(self):
        self.promos.tap_back()
        self.confirm.verify_screen()

    def open_addons(self, player):
        self.confirm.open_addons(player)
        self.addons.verify_screen()

    def add_addon(self, name):
        self.addons.add_item(name)

    def remove_addon(self, name):
        self.addons.remove_item(name)

    def save_addons(self):
        self.addons.tap_save()
        self.confirm.verify_screen()

    def set_player_addons(self, player, name, quantity=1):
        self.open_addons(player)
        for _ in range(int(quantity or 1)):
            self.add_addon(name)
        self.save_addons()

    def add_players_addons(self, players):
        for player in players or []:
            if player.get("add_ons_name"):
                self.set_player_addons(player["player"], player["add_ons_name"],
                                       player.get("add_ons_qty", 1))

    def cancel_addons(self):
        self.addons.tap_cancel()
        self.confirm.verify_screen()

    def use_swing_credits(self):
        self.confirm.toggle_swing_credits()

    def enter_note(self, text):
        self.confirm.enter_note(text)

    def add_player(self):
        self.confirm.add_player()
        self.player.verify_screen()

    def search_friend(self, name):
        self.player.search_friend(name)

    def select_friend(self, username):
        self.player.select_friend(username)
        self.confirm.verify_screen()

    def open_add_manually(self):
        self.player.open_add_manually_tab()

    def fill_player(self, first_name, last_name, phone_number):
        self.player.enter_first_name(first_name)
        self.player.enter_last_name(last_name)
        self.player.enter_phone_number(phone_number)

    def enter_player_email(self, email):
        self.player.enter_email(email)

    def open_player_country_picker(self):
        self.player.open_country_picker()
        self.country.verify_screen()

    def choose_player_country(self, name):
        self.country.select_country(name)
        self.player.verify_screen()

    def save_player(self):
        self.player.tap_save_player()
        self.confirm.verify_screen()

    def remove_player(self, player):
        self.confirm.remove_player(player)

    def open_payment_method(self):
        self.confirm.change_payment_method()
        self.payment.verify_screen()

    def choose_payment_method(self, name):
        self.payment.select_method(name)
        self.confirm.verify_screen()

    def invite_player(self, player):
        self.add_player()
        if str(player.get("add_method", "search")).lower() == "manual":
            self.open_add_manually()
            self.fill_player(player.get("first_name"), player.get("last_name"),
                             player.get("phone_number"))
            self.save_player()
        else:
            self.search_friend(player.get("search_keyword") or player.get("username"))
            self.select_friend(player.get("username"))

    def invite_players(self, players):
        for player in players or []:
            if str(player.get("add_method", "")).lower() not in ("", "host"):
                self.invite_player(player)

    def verify_booking_information(self, date, session, preferred_time, booking_type, players):
        assert date in self.confirm.booking_date_text(), (f"booking date text does not contain date: expected {date}, found {self.confirm.booking_date_text()}")
        assert session in self.confirm.session_text(), (f"session text does not contain session: expected {session}, found {self.confirm.session_text()}")
        assert preferred_time in self.confirm.preferred_time_text(), (f"preferred time text does not contain preferred time: expected {preferred_time}, found {self.confirm.preferred_time_text()}")
        assert booking_type in self.confirm.booking_type_text(), (f"booking type text does not contain booking type: expected {booking_type}, found {self.confirm.booking_type_text()}")
        for player in players or []:
            assert self.confirm.has_player(player["player"]), f"{player['player']} not in the booking"

    def verify_player_promo(self, player, promo_name):
        assert promo_name in self.confirm.player_promo_text(player), (f"player promo text(player) does not contain promo name: expected {promo_name}, found {self.confirm.player_promo_text(player)}")
    
    def verify_host_auto_applied_promo(self, player, promo_name):
        assert promo_name in self.confirm.player_promo_text(player), (f"player promo text(player) does not contain promo name: expected {promo_name}, found {self.confirm.player_promo_text(player)}")

    def verify_player_without_promo(self, player, promo_names=()):
        text = self.confirm.player_promo_text(player)
        for name in promo_names or ():
            assert name not in text, f"{player} should not use the promo {name}"

    def verify_players_promos(self, players):
        names = [player["promo_name"] for player in players or [] if player.get("promo_name")]
        for player in players or []:
            if player.get("promo_name"):
                self.verify_player_promo(player["player"], player["promo_name"])
            else:
                self.verify_player_without_promo(player["player"], names)

    def player_names(self, players):
        if not players:
            return []
        if isinstance(players, str):
            return [players]
        if isinstance(players, dict):
            return [players["player"]]
        return [player["player"] if isinstance(player, dict) else str(player) for player in players]

    def verify_auto_applied_promos(self, players, promo_name=""):
        for player in self.player_names(players):
            text = self.confirm.player_promo_text(player)
            assert promo_name in text if promo_name else "auto applied" in text.lower(), ( # type: ignore
                f"{player} does not show an auto applied promo")

    def verify_players_without_promo(self, players, promo_names=()):
        for player in self.player_names(players):
            self.verify_player_without_promo(player, promo_names)

    def apply_promo_for(self, player, promo_name):
        self.apply_player_promo(player, promo_name)

    def redeem_promo_for(self, player, code):
        self.redeem_player_promo(player, code)

    def verify_player_addons(self, player, name):
        assert name in self.confirm.player_addons_text(player), (f"player addons text(player) does not contain name: expected {name}, found {self.confirm.player_addons_text(player)}")

    def get_payment_information_before_payment(self, used_credit="0"):
        return self.confirm.payment_information(used_credit)

    def get_booking_code_after_payment(self):
        return self.success.booking_code_text()

    def verify_payment_success_tee_time(self, date, session, preferred_time, payment_information, venue="", payment_method="", player=1):
        self.success.verify_screen()
        assert self.success.booking_code_text(), "Booking code not shown on the success screen"
        assert date in self.success.booking_date_text(), (f"booking date text does not contain date: expected {date}, found {self.success.booking_date_text()}")
        if session:
            assert session in self.success.session_text(), (f"session text does not contain session: expected {session}, found {self.success.session_text()}")
        assert preferred_time in self.success.preferred_time_text(), (f"preferred time text does not contain preferred time: expected {preferred_time}, found {self.success.preferred_time_text()}")
        assert str(player) in self.success.players_text(), (f"players text does not contain str(player): expected {str(player)}, found {self.success.players_text()}") # type: ignore
        assert payment_information["total_payment"] in self.success.total_text(), (
            f"total on the success screen does not match: expected "
            f"{payment_information['total_payment']}, found {self.success.total_text()}")
        if venue:
            assert venue in self.success.venue_text(), (f"venue text does not contain venue: expected {venue}, found {self.success.venue_text()}") # type: ignore
        if payment_method:
            assert payment_method in self.success.payment_method_text(), (f"payment method text does not contain payment method: expected {payment_method}, found {self.success.payment_method_text()}") # type: ignore
        if payment_information.get("earned_credit"):
            assert payment_information["earned_credit"] in self.success.earned_credits_text(), (
            f"earned credits on the success screen do not match: expected "
            f"{payment_information['earned_credit']}, found {self.success.earned_credits_text()}")

    def verify_data_booking_details(self, booking_code, date, session, preferred_time,
                                    payment_information, player="1", status="UPCOMING"):
        self.booking.verify_screen()
        assert booking_code in self.booking.booking_code_text(), (f"booking code text does not contain booking code: expected {booking_code}, found {self.booking.booking_code_text()}")
        assert date in self.booking.booking_date_text(), (f"booking date text does not contain date: expected {date}, found {self.booking.booking_date_text()}")
        if session:
            assert session in self.booking.session_text(), (f"session text does not contain session: expected {session}, found {self.booking.session_text()}")
        assert preferred_time in self.booking.preferred_time_text(), (f"preferred time text does not contain preferred time: expected {preferred_time}, found {self.booking.preferred_time_text()}")
        assert str(player) in self.booking.players_text(), (f"players text does not contain str(player): expected {str(player)}, found {self.booking.players_text()}") # type: ignore
        assert amounts.to_number(payment_information["total_payment"]) == amounts.to_number(
            self.booking.total_payment_text()), (
            f"total payment on the booking details does not match: expected "
            f"{payment_information['total_payment']}, found {self.booking.total_payment_text()}")
        if status:
            assert self.booking.has_status(status), f"booking status {status} not shown"
        if payment_information.get("earned_credit"):
            assert amounts.to_number(payment_information["earned_credit"]) == amounts.to_number(
                self.booking.earned_credits_text()), (
                f"earned credits on the booking details do not match: expected "
                f"{payment_information['earned_credit']}, found {self.booking.earned_credits_text()}")

    def get_booking_details_information(self):
        return self.booking.payment_information()

    def pay_now(self):
        self.confirm.tap_pay_now()

    def proceed_to_pay(self):
        self.gateway.verify_screen()
        self.gateway.tap_proceed_to_pay()

    def verify_payment_success(self):
        self.success.verify_screen()

    def finish(self):
        self.success.tap_finish()

    def open_booking_details(self):
        self.success.open_booking_details()
        self.booking.verify_screen()

    def open_complete_breakdown(self):
        self.booking.open_breakdown()
        self.summary.verify_screen()

    def back_to_booking_details(self):
        self.summary.tap_back()
        self.booking.verify_screen()
    
    def verify_button_exclusive_featured_promo(self, player_type):
        self.details.verify_exclusive_swing_pass_promo(player_type)
    
    def verify_booking_confirmation_players(self, players):
        self.confirm.verify_screen()
        assert self.confirm.player_count() == len(players or []), (
            f"expected {len(players or [])} players, found {self.confirm.player_count()}")
        for player in players or []:
            assert self.confirm.has_player(player["player"]), f"{player['player']} not in the booking"
            if player.get("promo_name"):
                assert player["promo_name"] in self.confirm.player_promo_text(player["player"]), (
                    f"{player['player']} does not show the promo: expected "
                    f"{player['promo_name']}, found {self.confirm.player_promo_text(player['player'])}")
            if player.get("add_ons_name"):
                assert player["add_ons_name"] in self.confirm.player_addons_text(player["player"]), (
                    f"{player['player']} does not show the add on: expected "
                    f"{player['add_ons_name']}, found {self.confirm.player_addons_text(player['player'])}")
            assert self.confirm.price_line_text(player["player"]), (
                f"price detail line missing for {player['player']}")

    def verify_payment_success_players(self, date, session, preferred_time, payment_information,
                                       players, venue="", payment_method=""):
        self.verify_payment_success_tee_time(date, session, preferred_time, payment_information,
                                             venue, payment_method, str(len(players or []))) # type: ignore

    def verify_booking_details_players(self, booking_code, date, session, preferred_time,
                                       payment_information, players, status="UPCOMING"):
        self.verify_data_booking_details(booking_code, date, session, preferred_time,
                                         payment_information, str(len(players or [])), status)

    def open_credits_earnings(self):
        self.confirm.open_credits_earnings()
        self.credits.verify_screen()

    def verify_credits_earnings_players(self, players):
        self.credits.verify_screen()
        for player in players or []:
            assert self.credits.has_earning(player["player"]), (
                f"credits earning row missing for {player['player']}")

    def close_credits_earnings(self):
        self.credits.tap_got_it()
        self.confirm.verify_screen()

    def verify_booking_confirmation(self, booking_date, session, prefereed_time, method_booking):
        assert booking_date == self.confirm.booking_date_text(), (f"booking date does not match booking date text: expected {booking_date}, found {self.confirm.booking_date_text()}")
        assert session == self.confirm.session_text(), (f"session does not match session text: expected {session}, found {self.confirm.session_text()}")
        assert prefereed_time == self.confirm.preferred_time_text(), (f"prefereed time does not match preferred time text: expected {prefereed_time}, found {self.confirm.preferred_time_text()}")
        assert method_booking == self.confirm.booking_type_text(), (f"method booking does not match booking type text: expected {method_booking}, found {self.confirm.booking_type_text()}")
    
