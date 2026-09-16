from flows.base_flow import BaseFlow
from pages.onboarding.complete_profile_page import CompleteProfilePage
from pages.onboarding.birthday_picker_page import BirthdayPickerPage
from pages.onboarding.nationality_picker_page import NationalityPickerPage
from pages.onboarding.gender_picker_page import GenderPickerPage
from pages.onboarding.discovery_source_page import DiscoverySourcePage


class OnboardingFlow(BaseFlow):
    FLOW_NAME = "OnboardingFlow"

    def __init__(self, driver, reporter=None):
        super().__init__(driver, reporter)
        self.profile = self.page(CompleteProfilePage)
        self.birthday = self.page(BirthdayPickerPage)
        self.nationality = self.page(NationalityPickerPage)
        self.gender = self.page(GenderPickerPage)
        self.discovery = self.page(DiscoverySourcePage)

    def open_complete_profile(self):
        self.profile.verify_screen()

    def enter_name(self, first_name, last_name):
        self.profile.enter_first_name(first_name)
        self.profile.enter_last_name(last_name)

    def choose_birthday(self, month, day, year):
        self.profile.open_birthday()
        self.birthday.verify_screen()
        self.birthday.select_month(month)
        self.birthday.select_day(day)
        self.birthday.select_year(year)
        self.birthday.tap_confirm()
        self.profile.verify_screen()

    def choose_nationality(self, country):
        self.profile.open_nationality()
        self.nationality.verify_screen()
        self.nationality.enter_search(country)
        self.nationality.select_country(country)
        self.profile.verify_screen()

    def choose_gender(self, gender):
        self.profile.open_gender()
        self.gender.verify_screen()
        self.gender.select_gender(gender)

    def enter_account(self, username, email):
        self.profile.enter_username(username)
        self.profile.enter_email(email)

    def enter_referral_code(self, code):
        self.profile.scroll_to_referral_code()
        self.profile.enter_referral_code(code)

    def continue_to_discovery(self):
        self.profile.tap_next()
        self.discovery.verify_screen()

    def choose_discovery_source(self, source):
        self.discovery.select_source(source)

    def finish(self):
        self.discovery.tap_finish()
