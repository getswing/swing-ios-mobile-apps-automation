from helpers import amounts
from locators.swing_credits.swing_credits_locators import SwingCreditsLocators as L
from pages.base_page import BasePage


class SwingCreditsPage(BasePage):
    ROOT_LOCATOR = L.EL_HEADER
    PAGE_NAME = "SwingCreditsPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_HEADER, timeout=20), "Swing Credits screen not shown"
        assert self.is_visible(L.TXT_BALANCE, timeout=5), "Swing Credits balance not shown"
        assert self.is_visible(L.BTN_REDEEM, timeout=5), "Swing Credits redeem button not shown"
        assert self.is_visible(L.BTN_SEE_HISTORY, timeout=5), "Swing Credits see history button not shown"
        self.capture_step("Verify swing credits page")
        return self

    def open_redeem(self):
        self.capture_step("open_redeem")
        self.click(L.BTN_REDEEM)

    def open_scan_to_earn(self):
        self.capture_step("open_scan_to_earn")
        self.click(L.BTN_SCAN_TO_EARN)

    def toggle_auto_apply(self):
        self.capture_step("toggle_auto_apply")
        self.click(L.SWITCH_AUTO_APPLY)

    def open_cashbacks(self):
        self.capture_step("open_cashbacks")
        self.click(L.BTN_SEE_ALL_CASHBACKS)

    def open_learn_more(self):
        self.capture_step("open_learn_more")
        self.click(L.BTN_LEARN_MORE)

    def open_history(self):
        self.capture_step("Open history")
        self.click(L.BTN_SEE_HISTORY)

    def select_category(self, name):
        self.capture_step("select_category")
        self.click(L.TXT_CATEGORY_BY_NAME.format(name))

    def enter_reward_search(self, text):
        self.capture_step("enter_reward_search")
        self.type(L.INPUT_REWARD_SEARCH, text)

    def open_reward(self, title):
        self.capture_step("open_reward")
        self.scroll_and_click(L.EL_REWARD_BY_TITLE.format(title))

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def balance_text(self):
        return self.label_of(L.TXT_BALANCE)

    def balance(self):
        return amounts.to_number(self.balance_text())

    def auto_apply_is_on(self):
        return self.is_selected(L.SWITCH_AUTO_APPLY)

    def reward_count(self):
        return self.count(L.LIST_REWARDS)

    def category_count(self):
        return self.count(L.LIST_CATEGORY_CHIPS)

    def has_reward(self, title, timeout=5):
        return self.is_visible(L.EL_REWARD_BY_TITLE.format(title), timeout)
