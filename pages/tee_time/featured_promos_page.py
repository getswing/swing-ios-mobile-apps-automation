from locators.tee_time.featured_promos_locators import TeeTimeFeaturedPromosLocators as L
from pages.base_page import BasePage


class TeeTimeFeaturedPromosPage(BasePage):
    ROOT_LOCATOR = L.EL_HEADER
    PAGE_NAME = "TeeTimeFeaturedPromosPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_HEADER, timeout=20), "Tee time featured promos screen not shown"
        assert self.is_visible(L.IMG_AUTO_CLAIM_NOTICE, timeout=5), "Tee time featured promos auto claim notice not shown"
        assert self.is_visible(L.BTN_BACK, timeout=5), "Tee time featured promos back button not shown"
        self.capture_step("tee_time_featured_promos")
        return self

    def open_promo(self, name):
        self.capture_step("open_promo")
        self.scroll_and_click(L.IMG_PROMO_BY_NAME.format(name))

    def scroll_to_promo(self, name):
        self.capture_step("scroll_to_promo")
        self.scroll_to(L.IMG_PROMO_BY_NAME.format(name))

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def auto_claim_text(self):
        return self.label_of(L.IMG_AUTO_CLAIM_NOTICE)

    def promo_text(self, name):
        return self.label_of(L.IMG_PROMO_BY_NAME.format(name))

    def quota_text(self, name):
        return self.label_of(L.TXT_QUOTA_BY_PROMO.format(name))

    def promo_items(self):
        return self.texts_of(L.LIST_PROMOS)

    def promo_count(self):
        return self.count(L.LIST_PROMOS)

    def has_promo(self, name, timeout=5):
        return self.is_visible(L.IMG_PROMO_BY_NAME.format(name), timeout)
