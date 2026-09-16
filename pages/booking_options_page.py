from locators.booking_options_locators import BookingOptionsLocators as L
from pages.base_page import BasePage


class BookingOptionsPage(BasePage):
    ROOT_LOCATOR = L.IMG_RESCHEDULE
    PAGE_NAME = "BookingOptionsPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.IMG_RESCHEDULE, timeout=20), "Booking options sheet not shown"
        assert self.is_visible(L.IMG_CANCEL, timeout=5), "Cancel booking option not shown"
        assert self.is_visible(L.IMG_CONTACT_SUPPORT, timeout=5), "Contact support option not shown"
        self.capture_step("booking_options")
        return self

    def tap_reschedule(self):
        self.capture_step("tap_reschedule")
        self.click(L.IMG_RESCHEDULE)

    def tap_cancel(self):
        self.capture_step("tap_cancel")
        self.click(L.IMG_CANCEL)

    def tap_contact_support(self):
        self.capture_step("tap_contact_support")
        self.click(L.IMG_CONTACT_SUPPORT)

    def tap_option(self, name):
        self.capture_step("tap_option")
        self.click(L.IMG_OPTION.format(name))

    def has_option(self, name, timeout=5):
        return self.is_visible(L.IMG_OPTION.format(name), timeout)

    def tap_unlabeled(self):
        self.capture_step("tap_unlabeled")
        self.click(L.BTN_UNLABELED)

    def is_shown(self, timeout=5):
        return self.is_visible(L.IMG_RESCHEDULE, timeout)

    def dismiss(self):
        self.capture_step("dismiss")
        self.click(L.TXT_SCRIM)
