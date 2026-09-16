import pytest

from helpers.pdf_report import init_pdf
from test_data.login_test_data import LoginTestData as D
from flows.home_flow import HomeFlow
from flows.login_flow import LoginFlow


class TestLogin:

    @pytest.mark.app_reset("clear")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["LOGIN_001"])
    def test_login_screen_shows_phone_form(self, TC_ID, login_flow: LoginFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        login_flow.open_login()

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["LOGIN_002"])
    def test_select_country_from_picker(self, TC_ID, login_flow: LoginFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        login_flow.open_login()
        login_flow.choose_country(D.COUNTRY_NAME)
        login_flow.verify_country_selected(D.COUNTRY_NAME)

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["LOGIN_003"])
    def test_continue_enabled_after_phone_number(self, TC_ID, login_flow: LoginFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        login_flow.open_login()
        login_flow.choose_country(D.COUNTRY_NAME)
        login_flow.enter_phone_number(D.PHONE_NUMBER)
        login_flow.verify_button_continue_enable()
        
        
    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["LOGIN_004"])
    def test_verify_select_method_verification(self, TC_ID, login_flow: LoginFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        login_flow.open_login()
        login_flow.choose_country(D.COUNTRY_NAME)
        login_flow.enter_phone_number(D.PHONE_NUMBER)
        login_flow.continue_log_in()
        login_flow.choose_verification_method(D.METHOD_VERIFICATION)
        
    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["LOGIN_005"])
    def test_verify_enter_otp(self, TC_ID, login_flow: LoginFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        login_flow.open_login()
        login_flow.choose_country(D.COUNTRY_NAME)
        login_flow.enter_phone_number(D.PHONE_NUMBER)
        login_flow.continue_log_in()
        login_flow.choose_verification_method(D.METHOD_VERIFICATION)
        login_flow.verify_page_code_otp()
        
    @pytest.mark.app_reset("clear")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["LOGIN_006"])
    def test_verify_home_page_after_enter_otp(self, TC_ID , login_flow: LoginFlow, home_flow: HomeFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        login_flow.open_login()
        login_flow.choose_country(D.COUNTRY_NAME)
        login_flow.enter_phone_number(D.PHONE_NUMBER)
        login_flow.continue_log_in()
        login_flow.choose_verification_method(D.METHOD_VERIFICATION)
        login_flow.verify_page_code_otp()
        login_flow.enter_otp_code(D.OTP, D.COUNTRY_NAME, D.PHONE_NUMBER)
        home_flow.verify_sport_option_page()
        home_flow.select_sport(D.SPORT_TYPE)
        home_flow.enable_notifications()
        home_flow.enable_location()
        home_flow.dismiss_coachmark()
        home_flow.close_whats_new()
        home_flow.verify_home()
    
