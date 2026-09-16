class NotificationPermissionLocators:
    TXT_DESCRIPTION = '//XCUIElementTypeStaticText[starts-with(@name,"Enable notifications")]'
    BTN_ENABLE = '//XCUIElementTypeButton[@name="Enable notifications"]'
    BTN_LATER = '//XCUIElementTypeButton[contains(@name,"do it later")]'
    BTN_UNLABELED = '//XCUIElementTypeButton[not(@name)]'
    TXT_SCRIM = '//XCUIElementTypeStaticText[@name="Scrim"]'
