from locators.onboarding.discovery_source_locators import DiscoverySourceLocators as L
from pages.base_page import BasePage


class DiscoverySourcePage(BasePage):
    ROOT_LOCATOR = L.EL_TITLE
    PAGE_NAME = "DiscoverySourcePage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_TITLE, timeout=20), "Discovery source screen not shown"
        assert self.is_visible(L.IMG_SOCIAL_MEDIA, timeout=5), "Discovery source options not shown"
        assert self.is_visible(L.BTN_FINISH, timeout=5), "Discovery source finish button not shown"
        assert self.is_visible(L.BTN_PREVIOUS, timeout=5), "Discovery source previous button not shown"
        self.capture_step("Verify discovery source page")
        return self

    def select_source(self, name):
        self.capture_step("Select source", name)
        self.click(L.IMG_OPTION_BY_NAME.format(name))

    def select_social_media(self):
        self.capture_step("select_social_media")
        self.click(L.IMG_SOCIAL_MEDIA)

    def select_others(self):
        self.capture_step("select_others")
        self.click(L.IMG_OTHERS)

    def tap_finish(self):
        self.capture_step("Tap finish")
        self.click(L.BTN_FINISH)

    def tap_previous(self):
        self.capture_step("tap_previous")
        self.click(L.BTN_PREVIOUS)

    def title_text(self):
        return self.label_of(L.EL_TITLE)

    def has_source(self, name, timeout=5):
        return self.is_visible(L.IMG_OPTION_BY_NAME.format(name), timeout)

    def source_items(self):
        return self.texts_of(L.LIST_OPTIONS)

    def source_count(self):
        return self.count(L.LIST_OPTIONS)
