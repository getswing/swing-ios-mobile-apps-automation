class DrivingRangeSearchLocators:
    IMG_SEARCH_PLACEHOLDER = '//XCUIElementTypeImage[@name="Search..."]'
    INPUT_SEARCH = '//XCUIElementTypeOther[XCUIElementTypeOther[@name="ID"]]/preceding-sibling::XCUIElementTypeTextField'
    EL_COUNTRY = '//XCUIElementTypeOther[@name="ID"]'
    TXT_RESULT_COUNT = '//XCUIElementTypeStaticText[contains(@name,"driving range (s) found")]'
    EL_RESULT_BY_NAME = '//XCUIElementTypeOther[starts-with(@name,"{}")]'
    BTN_CLEAR = '//XCUIElementTypeTextField/following-sibling::XCUIElementTypeImage[1]'
    BTN_KEYBOARD_SEARCH = '//XCUIElementTypeButton[@name="Search"]'
