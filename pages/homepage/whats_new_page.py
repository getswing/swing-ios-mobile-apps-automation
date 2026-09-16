from locators.whats_new_locators import WhatsNewLocators as L
from pages.base_page import BasePage


class WhatsNewPage(BasePage):
    ROOT_LOCATOR = L.EL_TITLE
    PAGE_NAME = "WhatsNewPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_TITLE, timeout=20), "What's new screen not shown"
        assert self.is_visible(L.TXT_HEADLINE, timeout=5), "What's new headline not shown"
        assert self.is_visible(L.BTN_PRIMARY_ACTION, timeout=5), "What's new primary action not shown"
        self.capture_step("whats_new")
        return self

    def title_text(self):
        return self.label_of(L.EL_TITLE)

    def headline_text(self):
        return self.text_of(L.TXT_HEADLINE)

    def has_section(self, title, timeout=5):
        return self.is_visible(L.TXT_SECTION.format(title), timeout)

    def scroll_to_section(self, title):
        self.capture_step("scroll_to_section")
        self.scroll_to(L.TXT_SECTION.format(title))

    def tap_primary_action(self):
        self.capture_step("tap_primary_action")
        self.click(L.BTN_PRIMARY_ACTION)

    def tap_button(self, name):
        self.capture_step("tap_button")
        self.click(L.BTN_BY_NAME.format(name))

    def scroll_to_feedback(self):
        self.capture_step("scroll_to_feedback")
        self.scroll_to(L.BTN_FEEDBACK)

    def tap_feedback(self):
        self.capture_step("tap_feedback")
        self.click(L.BTN_FEEDBACK)

    def tap_back(self):
        self.capture_step("Tap back")
        self.click(L.BTN_BACK)
