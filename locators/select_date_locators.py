class SelectDateLocators:
    TXT_TITLE = '//XCUIElementTypeStaticText[@name="Select date"]'
    BTN_BACK = '//XCUIElementTypeButton[not(@name) and @enabled="true"]'
    TXT_MONTH_RANGE = '//XCUIElementTypeStaticText[contains(@name," to ")]'
    TXT_DATE = '//XCUIElementTypeStaticText[@name="{}"]'
    TXT_DATE_CONTAINS = '//XCUIElementTypeStaticText[contains(@name,"{}")]'
    LIST_DISABLED_DATES = '//XCUIElementTypeStaticText[contains(@name,"Disabled date")]'
    TXT_SCRIM = '//XCUIElementTypeStaticText[@name="Scrim"]'
