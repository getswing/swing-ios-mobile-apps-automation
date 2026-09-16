from locators.reschedule_success_locators import RescheduleSuccessLocators as L
from pages.base_page import BasePage


class RescheduleSuccessPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "RescheduleSuccessPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Reschedule success screen not shown"
        assert self.is_visible(L.TXT_BOOKING_ID, timeout=5), "Booking id not shown on success screen"
        assert self.is_visible(L.BTN_FINISH, timeout=5), "Finish button not shown"
        self.capture_step("reschedule_success")
        return self

    def title_text(self):
        return self.text_of(L.TXT_TITLE)

    def booking_id_text(self):
        return self.text_of(L.TXT_BOOKING_ID)

    def venue_text(self):
        return self.text_of(L.TXT_VENUE)

    def date_change_text(self):
        return self.label_of(L.IMG_DATE_CHANGE)

    def field_text(self, name):
        return self.text_of(L.TXT_FIELD.format(name))

    def tap_finish(self):
        self.capture_step("tap_finish")
        self.click(L.BTN_FINISH)

    def tap_see_booking_details(self):
        self.capture_step("tap_see_booking_details")
        self.click(L.BTN_SEE_BOOKING_DETAILS)
