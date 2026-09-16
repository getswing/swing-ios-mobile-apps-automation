import pytest

from helpers.pdf_report import init_pdf
from test_data.swing_credit_test_data import SwingCreditTestData as D
from flows.swing_credit_flow import SwingCreditFlow


class TestSwingCredit:
    
    @pytest.mark.app_reset("force-close")
    @pytest.mark.skip
    @pytest.mark.parametrize("TC_ID", ["SWING_CREDIT_001"])
    def test_verify_swing_credit(self,TC_ID, swing_credit_flow: SwingCreditFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        swing_credit_flow.open_swing_credits()
        swing_credit_flow.verify_swing_credits()
    
    @pytest.mark.app_reset("force-close")
    @pytest.mark.skip
    @pytest.mark.parametrize("TC_ID", ["SWING_CREDIT_002"])
    def test_verify_swing_history(self,TC_ID, swing_credit_flow: SwingCreditFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        swing_credit_flow.open_swing_credits()
        swing_credit_flow.verify_swing_credits()
        swing_credit_flow.open_history()
    
    @pytest.mark.app_reset("force-close")
    @pytest.mark.regression
    @pytest.mark.parametrize("TC_ID", ["SWING_CREDIT_003"])
    def test_verify_swing_credit_used_by_booking_code(self,TC_ID, swing_credit_flow: SwingCreditFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        swing_credit_flow.open_swing_credits()
        swing_credit_flow.verify_swing_credits()
        swing_credit_flow.open_history()
        swing_credit_flow.verify_used_credit_booking_code(D.BOOKING_CODE, D.TOTAL_CREDITS)
        
    @pytest.mark.app_reset("force-close")
    @pytest.mark.skip
    @pytest.mark.parametrize("TC_ID", ["SWING_CREDIT_004"])
    def test_verify_swing_credit_earn_by_booking_code(self,TC_ID, swing_credit_flow: SwingCreditFlow):
        D.load(TC_ID)
        pdf = init_pdf(D.TC_NAME, tc_id=TC_ID)
        swing_credit_flow.open_swing_credits()
        swing_credit_flow.verify_swing_credits()
        swing_credit_flow.open_history()
        swing_credit_flow.verify_earn_credit_booking_code(D.BOOKING_CODE, D.TOTAL_CREDITS)
    

