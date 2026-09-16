from locators.coachmark_locators import CoachmarkLocators as L
from pages.base_page import BasePage


class CoachmarkPage(BasePage):
    ROOT_LOCATOR = L.BTN_GOT_IT
    PAGE_NAME = "CoachmarkPage"

    SEQUENCE = [
        (L.TXT_TITLE_SPORT_MODE, L.TXT_DESCRIPTION),
        (L.TXT_TITLE_COUNTRIES, L.TXT_DESCRIPTION),
    ]

    def title_text(self):
        return self.text_of(L.TXT_TITLE_SPORT_MODE)

    def description_text(self):
        return self.text_of(L.TXT_DESCRIPTION)

    def has_title(self, title, timeout=5):
        return self.is_visible(L.TXT_TITLE.format(title), timeout)

    def tap_got_it(self):
        self.capture_step("Tap Got It")
        self.click(L.BTN_GOT_IT)

    def is_shown(self, timeout=3):
        return self.is_visible(L.BTN_GOT_IT, timeout)
    
    def verify_sequence(self, sequence: list | None = None):
        self.capture_step("Verify sequence", sequence)
        for title, body in (sequence or self.SEQUENCE):
            assert self.is_visible(title), "Not Shown Title"
            assert self.is_visible(body), "Not Shown Body"
            self.tap_got_it()
    
            
