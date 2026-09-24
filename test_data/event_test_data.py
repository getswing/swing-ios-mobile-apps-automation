from helpers.exceldata import ExcelData


class EventTestData(ExcelData):
    SHEET = "Event"
    ALIASES = {"VERIFICATION_METHOD": "METHOD_VERIFICATION", "EVENT_NAME": "EVENT"}

    COUNTRY_NAME = "Indonesia"
    PHONE_NUMBER = "82165162549"
    METHOD_VERIFICATION = "whatsapp"
    OTP = ""
    SPORT_TYPE = "Golf"

    MEMBER_TYPE = ""
    PLAYER_NAME = ""
    SEARCH_KEYWORD = ""
    EVENT = ""
    VENUE = ""

    EVENT_DATE = ""
    STARTING_TIME = ""
    REGISTRATION_METHOD = "Standard"
    TOTAL_PLAYERS = "1"
    QUESTION_ANSWER = ""
    FLIGHT = ""

    PROMO_NAME = ""
    PROMO_CODE = ""
    PAYMENT_METHOD = "DANA"
    
    TC_NAME = ""
    
    TOTAL_PRICE = ""
