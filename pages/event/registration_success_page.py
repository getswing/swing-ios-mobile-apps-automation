from locators.event.registration_success_locators import RegistrationSuccessLocators as L
from pages.base_page import BasePage


class RegistrationSuccessPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "RegistrationSuccessPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Registration success screen not shown"
        assert self.is_visible(L.TXT_SUBTITLE, timeout=5), "Registration success subtitle not shown"
        assert self.is_visible(L.TXT_REGISTRATION_CODE, timeout=5), "Registration code not shown"
        assert self.is_visible(L.BTN_SEE_REGISTRATION_DETAILS, timeout=5), "See registration details button not shown"
        self.capture_step("registration_success")
        return self

    def open_registration_details(self):
        self.capture_step("open_registration_details")
        self.click(L.BTN_SEE_REGISTRATION_DETAILS)

    def tap_finish(self):
        self.capture_step("tap_finish")
        self.click(L.BTN_FINISH)

    def title_text(self):
        return self.label_of(L.TXT_TITLE)

    def event_name_text(self, name):
        return self.label_of(L.TXT_EVENT_NAME.format(name))

    def registration_code_text(self):
        return self.label_of(L.TXT_REGISTRATION_CODE)

    def value_of_label(self, label):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format(label))

    def date_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Date"))

    def starting_time_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Starting time"))

    def venue_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Venue"))

    def players_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Players"))

    def total_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Total"))

    def payment_method_text(self):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format("Payment method"))

    def earned_credits_text(self):
        return self.label_of(L.EL_EARNED_CREDITS)

    def has_earned_credits(self, timeout=5):
        return self.is_visible(L.EL_EARNED_CREDITS, timeout)
