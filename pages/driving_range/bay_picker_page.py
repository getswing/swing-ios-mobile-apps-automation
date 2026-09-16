from locators.driving_range.bay_picker_locators import BayPickerLocators as L
from pages.base_page import BasePage


class BayPickerPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "BayPickerPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Bay picker screen not shown"
        assert self.is_visible(L.TXT_NUMBER_OF_BAYS, timeout=5), "Bay picker number of bays row not shown"
        assert self.is_visible(L.BTN_CONFIRM, timeout=5), "Bay picker confirm button not shown"
        self.capture_step("bay_picker")
        return self

    def increase_bays(self):
        self.capture_step("increase_bays")
        self.click(L.BTN_INCREASE)

    def decrease_bays(self):
        self.capture_step("decrease_bays")
        self.click(L.BTN_DECREASE)

    def set_bays(self, count):
        self.click_times(L.BTN_INCREASE, int(count) - 1)
        self.capture_step("Set bays", count)

    def add_bays(self, count):
        self.capture_step("add_bays", count)
        self.click_times(L.BTN_INCREASE, count)

    def remove_bays(self, count):
        self.capture_step("remove_bays", count)
        self.click_times(L.BTN_DECREASE, count)

    def tap_confirm(self):
        self.capture_step("Tap confirm")
        self.click(L.BTN_CONFIRM)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def dismiss(self):
        self.capture_step("dismiss")
        self.click(L.TXT_SCRIM)

    def bay_count_text(self):
        return self.label_of(L.TXT_BAY_COUNT)

    def increase_is_enabled(self):
        return self.is_enabled(L.BTN_INCREASE)

    def decrease_is_enabled(self):
        return self.is_enabled(L.BTN_DECREASE)

    def verify_maximum_bays(self, tot_bays: str):
        assert self.is_visible(L.TXT_MAXIMUM_BAYS.format(tot_bays)), "Not Found"
        assert self.is_disabled(L.BTN_INCREASE), ("self.is disabled(L.BTN INCREASE) is false")
        self.capture_step("Verify maximum bays", tot_bays)
