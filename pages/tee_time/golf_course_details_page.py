from locators.tee_time.golf_course_details_locators import GolfCourseDetailsLocators as L
from pages.base_page import BasePage


class GolfCourseDetailsPage(BasePage):
    ROOT_LOCATOR = L.EL_HEADER
    PAGE_NAME = "GolfCourseDetailsPage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_HEADER, timeout=20), "Golf course details screen not shown"
        assert self.is_visible(L.BTN_BACK, timeout=5), "Golf course details back button not shown"
        assert self.is_visible(L.TXT_SELECT_TEE_TIME, timeout=5), "Golf course details tee time section not shown"
        assert self.is_visible(L.BTN_BOOK_TEE_TIME, timeout=5), "Golf course details book tee time button not shown"
        self.capture_step("golf_course_details")
        return self

    def verify_all_sections(self):
        self.verify_screen()
        assert self.is_visible(L.IMG_HERO, timeout=10), "Golf course hero image not shown"
        assert self.is_visible(L.TXT_VENUE_LOCATION, timeout=5), "Golf course location not shown"
        assert self.is_visible(L.TXT_DISTANCE, timeout=5), "Golf course distance not shown"
        assert self.visible_count(L.LIST_PROMOS) > 0, "Golf course promo section not shown"
        assert self.is_visible(L.BTN_SEE_ALL_PROMOS, timeout=5), "Golf course see all promos not shown"
        assert self.is_visible(L.EL_CASHBACK_BANNER, timeout=5), "Golf course cashback banner not shown"
        assert self.is_visible(L.BTN_CALENDAR, timeout=5), "Golf course calendar button not shown"
        assert self.visible_count(L.LIST_DATE_STRIP) > 0, "Golf course date strip not shown"
        self.capture_step("Verify golf course details overview")
        assert self.visible_count(L.LIST_SESSION_TABS) > 0, "Golf course session tabs not shown"
        assert self.is_visible(L.IMG_SESSION_TAB_SELECTED, timeout=5), "Golf course selected session tab not shown"
        assert self.is_visible(L.TXT_SELECT_TEE_TIME, timeout=5), "Golf course tee time title not shown"
        assert self.is_visible(L.BTN_BOOK_TEE_TIME, timeout=5), "Golf course book tee time button not shown"
        self.capture_step("Verify golf course details schedule")
        self.scroll_to(L.BTN_VIEW_ON_MAPS)
        assert self.is_visible(L.TXT_LOCATION_TITLE, timeout=5), "Golf course location section not shown"
        assert self.is_visible(L.TXT_DISTANCE_FROM_LOCATION, timeout=5), "Golf course distance from location not shown"
        assert self.is_visible(L.BTN_VIEW_ON_MAPS, timeout=5), "Golf course Google Maps button not shown"
        self.capture_step("Verify golf course details location")
        self.scroll_to(L.TXT_MORE_INFORMATION)
        assert self.is_visible(L.TXT_MORE_INFORMATION, timeout=5), "Golf course more information not shown"
        self.capture_step("Verify golf course details more information")
        return self

    def scroll_to_location(self):
        self.capture_step("Scroll to location")
        self.scroll_to(L.BTN_VIEW_ON_MAPS)

    def scroll_to_more_information(self):
        self.capture_step("Scroll to more information")
        self.scroll_to(L.TXT_MORE_INFORMATION)

    def swipe_to_date(self, label):
        self.capture_step("Swipe to date", label)
        self.swipe_left_to_element(L.TXT_DATE_BY_LABEL.format(label), L.EL_DATE_STRIP)

    def swipe_to_promo(self, name):
        self.capture_step("Swipe to promo", name)
        self.swipe_left_to_element(L.IMG_PROMO_BY_NAME.format(name), L.EL_PROMO_STRIP)

    def open_featured_promos(self):
        self.capture_step("open_featured_promos")
        self.click(L.BTN_SEE_ALL_PROMOS)

    def open_calendar(self):
        self.capture_step("open_calendar")
        self.click(L.BTN_CALENDAR)

    def select_date(self, label):
        self.capture_step("select_date")
        self.click(L.TXT_DATE_BY_LABEL.format(label))

    def select_session(self, name):
        if name:
            self.capture_step("select_session")
            self.click(L.IMG_SESSION_TAB_BY_NAME.format(name))

    def select_slot(self, time):
        self.capture_step("select_slot")
        self.scroll_and_click(L.EL_SLOT_BY_TIME.format(time))

    def scroll_to_slot(self, time):
        self.capture_step("scroll_to_slot")
        self.scroll_to(L.EL_SLOT_BY_TIME.format(time))

    def open_maps(self):
        self.capture_step("open_maps")
        self.scroll_and_click(L.BTN_VIEW_ON_MAPS)

    def show_more_information(self):
        self.capture_step("show_more_information")
        self.scroll_and_click(L.BTN_SHOW_MORE)

    def tap_book_tee_time(self):
        self.capture_step("tap_book_tee_time")
        self.click(L.BTN_BOOK_TEE_TIME)

    def tap_back(self):
        self.capture_step("tap_back")
        self.click(L.BTN_BACK)

    def venue_name_text(self, name):
        return self.label_of(L.TXT_VENUE_NAME.format(name))

    def distance_text(self):
        return self.label_of(L.TXT_DISTANCE)

    def promo_text(self, name):
        return self.label_of(L.IMG_PROMO_BY_NAME.format(name))

    def slot_text(self, time):
        return self.label_of(L.EL_SLOT_BY_TIME.format(time))

    def slot_discount_text(self, time):
        return self.label_of(L.TXT_DISCOUNT_BY_SLOT.format(time))

    def promo_items(self):
        return self.texts_of(L.LIST_PROMOS)

    def date_items(self):
        return self.texts_of(L.LIST_DATE_STRIP)

    def session_items(self):
        return self.texts_of(L.LIST_SESSION_TABS)

    def selected_session_text(self):
        return self.label_of(L.IMG_SESSION_TAB_SELECTED)

    def slot_discount_items(self):
        return self.texts_of(L.LIST_SLOT_DISCOUNTS)

    def book_tee_time_is_enabled(self):
        return self.is_enabled(L.BTN_BOOK_TEE_TIME)

    def slot_count(self):
        return self.count(L.LIST_SLOTS)

    def unavailable_slot_count(self):
        return self.count(L.LIST_UNAVAILABLE_SLOTS)

    def spec_text(self, label):
        return self.value_after_label(L.TXT_SPEC_BY_LABEL.format(label))

    def address_text(self, text):
        return self.label_of(L.TXT_ADDRESS_BY_TEXT.format(text))

    def cashback_badge_text(self):
        return self.label_of(L.IMG_CASHBACK_BADGE)

    def has_slot(self, time, timeout=5):
        return self.is_visible(L.EL_SLOT_BY_TIME.format(time), timeout)

    def has_inclusion(self, name, timeout=5):
        return self.is_visible(L.EL_INCLUSION_BY_NAME.format(name), timeout)

    def has_facility(self, name, timeout=5):
        return self.is_visible(L.IMG_FACILITY_BY_NAME.format(name), timeout)
    
    def verify_exclusive_swing_pass_promo(self, player_type: str):
        match player_type:
            case "swing-player":
                assert self.is_visible(L.BTN_PROMO_ACTIVE), "Not Found"
            case "regular-player":
                assert self.is_visible(L.BTN_PROMO_JOIN), "Not Found"
            case "expired-player":
                assert self.is_visible(L.BTN_PROMO_RENEW), "Not Found"
            case _:
                print("Nothing Comes")
        
        return self
