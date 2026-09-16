from flows.base_flow import BaseFlow
from pages.homepage.home_page import HomePage
from pages.event.event_list_page import EventListPage
from pages.event.event_details_page import EventDetailsPage
from pages.event.registration_method_page import RegistrationMethodPage
from pages.event.registration_confirmation_page import RegistrationConfirmationPage
from pages.event.player_details_page import PlayerDetailsPage
from pages.event.add_player_page import EventAddPlayerPage
from pages.country_picker_page import CountryPickerPage
from pages.event.group_registration_info_page import GroupRegistrationInfoPage
from pages.driving_range.payment_method_page import PaymentMethodPage
from pages.driving_range.payment_gateway_page import PaymentGatewayPage
from pages.event.registration_success_page import RegistrationSuccessPage
from pages.event.registration_details_page import RegistrationDetailsPage
from pages.event.registration_summary_page import RegistrationSummaryPage


class EventFlow(BaseFlow):
    FLOW_NAME = "EventFlow"

    def __init__(self, driver, reporter=None):
        super().__init__(driver, reporter)
        self.home = self.page(HomePage)
        self.list = self.page(EventListPage)
        self.details = self.page(EventDetailsPage)
        self.method = self.page(RegistrationMethodPage)
        self.confirm = self.page(RegistrationConfirmationPage)
        self.player_form = self.page(PlayerDetailsPage)
        self.player = self.page(EventAddPlayerPage)
        self.country = self.page(CountryPickerPage)
        self.group_info = self.page(GroupRegistrationInfoPage)
        self.payment = self.page(PaymentMethodPage)
        self.gateway = self.page(PaymentGatewayPage)
        self.success = self.page(RegistrationSuccessPage)
        self.registration = self.page(RegistrationDetailsPage)
        self.summary = self.page(RegistrationSummaryPage)

    def open_events(self):
        self.home.open_events()
        self.list.verify_screen()

    def only_swing_pass_partners(self):
        self.list.scroll_to_swing_pass_filter()
        self.list.enable_swing_pass_filter()
        self.list.verify_screen()

    def all_partners(self):
        self.list.scroll_to_swing_pass_filter()
        self.list.disable_swing_pass_filter()
        self.list.verify_screen()

    def find_event(self, text):
        self.list.scroll_to_card(text)

    def open_event(self, text):
        self.list.open_card(text)
        self.details.verify_screen()

    def see_event_information(self):
        self.details.scroll_to_registration_fee()

    def secure_slot(self):
        self.details.tap_secure_slot()
        self.method.verify_screen()

    def choose_standard_registration(self):
        self.method.choose_standard_registration()
        self.confirm.verify_screen()

    def choose_group_registration(self):
        self.method.choose_group_registration()
        self.confirm.verify_screen()

    def open_registration_method(self):
        self.confirm.open_registration_method()
        self.method.verify_screen()

    def switch_to_group_registration(self):
        self.group_info.switch_to_group_registration()
        self.confirm.verify_screen()

    def close_group_registration_info(self):
        self.group_info.tap_close()
        self.confirm.verify_screen()

    def open_player_details(self, player):
        self.confirm.open_player_details(player)
        self.player_form.verify_screen()

    def answer_question(self, option):
        self.player_form.select_option(option)

    def find_question(self, text):
        self.player_form.scroll_to_question(text)

    def download_hcp_template(self):
        self.player_form.download_template()

    def upload_hcp_file(self):
        self.player_form.upload_file()

    def save_player_details(self):
        self.player_form.tap_save()
        self.confirm.verify_screen()

    def use_swing_credits(self):
        self.confirm.toggle_swing_credits()

    def enter_note(self, text):
        self.confirm.enter_note(text)

    def add_player(self):
        self.confirm.add_player()
        self.player.verify_screen()

    def search_friend(self, name):
        self.player.search_friend(name)

    def select_friend(self, username):
        self.player.select_friend(username)
        self.confirm.verify_screen()

    def open_add_manually(self):
        self.player.open_add_manually_tab()

    def fill_player(self, first_name, last_name, phone_number):
        self.player.enter_first_name(first_name)
        self.player.enter_last_name(last_name)
        self.player.enter_phone_number(phone_number)

    def enter_player_email(self, email):
        self.player.enter_email(email)

    def open_player_country_picker(self):
        self.player.open_country_picker()
        self.country.verify_screen()

    def choose_player_country(self, name):
        self.country.select_country(name)
        self.player.verify_screen()

    def save_player(self):
        self.player.tap_save_player()
        self.confirm.verify_screen()

    def remove_player(self, player):
        self.confirm.remove_player(player)

    def select_flight(self, name):
        self.confirm.select_flight(name)

    def let_organizer_arrange_flight(self):
        self.confirm.toggle_organizer_arrange()

    def open_payment_method(self):
        self.confirm.change_payment_method()
        self.payment.verify_screen()

    def choose_payment_method(self, name):
        self.payment.select_method(name)
        self.confirm.verify_screen()

    def verify_registration_confirmation(self):
        self.confirm.verify_screen()

    def pay_now(self):
        self.confirm.tap_pay_now()

    def proceed_to_pay(self):
        self.gateway.verify_screen()
        self.gateway.tap_proceed_to_pay()

    def verify_registration_success(self):
        self.success.verify_screen()

    def finish(self):
        self.success.tap_finish()

    def open_registration_details(self):
        self.success.open_registration_details()
        self.registration.verify_screen()

    def open_complete_breakdown(self):
        self.registration.open_breakdown()
        self.summary.verify_screen()

    def back_to_registration_details(self):
        self.summary.tap_back()
        self.registration.verify_screen()
