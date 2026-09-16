class RegistrationMethodLocators:
    TXT_TITLE = '//XCUIElementTypeStaticText[@name="How would you like to register for this event?"]'
    EL_GROUP_REGISTRATION = '//XCUIElementTypeOther[starts-with(@name,"Group registration")]'
    EL_STANDARD_REGISTRATION = '//XCUIElementTypeOther[starts-with(@name,"Standard registration")]'
    EL_METHOD_BY_NAME = '//XCUIElementTypeOther[starts-with(@name,"{}")]'
    BTN_LEARN_MORE = '//XCUIElementTypeButton[@name="Learn more about registration methods"]'
    BTN_CLOSE = '//XCUIElementTypeButton[@name="Learn more about registration methods"]/following-sibling::XCUIElementTypeButton[1]'
    TXT_SCRIM = '//XCUIElementTypeStaticText[@name="Scrim"]'
