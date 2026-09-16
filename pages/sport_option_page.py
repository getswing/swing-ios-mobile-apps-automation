from locators.sport_option_locators import SportOptionLocators as L
from pages.base_page import BasePage


class SportOptionPage(BasePage):
    ROOT_LOCATOR = L.EL_TITLE
    PAGE_NAME = "SportOptionPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_TITLE, timeout=20), "Sport option screen not shown"
        assert self.is_visible(L.LIST_SPORTS, timeout=5), "Sport list not shown"
        assert self.is_visible(L.CELL_GOLF, timeout=5), "Golf sport card not shown"
        self.capture_step("Verify sport option page")
        return self

    def title_text(self):
        return self.label_of(L.EL_TITLE)

    def select_sport(self, sport):
        self.capture_step("select_sport")
        self.click(L.CELL_SPORT.format(sport))

    def select_sport_by_label(self, label):
        self.capture_step("Select sport", label)
        self.click(L.CELL_SPORT_BY_LABEL.format(label))

    def select_golf(self):
        self.capture_step("select_golf")
        self.click(L.CELL_GOLF)

    def select_billiard(self):
        self.capture_step("select_billiard")
        self.click(L.CELL_BILLIARD)

    def select_padel(self):
        self.capture_step("select_padel")
        self.click(L.CELL_PADEL)

    def has_sport(self, sport, timeout=5):
        return self.is_visible(L.CELL_SPORT.format(sport), timeout)

    def scroll_to_sport(self, sport):
        self.capture_step("scroll_to_sport")
        self.scroll_to(L.CELL_SPORT.format(sport))

    def sport_items(self):
        return self.texts_of(L.LIST_SPORT_CARDS)

    def sport_count(self):
        return self.count(L.LIST_SPORT_CARDS)

    def badge_of_sport(self, sport):
        return self.text_of(L.TXT_BADGE_FOR_SPORT.format(sport))

    def coming_soon_count(self):
        return self.count(L.TXT_COMING_SOON)

    def has_beta(self, timeout=5):
        return self.is_visible(L.TXT_BETA, timeout)
