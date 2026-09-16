class VerificationCodeLocators:
    TXT_DESCRIPTION = '//XCUIElementTypeStaticText[starts-with(@name,"Enter the code")]'
    TXT_TITLE = '//XCUIElementTypeStaticText[@name="{} verification"]'
    INPUT_CODE = '//XCUIElementTypeTextField'
    BTN_SEND_AGAIN = '//XCUIElementTypeButton[@name="Send again"]'
    BTN_BACK = '//XCUIElementTypeButton[not(@name) and @enabled="true"]'
    LINK_TRY_OTHER_METHOD = '//XCUIElementTypeStaticText[starts-with(@name,"Try verification with")]'
    LINK_TRY_METHOD = '//XCUIElementTypeStaticText[@name="Try verification with {}"]'
    TXT_SCRIM = '//XCUIElementTypeStaticText[@name="Scrim"]'
