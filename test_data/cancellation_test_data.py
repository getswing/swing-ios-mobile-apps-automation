from helpers.exceldata import ExcelData


class CancellationTestData(ExcelData):
    SHEET = "Cancellation"
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
    REFUND = ""

    STATUS_BEFORE = "UPCOMING"
    STATUS_AFTER = "CANCELLED"
