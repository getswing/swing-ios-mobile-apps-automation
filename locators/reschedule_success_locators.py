class RescheduleSuccessLocators:
    TXT_TITLE = '//XCUIElementTypeStaticText[@name="Booking rescheduled"]'
    TXT_SUBTITLE = '//XCUIElementTypeStaticText[starts-with(@name,"See you on")]'
    TXT_VENUE = '//XCUIElementTypeStaticText[contains(@name,"Driving Range")]'
    TXT_BOOKING_ID = '//XCUIElementTypeStaticText[starts-with(@name,"Booking #")]'
    IMG_DATE_CHANGE = '//XCUIElementTypeImage[starts-with(@name,"Original date")]'
    TXT_FIELD = '//XCUIElementTypeStaticText[@name="{}"]'
    BTN_FINISH = '//XCUIElementTypeButton[@name="Finish"]'
    BTN_SEE_BOOKING_DETAILS = '//XCUIElementTypeButton[@name="See booking details"]'
