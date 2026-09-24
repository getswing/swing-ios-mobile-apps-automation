from locators.event.select_package_locators import SelectPackageLocators as L
from pages.base_page import BasePage


class SelectPackagePage(BasePage):
    ROOT_LOCATOR = L.EL_HEADER
    PAGE_NAME = "SelectPackagePage"

    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.EL_HEADER, timeout=20), "Select package screen not shown"
        assert self.is_visible(L.BTN_BACK, timeout=5), "Select package back button not shown"
        assert self.is_visible(L.EL_PLAYER_COUNT, timeout=5), "Select package player count not shown"
        assert self.is_visible(L.BTN_CONFIRM_PACKAGES, timeout=5), "Select package confirm button not shown"
        self.capture_step("select_package")
        return self

    def scroll_to_package(self, name):
        self.capture_step("Scroll to package", name)
        self.scroll_to(L.EL_PACKAGE_BY_NAME.format(name))

    def increase_package(self, name):
        self.capture_step("Increase package", name)
        self.click(L.BTN_INCREASE_BY_PACKAGE.format(name))

    def decrease_package(self, name):
        self.capture_step("Decrease package", name)
        self.click(L.BTN_DECREASE_BY_PACKAGE.format(name))

    def set_package_quantity(self, name, quantity):
        self.capture_step("Set package quantity", f"{name} = {quantity}")
        self.step_to(quantity, self.package_quantity(name),
                     L.BTN_INCREASE_BY_PACKAGE.format(name), L.BTN_DECREASE_BY_PACKAGE.format(name))

    def set_packages(self, packages):
        self.capture_step("Set packages", packages)
        self.set_quantities(packages, L.EL_PACKAGE_BY_NAME, L.BTN_INCREASE_BY_PACKAGE, L.BTN_DECREASE_BY_PACKAGE, name_key="package_name", quantity_key="package_qty")
        self.capture_step("Set packages", packages)
        
    def tap_confirm_packages(self):
        self.capture_step("Confirm packages")
        self.click(L.BTN_CONFIRM_PACKAGES)

    def tap_back(self):
        self.capture_step("Back from select package")
        self.click(L.BTN_BACK)

    def package_text(self, name):
        return self.label_of(L.EL_PACKAGE_BY_NAME.format(name))

    def package_quantity(self, name):
        return self.quantity_of(L.EL_PACKAGE_BY_NAME.format(name))

    def player_count_text(self):
        return self.label_of(L.EL_PLAYER_COUNT)

    def package_items(self):
        return self.texts_of(L.LIST_PACKAGES)

    def package_count(self):
        return self.count(L.LIST_PACKAGES)

    def has_package(self, name, timeout=5):
        return self.is_visible(L.EL_PACKAGE_BY_NAME.format(name), timeout)

    def decrease_is_disabled(self, name):
        return self.is_disabled(L.BTN_DECREASE_BY_PACKAGE.format(name))

    def confirm_is_enabled(self):
        return self.is_enabled(L.BTN_CONFIRM_PACKAGES)
