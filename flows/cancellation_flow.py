from flows.base_flow import BaseFlow
from pages.activity.activity_page import ActivityPage
from pages.booking_details_page import BookingDetailsPage
from pages.booking_options_page import BookingOptionsPage
from pages.cancel_booking_dialog_page import CancelBookingDialogPage
from pages.cancellation_success_page import CancellationSuccessPage
from pages.change_booking_page import ChangeBookingPage
from pages.homepage.home_page import HomePage


class CancellationFlow(BaseFlow):
    FLOW_NAME = "CancellationFlow"

    def __init__(self, driver, reporter=None):
        super().__init__(driver, reporter)
        self.home = self.page(HomePage)
        self.activity = self.page(ActivityPage)
        self.booking = self.page(BookingDetailsPage)
        self.options = self.page(BookingOptionsPage)
        self.change = self.page(ChangeBookingPage)
        self.dialog = self.page(CancelBookingDialogPage)
        self.success = self.page(CancellationSuccessPage)

    def verify_home(self):
        self.home.verify_screen()

    def open_activity(self):
        self.home.open_activity_tab()
        self.activity.verify_screen()

    def choose_activity_filter(self, name):
        self.activity.open_category_tab(name)

    def find_activity_card(self, text):
        self.activity.scroll_to_booking(text)

    def open_activity_card(self, text):
        self.activity.open_booking(text)
        self.booking.verify_screen()

    def verify_booking_details(self, booking_code, status=""):
        self.booking.verify_screen()
        assert booking_code in self.booking.booking_id_text(), (f"booking id text does not contain booking code: expected {booking_code}, found {self.booking.booking_id_text()}")
        if status:
            assert self.booking.has_status(status), f"booking status {status} not shown"

    def open_booking_options(self):
        self.booking.tap_more()
        self.options.verify_screen()

    def choose_cancel_booking(self):
        self.options.tap_cancel()
        self.change.verify_screen()

    def verify_cancellation_policy(self):
        self.change.open_cancellation_tab()
        assert self.change.has_cancellation_policy(), "Cancellation policy not shown"
        assert self.change.policy_rules(), "Cancellation policy rules not shown"

    def continue_cancel(self):
        self.change.tap_continue_cancel()
        self.dialog.verify_screen()

    def verify_confirmation_bottom_sheet(self):
        self.dialog.verify_screen()

    def confirm_cancellation(self):
        self.dialog.tap_confirm()
        self.success.verify_screen()

    def go_back_from_confirmation(self):
        self.dialog.tap_go_back()
        self.change.verify_screen()

    def verify_cancellation_success(self, booking_code="", venue="", refund=""):
        self.success.verify_screen()
        if booking_code:
            assert booking_code in self.success.booking_id_text(), (f"booking id text does not contain booking code: expected {booking_code}, found {self.success.booking_id_text()}")
        if venue:
            assert venue in self.success.venue_text(), (f"venue text does not contain venue: expected {venue}, found {self.success.venue_text()}")
        if refund:
            assert refund in self.success.refund_text(), (f"refund text does not contain refund: expected {refund}, found {self.success.refund_text()}")

    def see_booking_details(self):
        self.success.tap_see_booking_details()
        self.booking.verify_screen()

    def finish_cancellation(self):
        self.success.tap_finish()

    def verify_booking_details_after_cancellation(self, booking_code, status="CANCELLED"):
        self.booking.verify_screen()
        assert booking_code in self.booking.booking_id_text(), (f"booking id text does not contain booking code: expected {booking_code}, found {self.booking.booking_id_text()}")
        assert self.booking.has_status(status), f"booking status {status} not shown"

    def cancel_booking(self, card, booking_code, status_before="UPCOMING"):
        self.open_activity_card(card)
        self.verify_booking_details(booking_code, status_before)
        self.open_booking_options()
        self.choose_cancel_booking()
        self.verify_cancellation_policy()
        self.continue_cancel()
        self.confirm_cancellation()
