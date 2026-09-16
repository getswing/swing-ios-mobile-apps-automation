class SendReceiptLocators:
    TXT_TITLE = '//XCUIElementTypeStaticText[@name="Send receipt"]'
    TXT_DESCRIPTION = '//XCUIElementTypeStaticText[contains(@name,"send you a code")]'
    INPUT_EMAIL = '//XCUIElementTypeTextField'
    BTN_SEND = '//XCUIElementTypeButton[@name="Send receipt"]'
    BTN_BACK = '//XCUIElementTypeButton[not(@name) and @enabled="true"]'
    TXT_SCRIM = '//XCUIElementTypeStaticText[@name="Scrim"]'
