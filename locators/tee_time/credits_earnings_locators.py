class TeeTimeCreditsEarningsLocators:
    TXT_TITLE = '//XCUIElementTypeStaticText[@name="Swing Credits earnings"]'
    TXT_EARNING_BY_PLAYER = '//XCUIElementTypeStaticText[starts-with(@name,"{}")]'
    IMG_EARNING_BY_PLAYER = '//XCUIElementTypeImage[starts-with(@name,"{}")]'
    EL_EARNING_BY_PLAYER = '//XCUIElementTypeStaticText[starts-with(@name,"{}")] | //XCUIElementTypeImage[starts-with(@name,"{}")]'
    LIST_EARNINGS = '//XCUIElementTypeStaticText[contains(@name,"%")] | //XCUIElementTypeImage[contains(@name,"%")]'
    TXT_CREDITS_NOTE = '//XCUIElementTypeImage[contains(@name,"Swing Credits will only be issued")]'
    BTN_GOT_IT = '//XCUIElementTypeButton[@name="Got it!"]'
    TXT_SCRIM = '//XCUIElementTypeStaticText[@name="Scrim"]'
