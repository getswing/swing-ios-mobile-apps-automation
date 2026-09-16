from locators.event.player_details_locators import PlayerDetailsLocators as L
from pages.base_page import BasePage


class PlayerDetailsPage(BasePage):
    ROOT_LOCATOR = L.EL_TITLE
    PAGE_NAME = "PlayerDetailsPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_TITLE, timeout=20), "Player details sheet not shown"
        assert self.is_visible(L.BTN_CHANGE_PLAYER, timeout=5), "Player details change player button not shown"
        assert self.is_visible(L.BTN_SAVE_PLAYER_DETAILS, timeout=5), "Player details save button not shown"
        self.capture_step("player_details")
        return self

    def select_option(self, name):
        self.capture_step("select_option")
        self.scroll_and_click(L.BTN_OPTION_BY_NAME.format(name))

    def open_birthday_picker(self):
        self.capture_step("open_birthday_picker")
        self.scroll_and_click(L.EL_QUESTION_BIRTHDAY)

    def download_template(self):
        self.capture_step("download_template")
        self.scroll_and_click(L.BTN_DOWNLOAD_TEMPLATE)

    def upload_file(self):
        self.capture_step("upload_file")
        self.scroll_and_click(L.BTN_UPLOAD_FILE)

    def scroll_to_question(self, text):
        self.capture_step("scroll_to_question")
        self.scroll_to(L.EL_QUESTION_BY_TEXT.format(text))

    def change_player(self):
        self.capture_step("change_player")
        self.click(L.BTN_CHANGE_PLAYER)

    def remove_player(self):
        self.capture_step("remove_player")
        self.click(L.BTN_REMOVE_PLAYER)

    def tap_save(self):
        self.capture_step("tap_save")
        self.click(L.BTN_SAVE_PLAYER_DETAILS)

    def tap_close(self):
        self.capture_step("tap_close")
        self.click(L.BTN_CLOSE)

    def player_name_text(self, name):
        return self.label_of(L.TXT_PLAYER_NAME.format(name))

    def account_type_text(self):
        return self.label_of(L.TXT_ACCOUNT_TYPE)

    def birthday_value(self):
        return self.value_of(L.EL_QUESTION_BIRTHDAY)

    def has_question(self, text, timeout=5):
        return self.is_visible(L.EL_QUESTION_BY_TEXT.format(text), timeout)

    def has_option(self, name, timeout=5):
        return self.is_visible(L.EL_OPTION_BY_NAME.format(name), timeout)

    def option_is_selected(self, name):
        return self.is_selected(L.BTN_OPTION_BY_NAME.format(name))

    def has_hcp_upload(self, timeout=5):
        return self.is_visible(L.IMG_HCP_FILE, timeout)

    def save_is_enabled(self):
        return self.is_enabled(L.BTN_SAVE_PLAYER_DETAILS)
