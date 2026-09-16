from flows.base_flow import BaseFlow
from pages.activity.activity_page import ActivityPage
from pages.booking_details_page import BookingDetailsPage
from pages.booking_options_page import BookingOptionsPage
from pages.confirm_reschedule_dialog_page import ConfirmRescheduleDialogPage
from pages.confirm_reschedule_page import ConfirmReschedulePage
from pages.homepage.home_page import HomePage
from pages.reschedule_booking_page import RescheduleBookingPage
from pages.reschedule_success_page import RescheduleSuccessPage


class RescheduleFlow(BaseFlow):
    FLOW_NAME = "RescheduleFlow"

    def __init__(self, driver, reporter=None):
        super().__init__(driver, reporter)
        self.home = self.page(HomePage)
        self.activity = self.page(ActivityPage)
        self.booking = self.page(BookingDetailsPage)
        self.options = self.page(BookingOptionsPage)
        self.reschedule = self.page(RescheduleBookingPage)
        self.confirm = self.page(ConfirmReschedulePage)
        self.dialog = self.page(ConfirmRescheduleDialogPage)
        self.success = self.page(RescheduleSuccessPage)

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

    def choose_reschedule_booking(self):
        self.options.tap_reschedule()
        self.reschedule.verify_screen()

    def verify_reschedule_page(self):
        self.reschedule.verify_screen()

    def continue_reschedule(self):
        self.reschedule.tap_confirm_datetime()

    def open_calendar(self):
        self.reschedule.open_calendar()

    def choose_new_date(self, day):
        self.reschedule.select_day(day)

    def choose_new_time(self, time_slot):
        self.reschedule.scroll_to_time(time_slot)
        self.reschedule.select_time(time_slot)

    def confirm_new_date_time(self):
        self.reschedule.tap_confirm_datetime()
        self.confirm.verify_screen()

    def verify_confirm_reschedule(self, player_name, booking_code, duration, bay_type,
                                  original_date_time, new_date_time):
        self.confirm.verify_screen()
        date_change = self.confirm.date_change_text()
        assert player_name in self.confirm.field_text(player_name), (f"field text(player name) does not contain player name: expected {player_name}, found {self.confirm.field_text(player_name)}")
        assert booking_code in self.confirm.field_text(booking_code), (f"field text(booking code) does not contain booking code: expected {booking_code}, found {self.confirm.field_text(booking_code)}")
        assert duration in self.confirm.field_text(duration), (f"field text(duration) does not contain duration: expected {duration}, found {self.confirm.field_text(duration)}")
        if bay_type:
            assert bay_type in self.confirm.field_text(bay_type), (f"field text(bay type) does not contain bay type: expected {bay_type}, found {self.confirm.field_text(bay_type)}")
        assert original_date_time in date_change, f"original date and time not shown: {date_change}"
        assert new_date_time in date_change, f"new date and time not shown: {date_change}"

    def choose_reschedule_reason(self, reason):
        self.confirm.scroll_to_reason(reason)
        self.confirm.select_reason(reason)

    def confirm_reschedule_and_pay(self):
        self.confirm.scroll_to_payment_details()
        self.confirm.tap_confirm_and_pay()
        self.dialog.verify_screen()

    def verify_confirmation_bottom_sheet(self):
        self.dialog.verify_screen()

    def confirm_reschedule(self):
        self.dialog.tap_confirm()
        self.success.verify_screen()

    def go_back_from_confirmation(self):
        self.dialog.tap_go_back()
        self.confirm.verify_screen()

    def verify_reschedule_success(self, total_payment, payment_method, booking_code="", venue=""):
        self.success.verify_screen()
        assert total_payment in self.success.field_text(total_payment), (f"field text(total payment) does not contain total payment: expected {total_payment}, found {self.success.field_text(total_payment)}")
        assert payment_method in self.success.field_text(payment_method), (f"field text(payment method) does not contain payment method: expected {payment_method}, found {self.success.field_text(payment_method)}")
        if booking_code:
            assert booking_code in self.success.booking_id_text(), (f"booking id text does not contain booking code: expected {booking_code}, found {self.success.booking_id_text()}") # type: ignore
        if venue:
            assert venue in self.success.venue_text(), (f"venue text does not contain venue: expected {venue}, found {self.success.venue_text()}") # type: ignore

    def see_booking_details(self):
        self.success.tap_see_booking_details()
        self.booking.verify_screen()

    def finish_reschedule(self):
        self.success.tap_finish()

    def verify_booking_details_after_reschedule(self, booking_code, status, new_date, new_time):
        self.booking.verify_screen()
        assert booking_code in self.booking.booking_id_text(), (f"booking id text does not contain booking code: expected {booking_code}, found {self.booking.booking_id_text()}")
        assert self.booking.has_status(status), f"booking status {status} not shown"
        assert new_date in self.booking.field_text(new_date), (f"field text(new date) does not contain new date: expected {new_date}, found {self.booking.field_text(new_date)}")
        assert new_time in self.booking.field_text(new_time), (f"field text(new time) does not contain new time: expected {new_time}, found {self.booking.field_text(new_time)}")
