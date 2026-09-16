from locators.tee_time.credits_earnings_locators import TeeTimeCreditsEarningsLocators as L
from pages.base_page import BasePage


class TeeTimeCreditsEarningsPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "TeeTimeCreditsEarningsPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Swing Credits earnings sheet not shown"
        assert self.is_visible(L.BTN_GOT_IT, timeout=5), "Swing Credits earnings got it button not shown"
        assert self.visible_count(L.LIST_EARNINGS) > 0, "Swing Credits earnings rows not shown"
        self.capture_step("Verify Swing Credits earnings sheet")
        return self

    def tap_got_it(self):
        self.capture_step("Tap got it")
        self.click(L.BTN_GOT_IT)

    def dismiss(self):
        self.capture_step("Dismiss credits earnings")
        self.click(L.TXT_SCRIM)

    def title_text(self):
        return self.label_of(L.TXT_TITLE)

    def earning_text(self, player):
        return self.label_of(L.EL_EARNING_BY_PLAYER.format(player, player))

    def earning_items(self):
        return self.texts_of(L.LIST_EARNINGS)

    def earning_count(self):
        return self.count(L.LIST_EARNINGS)

    def has_earning(self, player, timeout=5):
        return self.is_visible(L.EL_EARNING_BY_PLAYER.format(player, player), timeout)
