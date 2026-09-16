class VerificationMethodLocators:
    TXT_TITLE = '//XCUIElementTypeStaticText[@name="Select verification method"]'
    IMG_SMS = '//XCUIElementTypeImage[starts-with(@name,"SMS")]'
    IMG_WHATSAPP = '//XCUIElementTypeImage[@name="WhatsApp"]'
    IMG_METHOD = '//XCUIElementTypeImage[starts-with(@name,"{}")]'
    LIST_METHODS = '//XCUIElementTypeImage[@name]'
    BTN_CONFIRM = '//XCUIElementTypeStaticText[@name="Select verification method"]/following-sibling::XCUIElementTypeButton[1]'
    TXT_SCRIM = '//XCUIElementTypeStaticText[@name="Scrim"]'
