class BookingMethodLocators:
    TXT_TITLE = '//XCUIElementTypeStaticText[@name="How would you like to make this tee time booking?"]'
    EL_GROUP_BOOKING = '//XCUIElementTypeOther[starts-with(@name,"Group booking")]'
    EL_STANDARD_BOOKING = '//XCUIElementTypeOther[starts-with(@name,"Standard booking")]'
    EL_METHOD_BY_NAME = '//XCUIElementTypeOther[starts-with(@name,"{}")]'
    BTN_LEARN_MORE = '//XCUIElementTypeButton[@name="Learn more about booking methods"]'
    BTN_CLOSE = '//XCUIElementTypeButton[@name="Learn more about booking methods"]/following-sibling::XCUIElementTypeButton[1]'
    TXT_SCRIM = '//XCUIElementTypeStaticText[@name="Scrim"]'
