class GroupRegistrationInfoLocators:
    TXT_TITLE = '//XCUIElementTypeStaticText[starts-with(@name,"Adding a Swing Pass member?")]'
    TXT_BULLET_BY_TEXT = '//XCUIElementTypeStaticText[starts-with(@name,"{}")]'
    BTN_LEARN_MORE = '//XCUIElementTypeButton[@name="Learn more about registration methods"]'
    BTN_SWITCH_TO_GROUP = '//XCUIElementTypeButton[@name="Switch to group registration"]'
    BTN_CLOSE = '//XCUIElementTypeButton[@name="Switch to group registration"]/following-sibling::XCUIElementTypeButton[1]'
    TXT_SCRIM = '//XCUIElementTypeStaticText[@name="Scrim"]'
