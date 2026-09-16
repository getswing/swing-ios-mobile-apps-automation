from helpers.exceldata import ExcelData


class LoginTestData(ExcelData):
    SHEET = "Login"
    ALIASES = {"VERIFICATION_METHOD": "METHOD_VERIFICATION"}

    COUNTRY_NAME = "Indonesia"
    PHONE_NUMBER = "82165162549"
    METHOD_VERIFICATION = "whatsapp"
    OTP = ""
    SPORT_TYPE = "Golf"
    TC_NAME = ""
