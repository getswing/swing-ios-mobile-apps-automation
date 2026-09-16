from locators.reschedule_details_locators import RescheduleDetailsLocators as L
from pages.base_page import BasePage


class RescheduleDetailsPage(BasePage):
    ROOT_LOCATOR = L.EL_TITLE
    PAGE_NAME = "RescheduleDetailsPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_TITLE, timeout=20), "Reschedule details screen not shown"
        assert self.is_visible(L.TXT_VENUE, timeout=5), "Reschedule details venue not shown"
        assert self.is_visible(L.TXT_REASON_TITLE, timeout=5), "Reschedule reason section not shown"
        self.capture_step("reschedule_details")
        return self

    def venue_text(self):
        return self.text_of(L.TXT_VENUE)

    def booking_id_text(self):
        return self.text_of(L.TXT_BOOKING_ID)

    def field_text(self, name):
        return self.text_of(L.TXT_FIELD.format(name))

    def date_change_text(self):
        return self.label_of(L.IMG_DATE_CHANGE)

    def scroll_to_field(self, name):
        self.capture_step("scroll_to_field")
        self.scroll_to(L.TXT_FIELD.format(name))

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)
