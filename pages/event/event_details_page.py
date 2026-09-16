from locators.event.event_details_locators import EventDetailsLocators as L
from pages.base_page import BasePage


class EventDetailsPage(BasePage):
    ROOT_LOCATOR = L.EL_HEADER
    PAGE_NAME = "EventDetailsPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_HEADER, timeout=20), "Event details screen not shown"
        assert self.is_visible(L.BTN_BACK, timeout=5), "Event details back button not shown"
        assert self.is_visible(L.EL_CASHBACK_BANNER, timeout=5), "Event details cashback banner not shown"
        assert self.is_visible(L.BTN_SECURE_SLOT, timeout=5), "Event details secure your slot button not shown"
        self.capture_step("event_details")
        return self

    def open_leaderboard(self):
        self.capture_step("open_leaderboard")
        self.click(L.EL_LEADERBOARD_BANNER)

    def scroll_to_registration_fee(self):
        self.capture_step("scroll_to_registration_fee")
        self.scroll_to(L.TXT_LABEL_BY_NAME.format("Registration fee"))

    def tap_secure_slot(self):
        self.capture_step("tap_secure_slot")
        self.click(L.BTN_SECURE_SLOT)

    def tap_share(self):
        self.capture_step("tap_share")
        self.click(L.BTN_SHARE)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def event_name_text(self, name):
        return self.label_of(L.TXT_EVENT_NAME.format(name))

    def location_text(self):
        return self.label_of(L.EL_LOCATION)

    def cashback_text(self):
        return self.label_of(L.EL_CASHBACK_BANNER)

    def venue_text(self):
        return self.label_of(L.TXT_VENUE_VALUE)

    def date_text(self):
        return self.label_of(L.TXT_DATE_VALUE)

    def starting_time_text(self):
        return self.label_of(L.TXT_STARTING_TIME_VALUE)

    def deadline_text(self):
        return self.label_of(L.TXT_DEADLINE_VALUE)

    def registration_fee_text(self):
        return self.label_of(L.TXT_REGISTRATION_FEE_VALUE)

    def value_of_label(self, label):
        return self.label_of(L.TXT_VALUE_BY_LABEL.format(label))

    def has_leaderboard_banner(self, timeout=5):
        return self.is_visible(L.EL_LEADERBOARD_BANNER, timeout)

    def secure_slot_is_enabled(self):
        return self.is_enabled(L.BTN_SECURE_SLOT)
