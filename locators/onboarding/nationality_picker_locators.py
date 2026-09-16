class NationalityPickerLocators:
    TXT_TITLE = '//XCUIElementTypeStaticText[@name="Select nationality"]'
    BTN_BACK = '//XCUIElementTypeStaticText[@name="Select nationality"]/preceding-sibling::XCUIElementTypeButton[1]'
    EL_SEARCH_COUNTRY = '//XCUIElementTypeOther[@name="Search country"]'
    INPUT_SEARCH = '//XCUIElementTypeOther[@name="Search country"]/following-sibling::XCUIElementTypeTextField'
    LIST_COUNTRIES = '//XCUIElementTypeScrollView/following-sibling::XCUIElementTypeStaticText'
    TXT_COUNTRY_BY_NAME = '//XCUIElementTypeStaticText[@name="{}"]'
    TXT_SCRIM = '//XCUIElementTypeStaticText[@name="Scrim"]'
