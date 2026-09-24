class SelectPackageLocators:
    EL_HEADER = '//XCUIElementTypeOther[@name="Select package"]'
    BTN_BACK = '//XCUIElementTypeOther[@name="Select package"]/preceding-sibling::XCUIElementTypeButton[1]'
    EL_PLAYER_COUNT = '//XCUIElementTypeOther[substring-after(@name," ")="player" or substring-after(@name," ")="players"]'
    LIST_PACKAGES = '//XCUIElementTypeOther[contains(@name," for ") and contains(@name," player")]'
    EL_PACKAGE_BY_NAME = '//XCUIElementTypeOther[starts-with(@name,"{}") and contains(@name," for ")]'
    BTN_DECREASE_BY_PACKAGE = '//XCUIElementTypeOther[starts-with(@name,"{}") and contains(@name," for ")]/following-sibling::XCUIElementTypeButton[1]'
    BTN_INCREASE_BY_PACKAGE = '//XCUIElementTypeOther[starts-with(@name,"{}") and contains(@name," for ")]/following-sibling::XCUIElementTypeButton[2]'
    BTN_CONFIRM_PACKAGES = '//XCUIElementTypeButton[@name="Confirm packages"]'
