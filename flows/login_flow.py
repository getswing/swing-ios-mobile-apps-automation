from flows.base_flow import BaseFlow
from pages.country_picker_page import CountryPickerPage
from pages.login_page import LoginPage
from pages.verification_method_page import VerificationMethodPage
from pages.verification_code_page import VerificationCodePage

import pycountry
import phonenumbers


class LoginFlow(BaseFlow):
    FLOW_NAME = "LoginFlow"

    def __init__(self, driver, reporter=None):
        super().__init__(driver, reporter)
        self.login = self.page(LoginPage)
        self.country = self.page(CountryPickerPage)
        self.verification_method = self.page(VerificationMethodPage)
        self.verification_code = self.page(VerificationCodePage)

    def open_login(self):
        self.login.verify_screen()

    def open_country_picker(self):
        self.login.select_country()
        self.country.verify_screen()

    def choose_country(self, country: str):
        self.open_country_picker()
        self.country.enter_search(country)
        self.country.select_country_containing(country)
        self.login.verify_screen()

    def enter_phone_number(self, phone_number: str):
        self.login.enter_phone_number(phone_number)
    
    def continue_log_in(self):
        self.login.tap_continue()
    
    def choose_verification_method(self, method: str):
        if method == "whatsapp":
            self.verification_method.select_whatsapp()
        elif method == "sms":
            self.verification_method.select_sms()
        
    def verify_bottom_sheet_verification_method(self):
        assert self.verification_method.verify_screen(), "Page is not showed"
    
    def enter_otp_code(self, otp: str,country: str, phone_number: str):
        country_code = pycountry.countries.get(name=country)
        if not country_code:
            country_code = pycountry.countries.search_fuzzy(country)[0]
        alpha2 = country_code.alpha_2
        dial_code = phonenumbers.country_code_for_region(alpha2)
        otp = self.login.resolve_otp_code(otp, phone_number, f"+{dial_code}")
        self.verification_code.enter_code(otp)

    def request_code(self, number=None):
        self.enter_phone_number(number)
        self.login.tap_continue()
        self.handle_system_alerts()
    
    def verify_button_continue_enable(self):
        assert self.login.continue_is_enabled(), "Disable"

    def verify_country_selected(self, country: str):
        country_code = pycountry.countries.get(name=country)
        if not country_code:
            country_code = pycountry.countries.search_fuzzy(country)[0]
        alpha2 = country_code.alpha_2
        dial_code = phonenumbers.country_code_for_region(alpha2)
        result = f"{alpha2} (+{dial_code})"
        assert self.login.selected_country() == result , "Not Same"
    
    def verify_page_code_otp(self):
        self.verification_code.verify_screen()
    
