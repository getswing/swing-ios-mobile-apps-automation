# SWING_APPS_IOS

Appium + pytest iOS automation for real devices and simulators.

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Appium server side (once):

```bash
npm install -g appium
appium driver install xcuitest
appium
```

## Configure

```bash
cp .env.simulator.example .env.simulator
cp .env.real_device.example .env.real_device
cp .env.example .env
```

`TARGET=simulator` loads `.env.simulator`, `TARGET=real_device` loads `.env.real_device`, anything else loads `.env`.
`APP_MODE=bundle_id` uses `BUNDLE_ID` on an already-installed app; `APP_MODE=app_path` installs from `APP_PATH` (.app for simulator, .ipa for device).

## Run

```bash
TARGET=simulator pytest
TARGET=real_device pytest -m smoke
pytest --target real_device --udid 00008110-000A4D9E0C63801E --bundle-id com.swing.apps
pytest -m regression -n 2
```

## Layout

```
config/      settings from .env, XCUITest capability builder
locators/    plain xpath string constants, one class per screen
pages/       base_page.py + one page object per screen
flows/       base_flow.py + business flows composed from pages
fixtures/    pytest fixtures (driver, pages, flows, data)
helpers/     driver_factory, waits, gestures, device, app, alerts, keyboard, media, reporter, assertions, logger
tests/       pytest tests
```

## Locators from XML

Locators are plain xpath strings:

```python
class LoginLocators:
    INPUT_PHONE_NUMBER = '//XCUIElementTypeTextField[@name="phone_number"]'
    BTN_LOGIN = '//XCUIElementTypeButton[@name="login_button"]'
    CELL_BY_TITLE = '//XCUIElementTypeCell[@label="{}"]'
```

```python
self.click(L.BTN_LOGIN)
self.click(L.CELL_BY_TITLE.format("Alpha"))
```

Paste the page source and run `/locator <screen name>` - it writes the locators and then the page
object - or drive the parser directly:

```bash
python3 .claude/skills/ios-locator/xml_to_locators.py dump.xml --report
python3 .claude/skills/ios-locator/xml_to_locators.py dump.xml --class-name HomeLocators --output locators/home_locators.py
```

## Page objects

Pages stay thin: one line per interaction, straight to a `BasePage` helper. No waits, no
asserts, no logging in the page. Assertions live in tests, orchestration in flows.

```python
class LoginPage(BasePage):
    ROOT_LOCATOR = L.INPUT_PHONE_NUMBER
    PAGE_NAME = "LoginPage"

    def enter_phone_number(self, number):
        return self.type(L.INPUT_PHONE_NUMBER, number, hide_keyboard=True)

    def tap_continue(self):
        return self.click(L.BTN_CONTINUE)
```

Every page defines `verify_screen()` — the only place a page asserts:

```python
    def verify_screen(self):
        self.wait_until_loaded()
        assert self.is_visible(L.TXT_TITLE, timeout=20), "Country picker screen not shown"
        assert self.is_visible(L.EL_SEARCH_BAR, timeout=5), "Country search bar not shown"
        assert self.is_visible(L.BTN_BACK, timeout=5), "Country picker back button not shown"
        self.capture_step("country_picker")
        return self
```

First anchor `timeout=20` (screen may still be arriving), the rest `timeout=5`. `capture_step`
puts a named screenshot in the step report. Call it at each screen boundary:

```
   - note       wait for CountryPickerPage
   - read       is visible TXT_TITLE -> True
   - read       is visible EL_SEARCH_BAR -> False
AssertionError: Country search bar not shown
```

Scaffold a page from its locators file:

```bash
python3 .claude/skills/ios-page/page_scaffold.py locators/country_picker_locators.py
python3 .claude/skills/ios-page/page_scaffold.py locators/country_picker_locators.py --output pages/country_picker_page.py
```

Or run `/page <screen>`. `/locator` now continues into the page automatically and stops there —
flows and tests stay hand-written.

## Step report

Every `BasePage` action and read is recorded automatically, so a page method costs nothing
extra to report. `flow.step("...")` adds a business-level line on top.

```
tests/test_login.py::test_request_code [passed] 8.31s
    1     0.10s  step       open login screen
    2     0.42s  action     click PICKER_COUNTRY
    3     1.05s  action     type INPUT_PHONE_NUMBER = 81234567890
    4     1.90s  read       is enabled BTN_CONTINUE -> True
    5     2.11s  action     click BTN_CONTINUE
```

Locator constants are resolved back to their names, so the report reads `BTN_CONTINUE`
rather than the xpath.

Each run writes `reports/steps/run_<timestamp>.json` and `.txt`, and the steps are attached
to the pytest-html report per test.

Steps are also printed live as they happen — the action line goes out *before* the click or
type is performed, so a hang tells you exactly which element it is stuck on. Run with `-s` to
see them while the test runs:

```bash
pytest -s -m smoke
```

```
==> open login screen
   - action     click PICKER_COUNTRY
   - action     type INPUT_PHONE_NUMBER = 81234567890
   - read       is enabled BTN_CONTINUE -> True
   - action     click BTN_CONTINUE
```

Without `-s` pytest captures the prints and shows them on failure.

| Key | Default | Effect |
|---|---|---|
| `STEP_REPORT` | `true` | Record steps at all |
| `STEP_PRINT` | `true` | Print each step to stdout as it happens |
| `STEP_SCREENSHOTS` | `false` | Capture a screenshot per step into `reports/screenshots/steps/<run>/` |

```bash
STEP_SCREENSHOTS=true pytest -s -m smoke
```

With `STEP_SCREENSHOTS=true` every step entry carries a `screenshot` path in the JSON, which
is the input a PDF renderer needs. The renderer itself is not built yet and will need
`fpdf2` or `reportlab` added to requirements.

## Flows

Pages bound in `__init__`, one method per business action, `verify_screen()` at every screen
boundary:

```python
class EventsFlow(BaseFlow):
    def __init__(self, driver, reporter=None):
        super().__init__(driver, reporter)
        self.home = self.page(HomePage)
        self.list = self.page(EventsListPage)

    def open_events(self):
        self.home.open_events()
        self.list.verify_screen()
```

No asserts, no waits, no locators in a flow. `/flow <journey>` builds one.

## Tests

```python
class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.parametrize("TC_ID", ["LOGIN_001"])
    def test_login_screen_shows_phone_form(self, TC_ID, login_flow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        login_flow.open_login()
```

Data comes from `fixtures/data/<TC_ID>.yaml` through `D`, never from literals:

```yaml
tc_name: Login with valid phone number
country_name: Indonesia
phone_number: "81234567890"
```

`/test <feature>` writes one.

## PDF report per test case

`init_pdf(D.TC_NAME, tc_id=TC_ID)` turns the step report into a PDF: a header page (case, status,
duration, target, device, failure), then every step with its screenshot. It forces a screenshot per
step for that test regardless of `STEP_SCREENSHOTS`, and writes
`reports/pdf/<TC_ID>_<name>_<run>.pdf` when the test finishes. The path is also attached to the
pytest-html report.

Needs `fpdf2` (in `requirements.txt`). Without it the run still passes and the PDF is skipped with
a warning.
