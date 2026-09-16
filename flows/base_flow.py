from typing import TypeVar, cast

from config.settings import settings
from helpers import alerts, app_helper, device, gestures, media, waits
from helpers.logger import get_logger
from helpers.reporter import reporter as default_reporter
from pages.base_page import BasePage

PageT = TypeVar("PageT", bound=BasePage)


class BaseFlow:
    FLOW_NAME = "BaseFlow"

    def __init__(self, driver, reporter=None):
        self.driver = driver
        self.settings = settings
        self.reporter = reporter or default_reporter
        self.log = get_logger(self.__class__.__name__)
        self._pages: dict[str, BasePage] = {}

    def page(self, page_class: type[PageT]) -> PageT:
        key = page_class.__name__
        if key not in self._pages:
            self._pages[key] = page_class(self.driver)
        return cast(PageT, self._pages[key])

    def step(self, description):
        self.reporter.step(description)
        return self

    def restart_app(self):
        app_helper.restart(self.driver)
        return self

    def terminate_app(self):
        app_helper.terminate(self.driver)
        return self

    def activate_app(self):
        app_helper.activate(self.driver)
        return self

    def background_app(self, seconds=5):
        device.background_app(self.driver, seconds)
        return self

    def open_deeplink(self, url):
        device.open_deeplink(self.driver, url, settings.BUNDLE_ID)
        return self

    def handle_system_alerts(self, accept=True, max_alerts=3):
        alerts.handle_all(self.driver, accept, max_alerts)
        return self

    def swipe(self, direction="up"):
        gestures.swipe(self.driver, direction)
        return self

    def wait_for(self, condition, timeout=None, message="flow condition failed"):
        waits.wait_until_true(condition, timeout, message=message)
        return self

    def screenshot(self, name=None):
        path = media.screenshot(self.driver, name or self.FLOW_NAME)
        self.reporter.attach(path, name or self.FLOW_NAME)
        return path
