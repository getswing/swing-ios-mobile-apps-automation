import calendar

from flows.base_flow import BaseFlow
from helpers.checks import CheckTable
from pages.event.player_details_page import PlayerDetailsPage
from pages.event.registration_confirmation_page import RegistrationConfirmationPage
from pages.onboarding.birthday_picker_page import BirthdayPickerPage


class PlayerDetailsFlow(BaseFlow):
    FLOW_NAME = "PlayerDetailsFlow"

    def __init__(self, driver, reporter=None):
        super().__init__(driver, reporter)
        self.confirm = self.page(RegistrationConfirmationPage)
        self.form = self.page(PlayerDetailsPage)
        self.picker = self.page(BirthdayPickerPage)

    # ----------------------------- actions -----------------------------

    def open_player_details(self, player):
        self.confirm.open_player_details(player)
        self.form.verify_screen()

    def find_question(self, question):
        self.form.scroll_to_question(question)

    def select_option(self, option):
        self.form.select_option(option)

    def open_birthday_picker(self):
        self.form.open_birthday_picker()
        self.picker.verify_screen()

    def choose_birthday(self, day, month, year):
        self.picker.select_month(month)
        self.picker.select_day(day)
        self.picker.select_year(year)
        self.picker.tap_confirm()
        self.form.verify_screen()

    def set_birthday(self, value):
        day, month, year = str(value).split("/")
        self.open_birthday_picker()
        self.choose_birthday(str(int(day)), calendar.month_name[int(month)], year)

    def download_template(self):
        self.form.download_template()

    def upload_file(self):
        self.form.upload_file()

    def close_player_details(self):
        self.form.tap_close()
        self.confirm.verify_screen()

    def save_player_details(self):
        self.form.tap_save()
        self.confirm.verify_screen()

    def answer_question(self, answer):
        self.find_question(answer["question"])
        answer_type = str(answer.get("answer_type") or "option").lower()
        if answer_type == "option":
            self.select_option(answer["answer"])
        elif answer_type == "date":
            self.set_birthday(answer["answer"])
        elif answer_type == "file":
            self.upload_file()

    def answer_questions(self, answers):
        for answer in answers or []:
            self.answer_question(answer)

    def fill_player_details(self, player, answers):
        self.step(f"fill in details for {player}")
        self.open_player_details(player)
        self.answer_questions(answers)
        self.save_player_details()

    def fill_players_details(self, players, details):
        for player in self.player_names(players):
            if details.get(player):
                self.fill_player_details(player, details[player])

    # --------------------------- verifications ---------------------------

    def answer_found(self, answer):
        answer_type = str(answer.get("answer_type") or "option").lower()
        if answer_type == "option":
            return "selected" if self.form.option_is_selected(answer["answer"]) else "not selected"
        if answer_type == "date":
            return self.form.birthday_value()
        return "filled" if self.form.has_hcp_upload() else "not filled"

    def answer_expected(self, answer):
        answer_type = str(answer.get("answer_type") or "option").lower()
        if answer_type == "option":
            return "selected"
        if answer_type == "date":
            return answer["answer"]
        return "filled"

    def verify_questions_shown(self, answers):
        table = CheckTable("Fill in details - questions")
        for answer in answers or []:
            self.find_question(answer["question"])
            table.truthy(answer["question"], self.form.has_question(answer["question"]))
            if str(answer.get("answer_type") or "option").lower() == "option":
                table.truthy(f"{answer['question']} - {answer['answer']}",
                             self.form.has_option(answer["answer"]))
        table.verify()

    def verify_answers(self, player, answers):
        table = CheckTable(f"Fill in details - {player}")
        for answer in answers or []:
            self.find_question(answer["question"])
            expected = self.answer_expected(answer)
            found = self.answer_found(answer)
            table.add(f"{answer['question']} - {answer['answer']}", expected, found, expected == found)
        table.verify()

    def verify_player_details(self, player, answers):
        self.open_player_details(player)
        self.verify_answers(player, answers)
        self.close_player_details()

    def verify_players_details(self, players, details):
        for player in self.player_names(players):
            if details.get(player):
                self.verify_player_details(player, details[player])

    def verify_save_is_disabled(self):
        table = CheckTable("Fill in details - save button")
        enabled = self.form.save_is_enabled()
        table.add("Save player details", "disabled", "enabled" if enabled else "disabled", not enabled)
        table.verify()

    def verify_save_is_enabled(self):
        table = CheckTable("Fill in details - save button")
        table.truthy("Save player details enabled", self.form.save_is_enabled())
        table.verify()
