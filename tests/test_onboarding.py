import pytest

from helpers.pdf_report import init_pdf
from test_data.onboarding_test_data import OnboardingTestData as D
from flows.home_flow import HomeFlow
from flows.login_flow import LoginFlow
from flows.onboarding_flow import OnboardingFlow
from flows.swing_credit_flow import SwingCreditFlow


class TestOnboarding:
    
    def _login_before_onboarding(self, login_flow: LoginFlow):
        login_flow.open_login()
        login_flow.choose_country(D.COUNTRY_NAME)
        login_flow.enter_phone_number(D.PHONE_NUMBER)
        login_flow.continue_log_in()
        login_flow.choose_verification_method(D.METHOD_VERIFICATION)
        login_flow.verify_page_code_otp()
        login_flow.enter_otp_code(D.OTP, D.COUNTRY_NAME, D.PHONE_NUMBER)
    
    def _fill_information_onboarding_user(self, onboarding_flow: OnboardingFlow):
        onboarding_flow.open_complete_profile()
        onboarding_flow.enter_name(D.FIRST_NAME, D.LAST_NAME)
        onboarding_flow.choose_birthday(D.BIRTH_MONTH, D.BIRTH_DAY, D.BIRTH_YEAR)
        onboarding_flow.choose_nationality(D.NATIONALITY)
        onboarding_flow.choose_gender(D.GENDER)
        onboarding_flow.enter_account(D.USERNAME, D.EMAIL)
    
    @pytest.mark.app_reset("clear")
    @pytest.mark.skip
    @pytest.mark.parametrize("TC_ID", ["ONBOARDING_001"])
    def test_verify_page_onboarding(self,TC_ID, login_flow: LoginFlow, onboarding_flow: OnboardingFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login_before_onboarding(login_flow)
        onboarding_flow.open_complete_profile()
    
    
    @pytest.mark.app_reset("clear")
    @pytest.mark.skip
    @pytest.mark.parametrize("TC_ID", ["ONBOARDING_002"])
    def test_onboarding_new_account_without_referreal_code(self, TC_ID, login_flow: LoginFlow, onboarding_flow: OnboardingFlow, home_flow: HomeFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login_before_onboarding(login_flow)
        self._fill_information_onboarding_user(onboarding_flow)
        onboarding_flow.continue_to_discovery()
        onboarding_flow.choose_discovery_source(D.DISCOVERY_SOURCE)
        onboarding_flow.finish()
        home_flow.verify_sport_option_page()
        home_flow.select_sport(D.SPORT_TYPE)
        home_flow.enable_notifications()
        home_flow.enable_location()
        home_flow.dismiss_coachmark()
        home_flow.close_whats_new()
        home_flow.verify_home()

    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["ONBOARDING_003"])
    def test_onboarding_new_account_with_referral_code(self, TC_ID, login_flow: LoginFlow, onboarding_flow: OnboardingFlow, home_flow: HomeFlow, swing_credit_flow: SwingCreditFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        self._login_before_onboarding(login_flow)
        self._fill_information_onboarding_user(onboarding_flow)
        onboarding_flow.enter_referral_code(D.REFERRAL_CODE)
        onboarding_flow.continue_to_discovery()
        onboarding_flow.choose_discovery_source(D.DISCOVERY_SOURCE)
        onboarding_flow.finish()
        home_flow.verify_sport_option_page()
        home_flow.select_sport(D.SPORT_TYPE)
        home_flow.enable_notifications()
        home_flow.enable_location()
        home_flow.dismiss_coachmark()
        home_flow.close_whats_new()
        home_flow.verify_home()
        swing_credit_flow.open_swing_credits()
        swing_credit_flow.open_history()
        swing_credit_flow.verify_referral_credit_booking_code()
        
