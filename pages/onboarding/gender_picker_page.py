from locators.onboarding.gender_picker_locators import GenderPickerLocators as L
from pages.base_page import BasePage


class GenderPickerPage(BasePage):
    ROOT_LOCATOR = L.TXT_NOT_SPECIFIED
    PAGE_NAME = "GenderPickerPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_NOT_SPECIFIED, timeout=20), "Gender picker screen not shown"
        assert self.is_visible(L.TXT_MALE, timeout=5), "Gender picker male option not shown"
        assert self.is_visible(L.TXT_FEMALE, timeout=5), "Gender picker female option not shown"
        assert self.is_visible(L.BTN_CONFIRM, timeout=5), "Gender picker confirm button not shown"
        self.capture_step("Verify gender picker page")
        return self

    def select_gender(self, gender):
        self.capture_step("Select gender", gender)
        self.click(L.TXT_OPTION_BY_NAME.format(gender))

    def select_male(self):
        self.capture_step("select_male")
        self.click(L.TXT_MALE)

    def select_female(self):
        self.capture_step("select_female")
        self.click(L.TXT_FEMALE)

    def select_not_specified(self):
        self.capture_step("select_not_specified")
        self.click(L.TXT_NOT_SPECIFIED)

    def tap_confirm(self):
        self.capture_step("Tap confirm")
        self.click(L.BTN_CONFIRM)

    def dismiss(self):
        self.capture_step("dismiss")
        self.click(L.TXT_SCRIM)

    def has_gender(self, gender, timeout=5):
        return self.is_visible(L.TXT_OPTION_BY_NAME.format(gender), timeout)
