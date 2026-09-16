import pytest

from flows.event_flow import EventFlow
from flows.home_flow import HomeFlow
from flows.login_flow import LoginFlow
from helpers.pdf_report import init_pdf
from test_data.event_test_data import EventTestData as D
from test_data.player_data import load_players


class TestEvent:

    def _login(self, login_flow: LoginFlow, home_flow: HomeFlow):
        login_flow.open_login()
        login_flow.choose_country(D.COUNTRY_NAME)
        login_flow.enter_phone_number(D.PHONE_NUMBER)
        login_flow.continue_log_in()
        login_flow.choose_verification_method(D.METHOD_VERIFICATION)
        login_flow.verify_page_code_otp()
        login_flow.enter_otp_code(D.OTP, D.COUNTRY_NAME, D.PHONE_NUMBER)
        home_flow.select_sport_if_shown(D.SPORT_TYPE)
        home_flow.enable_notifications_if_shown()
        home_flow.enable_location_if_shown()
        home_flow.dismiss_coachmark_if_shown()
        home_flow.close_whats_new_if_shown()
        home_flow.verify_home()

    def _open_standard_registration(self, event_flow: EventFlow):
        event_flow.open_events()
        event_flow.find_event(D.EVENT)
        event_flow.open_event(D.EVENT)
        event_flow.secure_slot()
        event_flow.choose_standard_registration()

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["EVENT_001", "EVENT_002", "EVENT_003"])
    def test_verify_page_explore_event(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, event_flow: EventFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        event_flow.open_events()

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["EVENT_004"])
    def test_verify_page_explore_event_swing_pass_only(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, event_flow: EventFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        event_flow.open_events()
        event_flow.only_swing_pass_partners()

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["EVENT_005"])
    def test_verify_page_event_details(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, event_flow: EventFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        event_flow.open_events()
        event_flow.find_event(D.EVENT)
        event_flow.open_event(D.EVENT)
        event_flow.see_event_information()

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["EVENT_006"])
    def test_verify_registration_method_event(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, event_flow: EventFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        event_flow.open_events()
        event_flow.find_event(D.EVENT)
        event_flow.open_event(D.EVENT)
        event_flow.secure_slot()

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["EVENT_007"])
    def test_verify_registration_confirmation_standard(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, event_flow: EventFlow):
        D.load(TC_ID)
        PLAYERS = load_players(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        self._open_standard_registration(event_flow)
        event_flow.verify_registration_information(D.EVENT_DATE, D.STARTING_TIME, D.VENUE,
                                                   D.REGISTRATION_METHOD, PLAYERS)
        event_flow.verify_registration_confirmation_players(PLAYERS)

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["EVENT_008", "EVENT_009", "EVENT_010"])
    def test_verify_auto_applied_promo_event(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, event_flow: EventFlow):
        D.load(TC_ID)
        PLAYERS = load_players(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        self._open_standard_registration(event_flow)
        event_flow.verify_players_promos(PLAYERS)

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["EVENT_011", "EVENT_012"])
    def test_registration_event_host_only(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, event_flow: EventFlow):
        D.load(TC_ID)
        PLAYERS = load_players(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        self._open_standard_registration(event_flow)
        event_flow.fill_players_details(PLAYERS, D.QUESTION_ANSWER)
        event_flow.apply_player_promos(PLAYERS)
        event_flow.verify_players_promos(PLAYERS)
        event_flow.verify_registration_information(D.EVENT_DATE, D.STARTING_TIME, D.VENUE,
                                                   D.REGISTRATION_METHOD, PLAYERS)
        event_flow.choose_payment_method(D.PAYMENT_METHOD)
        payment_information = event_flow.get_payment_information_before_payment("0")
        event_flow.pay_now()
        registration_code = event_flow.get_registration_code_after_payment()
        event_flow.verify_payment_success_event(D.EVENT_DATE, D.STARTING_TIME, payment_information,
                                                PLAYERS, D.VENUE, D.PAYMENT_METHOD)
        event_flow.open_registration_details()
        event_flow.verify_registration_details(registration_code, D.EVENT_DATE, D.STARTING_TIME,
                                               D.VENUE)

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["EVENT_013", "EVENT_014", "EVENT_015", "EVENT_016"])
    def test_registration_event_with_invited_players(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, event_flow: EventFlow):
        D.load(TC_ID)
        PLAYERS = load_players(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        self._open_standard_registration(event_flow)
        event_flow.invite_players(PLAYERS)
        event_flow.fill_players_details(PLAYERS, D.QUESTION_ANSWER)
        event_flow.apply_player_promos(PLAYERS)
        event_flow.verify_registration_confirmation_players(PLAYERS)
        event_flow.verify_players_promos(PLAYERS)
        event_flow.choose_payment_method(D.PAYMENT_METHOD)
        payment_information = event_flow.get_payment_information_before_payment("0")
        event_flow.pay_now()
        registration_code = event_flow.get_registration_code_after_payment()
        event_flow.verify_payment_success_event(D.EVENT_DATE, D.STARTING_TIME, payment_information,
                                                PLAYERS, D.VENUE, D.PAYMENT_METHOD)
        event_flow.open_registration_details()
        event_flow.verify_registration_details(registration_code, D.EVENT_DATE, D.STARTING_TIME,
                                               D.VENUE)

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["EVENT_017"])
    def test_registration_event_with_flight(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, event_flow: EventFlow):
        D.load(TC_ID)
        PLAYERS = load_players(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        self._open_standard_registration(event_flow)
        event_flow.invite_players(PLAYERS)
        event_flow.fill_players_details(PLAYERS, D.QUESTION_ANSWER)
        event_flow.select_flight(D.FLIGHT)
        event_flow.apply_player_promos(PLAYERS)
        event_flow.verify_registration_confirmation_players(PLAYERS)
        event_flow.choose_payment_method(D.PAYMENT_METHOD)
        payment_information = event_flow.get_payment_information_before_payment("0")
        event_flow.pay_now()
        registration_code = event_flow.get_registration_code_after_payment()
        event_flow.verify_payment_success_event(D.EVENT_DATE, D.STARTING_TIME, payment_information,
                                                PLAYERS, D.VENUE, D.PAYMENT_METHOD)
        event_flow.open_registration_details()
        event_flow.verify_registration_details(registration_code, D.EVENT_DATE, D.STARTING_TIME,
                                               D.VENUE)

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["EVENT_018"])
    def test_registration_event_organizer_arranges_flight(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, event_flow: EventFlow):
        D.load(TC_ID)
        PLAYERS = load_players(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        self._open_standard_registration(event_flow)
        event_flow.invite_players(PLAYERS)
        event_flow.fill_players_details(PLAYERS, D.QUESTION_ANSWER)
        event_flow.let_organizer_arrange_flight()
        event_flow.apply_player_promos(PLAYERS)
        event_flow.choose_payment_method(D.PAYMENT_METHOD)
        payment_information = event_flow.get_payment_information_before_payment("0")
        event_flow.pay_now()
        registration_code = event_flow.get_registration_code_after_payment()
        event_flow.verify_payment_success_event(D.EVENT_DATE, D.STARTING_TIME, payment_information,
                                                PLAYERS, D.VENUE, D.PAYMENT_METHOD)
        event_flow.open_registration_details()
        event_flow.verify_registration_details(registration_code, D.EVENT_DATE, D.STARTING_TIME,
                                               D.VENUE)

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["EVENT_019"])
    def test_registration_event_with_redeemed_promo(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, event_flow: EventFlow):
        D.load(TC_ID)
        PLAYERS = load_players(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        self._open_standard_registration(event_flow)
        event_flow.fill_players_details(PLAYERS, D.QUESTION_ANSWER)
        event_flow.apply_player_promos(PLAYERS)
        event_flow.verify_players_promos(PLAYERS)
        event_flow.choose_payment_method(D.PAYMENT_METHOD)
        payment_information = event_flow.get_payment_information_before_payment("0")
        event_flow.pay_now()
        registration_code = event_flow.get_registration_code_after_payment()
        event_flow.verify_payment_success_event(D.EVENT_DATE, D.STARTING_TIME, payment_information,
                                                PLAYERS, D.VENUE, D.PAYMENT_METHOD)
        event_flow.open_registration_details()
        event_flow.verify_registration_details(registration_code, D.EVENT_DATE, D.STARTING_TIME,
                                               D.VENUE)
