from locators.tee_time.add_ons_locators import AddOnsLocators as L
from pages.base_page import BasePage


class AddOnsPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "AddOnsPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Add-ons sheet not shown"
        assert self.is_visible(L.TXT_FOR_PLAYER, timeout=5), "Add-ons player name not shown"
        assert self.is_visible(L.BTN_SAVE, timeout=5), "Add-ons save button not shown"
        assert self.is_visible(L.BTN_CANCEL, timeout=5), "Add-ons cancel button not shown"
        self.capture_step("add_ons")
        return self

    def add_item(self, name):
        self.capture_step("add_item")
        self.click(L.BTN_INCREASE_BY_ITEM.format(name))

    def remove_item(self, name):
        self.capture_step("remove_item")
        self.click(L.BTN_DECREASE_BY_ITEM.format(name))

    def tap_save(self):
        self.capture_step("tap_save")
        self.click(L.BTN_SAVE)

    def tap_cancel(self):
        self.capture_step("tap_cancel")
        self.click(L.BTN_CANCEL)

    def for_player_text(self):
        return self.label_of(L.TXT_FOR_PLAYER)

    def item_text(self, name):
        return self.label_of(L.EL_ITEM_BY_NAME.format(name))

    def item_count(self):
        return self.count(L.LIST_ITEMS)

    def save_button_text(self):
        return self.label_of(L.BTN_SAVE)

    def has_item(self, name, timeout=5):
        return self.is_visible(L.EL_ITEM_BY_NAME.format(name), timeout)

    def save_is_enabled(self):
        return self.is_enabled(L.BTN_SAVE)
