class GroupBookingInfoLocators:
    TXT_TITLE = '//XCUIElementTypeStaticText[starts-with(@name,"Adding a Swing Pass member?")]'
    TXT_BULLET_BY_TEXT = '//XCUIElementTypeStaticText[starts-with(@name,"{}")]'
    BTN_LEARN_MORE = '//XCUIElementTypeButton[@name="Learn more about booking methods"]'
    BTN_SWITCH_TO_GROUP = '//XCUIElementTypeButton[@name="Switch to group booking"]'
    BTN_CLOSE = '//XCUIElementTypeButton[@name="Switch to group booking"]/following-sibling::XCUIElementTypeButton[1]'
    TXT_SCRIM = '//XCUIElementTypeStaticText[@name="Scrim"]'
