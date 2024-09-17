import numpy as np


# Function to assess risk based on individual parameters
def assess_risk(annual_income, credit_score, debt_to_income):
    if annual_income < 40000 or credit_score < 650 or debt_to_income > 0.4:
        return 1  # High risk
    return 0  # Low risk


# Create risk classification using assess_risk
def classify_risk(data):
    return np.array([assess_risk(row[0], row[1], row[2]) for row in data])


def assess_mortgage_eligibility(annual_income, credit_score, down_payment):
    home_price = 500000
    required_income = home_price * 0.2
    required_down_payment = home_price * 0.1

    if (
        annual_income >= required_income
        and credit_score >= 650
        and down_payment >= required_down_payment
    ):
        eligibility = True
    else:
        eligibility = False

    return eligibility
