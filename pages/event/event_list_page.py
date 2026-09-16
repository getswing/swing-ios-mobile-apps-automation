from locators.event.event_list_locators import EventListLocators as L
from pages.base_page import BasePage


class EventListPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "EventListPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Event list screen not shown"
        assert self.is_visible(L.IMG_SWING_PASS_FILTER, timeout=5), "Event list Swing Pass filter not shown"
        assert self.is_visible(L.BTN_BACK, timeout=5), "Event list back button not shown"
        self.capture_step("event_list")
        return self

    def toggle_swing_pass_filter(self):
        self.capture_step("toggle_swing_pass_filter")
        self.click(L.SWITCH_SWING_PASS_FILTER)

    def scroll_to_swing_pass_filter(self):
        self.capture_step("scroll_to_swing_pass_filter")
        self.scroll_to(L.IMG_SWING_PASS_FILTER, "up")

    def enable_swing_pass_filter(self):
        self.capture_step("enable_swing_pass_filter")
        self.set_switch(L.SWITCH_SWING_PASS_FILTER, True)

    def disable_swing_pass_filter(self):
        self.capture_step("disable_swing_pass_filter")
        self.set_switch(L.SWITCH_SWING_PASS_FILTER, False)

    def open_card(self, text):
        self.capture_step("open_card")
        self.click(L.EL_CARD_BY_TEXT.format(text))

    def scroll_to_card(self, text):
        self.capture_step("scroll_to_card")
        self.scroll_to(L.EL_CARD_BY_TEXT.format(text))

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def title_text(self):
        return self.label_of(L.TXT_TITLE)

    def card_text(self, text):
        return self.label_of(L.EL_CARD_BY_TEXT.format(text))

    def card_count(self):
        return self.count(L.LIST_CARDS)

    def card_items(self):
        return self.texts_of(L.LIST_CARDS)

    def has_card(self, text, timeout=5):
        return self.is_visible(L.EL_CARD_BY_TEXT.format(text), timeout)

    def swing_pass_filter_is_on(self):
        return self.is_selected(L.SWITCH_SWING_PASS_FILTER)
