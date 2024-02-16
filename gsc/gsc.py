

def gcs_category(eyes,verbal,motor):
    total = eyes + verbal + motor
    if total > 15 or total < 3:
        raise ValueError(f'The Value {total} is invalid.')
    if total > 12:
        category = 'mild'
    elif total > 8:
        category = 'moderate'
    else:
        category = 'severe'
    return category

patient_eyes = 3
patient_verbal = 4
patient_motor = 10

result = gcs_category(patient_eyes, patient_verbal, patient_motor)
print(result)
