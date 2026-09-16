import pytest

from flows.cancellation_flow import CancellationFlow
from flows.home_flow import HomeFlow
from flows.login_flow import LoginFlow
from helpers.pdf_report import init_pdf
from test_data.cancellation_test_data import CancellationTestData as D


class TestCancellation:

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

    def _open_cancel_booking(self, cancellation_flow: CancellationFlow):
        cancellation_flow.verify_home()
        cancellation_flow.open_activity()
        cancellation_flow.choose_activity_filter(D.ACTIVITY_FILTER)
        cancellation_flow.find_activity_card(D.ACTIVITY_CARD)
        cancellation_flow.open_activity_card(D.ACTIVITY_CARD)
        cancellation_flow.verify_booking_details(D.BOOKING_CODE, D.STATUS_BEFORE)
        cancellation_flow.open_booking_options()
        cancellation_flow.choose_cancel_booking()
        cancellation_flow.verify_cancellation_policy()

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["CANCELLATION_001"])
    def test_cancel_booking_driving_range(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, cancellation_flow: CancellationFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        self._open_cancel_booking(cancellation_flow)
        cancellation_flow.continue_cancel()
        cancellation_flow.verify_confirmation_bottom_sheet()
        cancellation_flow.confirm_cancellation()
        cancellation_flow.verify_cancellation_success(D.BOOKING_CODE, D.VENUE, D.REFUND)
        cancellation_flow.see_booking_details()
        cancellation_flow.verify_booking_details_after_cancellation(D.BOOKING_CODE, D.STATUS_AFTER)

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["CANCELLATION_002"])
    def test_cancel_booking_tee_time(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, cancellation_flow: CancellationFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        self._open_cancel_booking(cancellation_flow)
        cancellation_flow.continue_cancel()
        cancellation_flow.verify_confirmation_bottom_sheet()
        cancellation_flow.confirm_cancellation()
        cancellation_flow.verify_cancellation_success(D.BOOKING_CODE, D.VENUE, D.REFUND)
        cancellation_flow.see_booking_details()
        cancellation_flow.verify_booking_details_after_cancellation(D.BOOKING_CODE, D.STATUS_AFTER)

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["CANCELLATION_003"])
    def test_verify_cancellation_policy(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, cancellation_flow: CancellationFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        self._open_cancel_booking(cancellation_flow)

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["CANCELLATION_004"])
    def test_go_back_from_cancel_booking_sheet(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, cancellation_flow: CancellationFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        self._open_cancel_booking(cancellation_flow)
        cancellation_flow.continue_cancel()
        cancellation_flow.verify_confirmation_bottom_sheet()
        cancellation_flow.go_back_from_confirmation()
