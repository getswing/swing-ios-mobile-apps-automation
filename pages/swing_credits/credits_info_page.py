from locators.swing_credits.credits_info_locators import CreditsInfoLocators as L
from pages.base_page import BasePage


class CreditsInfoPage(BasePage):
    ROOT_LOCATOR = L.EL_HEADER
    PAGE_NAME = "CreditsInfoPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_HEADER, timeout=20), "Credits info screen not shown"
        assert self.is_visible(L.IMG_BENEFIT_ENDLESS_CASHBACKS, timeout=5), "Credits info benefit cards not shown"
        assert self.is_visible(L.TXT_FAQ_TITLE, timeout=5), "Credits info FAQ section not shown"
        self.capture_step("credits_info")
        return self

    def open_faq(self, question):
        self.capture_step("open_faq")
        self.scroll_and_click(L.IMG_FAQ_BY_QUESTION.format(question))

    def scroll_to_faq(self, question):
        self.capture_step("scroll_to_faq")
        self.scroll_to(L.IMG_FAQ_BY_QUESTION.format(question))

    def tap_contact_us(self):
        self.capture_step("tap_contact_us")
        self.scroll_and_click(L.BTN_CONTACT_US)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def benefit_text(self, title):
        return self.label_of(L.IMG_BENEFIT_BY_TITLE.format(title))

    def faq_text(self, question):
        return self.label_of(L.IMG_FAQ_BY_QUESTION.format(question))

    def has_benefit(self, title, timeout=5):
        return self.is_visible(L.IMG_BENEFIT_BY_TITLE.format(title), timeout)

    def has_faq(self, question, timeout=5):
        return self.is_visible(L.IMG_FAQ_BY_QUESTION.format(question), timeout)
