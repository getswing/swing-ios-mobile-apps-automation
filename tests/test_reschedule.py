import pytest

from flows.home_flow import HomeFlow
from flows.login_flow import LoginFlow
from flows.reschedule_flow import RescheduleFlow
from helpers.pdf_report import init_pdf
from test_data.reschedule_test_data import RescheduleTestData as D


class TestReschedule:

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

    def _open_confirm_reschedule(self, reschedule_flow: RescheduleFlow):
        reschedule_flow.verify_home()
        reschedule_flow.open_activity()
        reschedule_flow.choose_activity_filter(D.ACTIVITY_FILTER)
        reschedule_flow.find_activity_card(D.ACTIVITY_CARD)
        reschedule_flow.open_activity_card(D.ACTIVITY_CARD)
        reschedule_flow.verify_booking_details(D.BOOKING_CODE, D.STATUS_BEFORE)
        reschedule_flow.open_booking_options()
        reschedule_flow.choose_reschedule_booking()
        reschedule_flow.verify_reschedule_page()
        reschedule_flow.open_calendar()
        reschedule_flow.choose_new_date(D.NEW_DATE)
        reschedule_flow.choose_new_time(D.NEW_TIME)
        reschedule_flow.confirm_new_date_time()
        reschedule_flow.verify_confirm_reschedule(D.PLAYER_NAME, D.BOOKING_CODE, D.DURATION,
                                                  D.BAY_TYPE, D.ORIGINAL_DATE_TIME, D.NEW_DATE_TIME)
        reschedule_flow.choose_reschedule_reason(D.REASON)

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["RESCHEDULE_001"])
    def test_reschedule_booking_driving_range(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, reschedule_flow: RescheduleFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        self._open_confirm_reschedule(reschedule_flow)
        reschedule_flow.confirm_reschedule_and_pay()
        reschedule_flow.verify_confirmation_bottom_sheet()
        reschedule_flow.confirm_reschedule()
        reschedule_flow.verify_reschedule_success(D.TOTAL_PAYMENT, D.PAYMENT_METHOD, D.BOOKING_CODE, D.VENUE)
        reschedule_flow.see_booking_details()
        reschedule_flow.verify_booking_details_after_reschedule(D.BOOKING_CODE, D.STATUS_AFTER,
                                                               D.NEW_DATE_TIME, D.NEW_TIME)

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["RESCHEDULE_002"])
    def test_reschedule_booking_tee_time(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, reschedule_flow: RescheduleFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        self._open_confirm_reschedule(reschedule_flow)
        reschedule_flow.confirm_reschedule_and_pay()
        reschedule_flow.verify_confirmation_bottom_sheet()
        reschedule_flow.confirm_reschedule()
        reschedule_flow.verify_reschedule_success(D.TOTAL_PAYMENT, D.PAYMENT_METHOD, D.BOOKING_CODE, D.VENUE)
        reschedule_flow.see_booking_details()
        reschedule_flow.verify_booking_details_after_reschedule(D.BOOKING_CODE, D.STATUS_AFTER,
                                                               D.NEW_DATE_TIME, D.NEW_TIME)

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["RESCHEDULE_003"])
    def test_go_back_from_confirm_reschedule_sheet(self, TC_ID, login_flow: LoginFlow, home_flow: HomeFlow, reschedule_flow: RescheduleFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login(login_flow, home_flow)
        self._open_confirm_reschedule(reschedule_flow)
        reschedule_flow.confirm_reschedule_and_pay()
        reschedule_flow.verify_confirmation_bottom_sheet()
        reschedule_flow.go_back_from_confirmation()
