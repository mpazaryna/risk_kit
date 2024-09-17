import math


def calculate_mortgage_risk(loan_amount, property_value):
    if property_value <= 0:
        raise ValueError("Property value must be greater than zero")

    ltv_ratio = (loan_amount / property_value) * 100

    if ltv_ratio <= 80:
        risk_score = 1
    elif 80 < ltv_ratio <= 90:
        risk_score = 2
    elif 90 < ltv_ratio <= 95:
        risk_score = 3
    else:
        risk_score = 4

    return risk_score
