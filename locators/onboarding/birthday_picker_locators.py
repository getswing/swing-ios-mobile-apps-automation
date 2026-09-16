class BirthdayPickerLocators:
    TXT_TITLE = '//XCUIElementTypeStaticText[@name="Select birthday"]'
    BTN_BACK = '//XCUIElementTypeStaticText[@name="Select birthday"]/preceding-sibling::XCUIElementTypeButton[1]'
    LIST_WHEELS = '//XCUIElementTypeScrollView'
    EL_WHEEL_BY_INDEX = '(//XCUIElementTypeScrollView)[{}]'
    TXT_VALUE_BY_NAME = '//XCUIElementTypeStaticText[@name="{}"]'
    BTN_CONFIRM = '//XCUIElementTypeButton[@name="Confirm"]'
    TXT_SCRIM = '//XCUIElementTypeStaticText[@name="Scrim"]'
    
    WHEEL_MONTH = "(//XCUIElementTypeScrollView)[1]"
    WHEEL_DAY = "(//XCUIElementTypeScrollView)[2]"
    WHEEL_YEAR = "(//XCUIElementTypeScrollView)[3]"
