from helpers import amounts
from locators.swing_credits.credits_history_locators import CreditsHistoryLocators as L
from pages.base_page import BasePage


class CreditsHistoryPage(BasePage):
    ROOT_LOCATOR = L.EL_HEADER
    PAGE_NAME = "CreditsHistoryPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_HEADER, timeout=20), "Credits history screen not shown"
        assert self.is_visible(L.TXT_TAB_ALL, timeout=5), "Credits history all tab not shown"
        assert self.is_visible(L.TXT_TAB_EARNED, timeout=5), "Credits history earned tab not shown"
        assert self.is_visible(L.TXT_TAB_USAGE, timeout=5), "Credits history usage tab not shown"
        self.capture_step("Verify credits history page")
        return self

    def select_tab(self, name):
        self.capture_step("select_tab")
        self.click(L.TXT_TAB_BY_NAME.format(name))

    def open_all_tab(self):
        self.capture_step("Open all tab")
        self.click(L.TXT_TAB_ALL)

    def open_earned_tab(self):
        self.capture_step("Open earned tab")
        self.click(L.TXT_TAB_EARNED)

    def open_usage_tab(self):
        self.capture_step("Open usage tab")
        self.click(L.TXT_TAB_USAGE)

    def open_booking(self, code):
        self.capture_step("open_booking")
        self.click(L.EL_ITEM_BY_BOOKING_CODE.format(code))

    def scroll_to_booking(self, code):
        self.capture_step("scroll_to_booking")
        self.scroll_to(L.EL_ITEM_BY_BOOKING_CODE.format(amounts.booking_tag(code)))

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)
    
    def verify_credit_by_booking_code(self, booking_code: str):
        tag = amounts.booking_tag(booking_code)
        assert self.is_visible(L.LIST_ITEM_BY_BOOKING_CODE.format(tag)), (
            f"no swing credit row for {tag}, history shows {self.booking_codes()}")

    def scroll_to_booking_player(self, code, player):
        self.capture_step("Scroll to booking row", f"{amounts.booking_tag(code)} - {player}")
        self.scroll_to(L.EL_ITEM_BY_BOOKING_CODE_AND_PLAYER.format(amounts.booking_tag(code), player))

    def has_booking_for_player(self, code, player, timeout=5):
        return self.is_visible(
            L.EL_ITEM_BY_BOOKING_CODE_AND_PLAYER.format(amounts.booking_tag(code), player), timeout)

    def booking_label_for_player(self, code, player):
        return self.label_of(
            L.EL_ITEM_BY_BOOKING_CODE_AND_PLAYER.format(amounts.booking_tag(code), player))

    def booking_amount_text_for_player(self, code, player):
        return amounts.amount_text(self.booking_label_for_player(code, player))

    def booking_amount_number_for_player(self, code, player):
        return amounts.to_number(self.booking_label_for_player(code, player))

    def verify_credit_by_booking_code_player(self, booking_code, player):
        tag = amounts.booking_tag(booking_code)
        assert self.has_booking_for_player(booking_code, player), (
            f"no swing credit row for {tag} and {player}, history shows {self.item_labels()}")

    def verify_credit_by_referral_code(self):
        assert self.is_visible(L.LIST_ITEM_BY_BOOKING_CODE.format("Reward for using")), "Credit is not visibile"
    
    def item_labels(self):
        return self.texts_of(L.LIST_ITEMS)

    def earned_labels(self):
        return self.texts_of(L.LIST_EARNED_ITEMS)

    def used_labels(self):
        return self.texts_of(L.LIST_USED_ITEMS)

    def booking_label(self, code):
        return self.label_of(L.LIST_ITEM_BY_BOOKING_CODE.format(amounts.booking_tag(code)))

    def booking_credits(self, code):
        return amounts.to_number(self.booking_label(code))

    def booking_credits_referral(self):
        return amounts.to_number(self.booking_label("Reward for using"))

    def booking_direction(self, code):
        return amounts.direction(self.booking_label(code))

    def booking_amount_text(self, code):
        return amounts.amount_text(self.booking_label(code))

    def booking_amount_number(self, code):
        return amounts.to_number(self.booking_label(code))
    
    def booking_amount_text_referral(self):
        return amounts.amount_text(self.booking_label("Reward for using"))
    
    def booking_amount_number_referral(self):
        return amounts.to_number(self.booking_label("Reward for using"))

    def booking_codes(self):
        return [amounts.booking_code(label) for label in self.item_labels()]

    def total_credits(self):
        return amounts.total(self.item_labels())

    def total_earned(self):
        return amounts.total(self.earned_labels())

    def total_used(self):
        return amounts.total(self.used_labels())

    def has_booking(self, code, timeout=5):
        return self.is_visible(L.EL_ITEM_BY_BOOKING_CODE.format(code), timeout)

    def item_count(self):
        return self.count(L.LIST_ITEMS)

    def date_group_count(self):
        return self.count(L.LIST_DATE_GROUPS)

    def has_date_group(self, label, timeout=5):
        return self.is_visible(L.EL_DATE_GROUP_BY_LABEL.format(label), timeout)
