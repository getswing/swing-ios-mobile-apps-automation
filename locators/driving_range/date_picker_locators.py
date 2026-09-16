class DatePickerLocators:
    TXT_TITLE = '//XCUIElementTypeStaticText[@name="Select date"]'
    BTN_BACK = '//XCUIElementTypeStaticText[@name="Select date"]/preceding-sibling::XCUIElementTypeButton[1]'
    TXT_MONTH_RANGE = '//XCUIElementTypeStaticText[contains(@name," to ")]'
    TXT_DAY_BY_LABEL = '//XCUIElementTypeStaticText[contains(@name,"{}")]'
    TXT_DISABLED_DAY = '//XCUIElementTypeStaticText[contains(@name,"Disabled date")]'
    LIST_ENABLED_DAYS = '//XCUIElementTypeStaticText[contains(@name," 2026") and not(contains(@name,"Disabled date"))]'
    TXT_SCRIM = '//XCUIElementTypeStaticText[@name="Scrim"]'
