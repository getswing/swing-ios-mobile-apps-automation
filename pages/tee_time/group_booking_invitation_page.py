from locators.tee_time.group_booking_invitation_locators import GroupBookingInvitationLocators as L
from pages.base_page import BasePage


class GroupBookingInvitationPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "GroupBookingInvitationPage"
    INVITATION_TIMEOUT = 90

    def verify_screen(self):
        self.wait_until_loaded(self.INVITATION_TIMEOUT)
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Group booking invitation sheet not shown"
        assert self.is_visible(L.TXT_MESSAGE, timeout=5), "Group booking invitation message not shown"
        assert self.is_visible(L.BTN_ACCEPT, timeout=5), "Accept invitation button not shown"
        assert self.is_visible(L.BTN_DECLINE, timeout=5), "Decline invitation button not shown"
        self.capture_step("group_booking_invitation")
        return self

    def tap_accept(self):
        self.capture_step("tap_accept_invitation")
        self.click(L.BTN_ACCEPT)

    def tap_decline(self):
        self.capture_step("tap_decline_invitation")
        self.click(L.BTN_DECLINE)

    def message_text(self):
        return self.label_of(L.TXT_MESSAGE)

    def has_sheet(self, timeout=3):
        return self.is_visible(L.TXT_TITLE, timeout)
