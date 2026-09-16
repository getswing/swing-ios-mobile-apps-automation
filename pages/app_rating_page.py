from locators.app_rating_locators import AppRatingLocators as L
from pages.base_page import BasePage


class AppRatingPage(BasePage):
    ROOT_LOCATOR = L.TXT_TITLE
    PAGE_NAME = "AppRatingPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "App rating prompt not shown"
        assert self.is_visible(L.BTN_NOT_NOW, timeout=5), "Not Now button not shown"
        self.capture_step("app_rating")
        return self

    def tap_star(self, index):
        self.capture_step("tap_star")
        self.click(L.BTN_STAR_BY_INDEX.format(index))

    def star_count(self):
        return self.count(L.LIST_STARS)

    def tap_not_now(self):
        self.capture_step("tap_not_now")
        self.click(L.BTN_NOT_NOW)

    def is_shown(self, timeout=3):
        return self.is_visible(L.BTN_NOT_NOW, timeout)
