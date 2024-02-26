"""
This file contains a function to calculate the BMI of a person.
"""


def calculate_bmi(weight, height):
    """
    Calculate the BMI of a person.

    Args:
        weight (float): weight of the person in kg
        height (float): height of the person in meters

    Returns:
        float: the BMI of the person
    """
    
    # if height is over 2.5m, assume is in centimeters and convert to metres
    if height > 2.5:
        height = height / 100

    # calculate bmi
    bmi = weight/(height*height)
    
    # return bmi
    return round(bmi, 2)

bob_weight = 70 # in kg
bob_height = 175 # in meter


bmi = calculate_bmi(height=bob_height, weight=bob_weight)
print(bmi)

import pandas as pd
pd.read_csv('patients_data.csv')
