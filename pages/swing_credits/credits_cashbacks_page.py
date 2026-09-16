from locators.swing_credits.credits_cashbacks_locators import CreditsCashbacksLocators as L
from pages.base_page import BasePage


class CreditsCashbacksPage(BasePage):
    ROOT_LOCATOR = L.EL_HEADER
    PAGE_NAME = "CreditsCashbacksPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_HEADER, timeout=20), "Credits cashbacks screen not shown"
        assert self.is_visible(L.EL_SEARCH, timeout=5), "Credits cashbacks search field not shown"
        assert self.is_visible(L.TXT_COLUMN_REGULAR, timeout=5), "Credits cashbacks regular column not shown"
        assert self.is_visible(L.TXT_COLUMN_SWING_PASS, timeout=5), "Credits cashbacks Swing Pass column not shown"
        self.capture_step("credits_cashbacks")
        return self

    def enter_search(self, text):
        self.capture_step("enter_search")
        self.type(L.INPUT_SEARCH, text)

    def select_tab(self, name):
        self.capture_step("select_tab")
        self.click(L.IMG_TAB_BY_NAME.format(name))

    def scroll_to_venue(self, name):
        self.capture_step("scroll_to_venue")
        self.scroll_to(L.TXT_VENUE_BY_NAME.format(name))

    def open_venue(self, name):
        self.capture_step("open_venue")
        self.scroll_and_click(L.TXT_VENUE_BY_NAME.format(name))

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def has_venue(self, name, timeout=5):
        return self.is_visible(L.TXT_VENUE_BY_NAME.format(name), timeout)

    def has_rate(self, rate, timeout=5):
        return self.is_visible(L.TXT_CASHBACK_RATE.format(rate), timeout)

    def cashback_row_count(self):
        return self.count(L.LIST_CASHBACK_LABELS)
