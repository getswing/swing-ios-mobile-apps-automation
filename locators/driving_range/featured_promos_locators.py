class FeaturedPromosLocators:
    EL_HEADER = '//XCUIElementTypeOther[@name="Featured promos"]'
    BTN_BACK = '//XCUIElementTypeOther[@name="Featured promos"]/preceding-sibling::XCUIElementTypeButton[1]'
    IMG_AUTO_CLAIM_NOTICE = '//XCUIElementTypeImage[starts-with(@name,"Featured promos are now automatically claimed")]'
    IMG_PROMO_BY_NAME = '//XCUIElementTypeImage[starts-with(@name,"{0}")]'
    TXT_QUOTA_BY_PROMO = '//XCUIElementTypeImage[starts-with(@name,"{0}")]/following-sibling::XCUIElementTypeStaticText[1]'
    LIST_PROMOS = '//XCUIElementTypeImage[contains(@name,"Validity")]'
    LIST_QUOTAS = '//XCUIElementTypeStaticText[starts-with(@name,"x")]'
    IMG_SWING_PASS_PROMO = '//XCUIElementTypeImage[contains(@name,"Swing Pass Exclusive")]'
