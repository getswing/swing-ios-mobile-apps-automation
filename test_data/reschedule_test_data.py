from helpers.exceldata import ExcelData


class RescheduleTestData(ExcelData):
    SHEET = "Reschedule"
    ALIASES = {"VERIFICATION_METHOD": "METHOD_VERIFICATION"}

    COUNTRY_NAME = "Indonesia"
    PHONE_NUMBER = "82165162549"
    METHOD_VERIFICATION = "whatsapp"
    OTP = ""
    SPORT_TYPE = "Golf"

    ACTIVITY_FILTER = "Driving range"
    ACTIVITY_CARD = "Albatross Driving Range"
    BOOKING_CODE = ""
    VENUE = "Albatross Driving Range"

    PLAYER_NAME = "QA Auto Mation"
    DURATION = "60 minutes"
    BAY_TYPE = "Regular"

    ORIGINAL_DATE_TIME = ""
    NEW_DATE = "19"
    NEW_TIME = "15:00"
    NEW_DATE_TIME = ""
    REASON = "Wrong date or time booked"

    TOTAL_PAYMENT = ""
    PAYMENT_METHOD = "DANA"
    STATUS_BEFORE = "UPCOMING"
    STATUS_AFTER = "RESCHEDULED"
    
    TC_NAME = ""
