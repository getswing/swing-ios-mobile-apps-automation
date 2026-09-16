from locators.onboarding.complete_profile_locators import CompleteProfileLocators as L
from pages.base_page import BasePage


class CompleteProfilePage(BasePage):
    ROOT_LOCATOR = L.TXT_WELCOME
    PAGE_NAME = "CompleteProfilePage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_WELCOME, timeout=20), "Complete profile screen not shown"
        assert self.is_visible(L.INPUT_FIRST_NAME, timeout=5), "Complete profile first name field not shown"
        assert self.is_visible(L.EL_BIRTHDAY, timeout=5), "Complete profile birthday field not shown"
        assert self.is_visible(L.BTN_NEXT, timeout=5), "Complete profile next button not shown"
        self.capture_step("Verify complete profile page")
        return self

    def enter_first_name(self, text):
        self.capture_step("Enter first name", text)
        self.type(L.INPUT_FIRST_NAME, text, hide_keyboard=True, dismiss_with=L.TXT_WELCOME)

    def enter_last_name(self, text):
        self.capture_step("Enter last name", text)
        self.type(L.INPUT_LAST_NAME, text, hide_keyboard=True, dismiss_with=L.TXT_WELCOME)

    def enter_username(self, text):
        self.capture_step("Enter username", text)
        self.type(L.INPUT_USERNAME, text, hide_keyboard=True, dismiss_with=L.TXT_WELCOME)

    def enter_email(self, text):
        self.capture_step("Enter email", text)
        self.type(L.INPUT_EMAIL, text, hide_keyboard=True, dismiss_with=L.TXT_WELCOME)

    def enter_referral_code(self, text):
        self.capture_step("Enter referral code", text)
        self.type(L.INPUT_REFERRAL_CODE, text, hide_keyboard=True, dismiss_with=L.TXT_WELCOME)

    def open_birthday(self):
        self.capture_step("Open birthday")
        self.click(L.EL_BIRTHDAY)

    def open_nationality(self):
        self.capture_step("Open nationality")
        self.click(L.EL_NATIONALITY)

    def open_gender(self):
        self.capture_step("Open gender")
        self.click(L.EL_GENDER)

    def open_field(self, name):
        self.capture_step("open_field")
        self.click(L.EL_FIELD_BY_NAME.format(name))

    def scroll_to_referral_code(self):
        self.capture_step("Scroll to referral code")
        self.scroll_to(L.INPUT_REFERRAL_CODE)

    def tap_next(self):
        self.capture_step("Tap next")
        self.click(L.BTN_NEXT)

    def first_name_value(self):
        return self.value_of(L.INPUT_FIRST_NAME)

    def last_name_value(self):
        return self.value_of(L.INPUT_LAST_NAME)

    def username_value(self):
        return self.value_of(L.INPUT_USERNAME)

    def email_value(self):
        return self.value_of(L.INPUT_EMAIL)

    def birthday_text(self):
        return self.label_of(L.EL_BIRTHDAY)

    def nationality_text(self):
        return self.label_of(L.EL_NATIONALITY)

    def gender_text(self):
        return self.label_of(L.EL_GENDER)

    def next_is_enabled(self):
        return self.is_enabled(L.BTN_NEXT)
