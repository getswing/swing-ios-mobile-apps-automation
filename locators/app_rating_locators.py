class AppRatingLocators:
    TXT_TITLE = '//XCUIElementTypeStaticText[starts-with(@name,"Enjoying")]'
    TXT_SUBTITLE = '//XCUIElementTypeStaticText[starts-with(@name,"Tap a star")]'
    LIST_STARS = '//XCUIElementTypeButton[@name="star"]'
    BTN_STAR_BY_INDEX = '(//XCUIElementTypeButton[@name="star"])[{}]'
    BTN_NOT_NOW = '//XCUIElementTypeButton[@name="Not Now"]'
