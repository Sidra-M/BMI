

def calculate_air_score(examination: dict):
    
    # start with score of 0
    running_score = 0 

    # see if vomiting, add 1 to running score
    if examination['vomiting'] == True:
        running_score = running_score + 1

    # see if rif pain
    if examination['rif_pain'] == True:
        running_score = running_score + 1

    # score light, medium, sever in reboubd
    rebound_in_lowercase = examination['rebound'].lower()
    if rebound_in_lowercase == "light":
        running_score = running_score + 1
    elif rebound_in_lowercase == "medium":
        running_score = running_score + 2
    elif rebound_in_lowercase == 'strong':
        running_score = running_score + 3

    # see if fever
    if examination['fever'] == True:
        running_score = running_score + 1

    # score wbc
    if 15 > examination['wbc'] >= 10:
        running_score = running_score + 1
    elif examination['wbc'] > 15:
        running_score = running_score + 2

    # score crp
    if 49 > examination['crp'] > 10: 
        running_score = running_score + 1
    elif examination['crp'] > 50:
        running_score = running_score + 2

    # categorise with recommendation
    if running_score <= 4:
        category = "Total Score 0 - 4. Recommend discharge home"
    elif running_score <= 8:
        category = "Total Score 5 - 8. Recommend monitor in hospital"
    elif running_score >= 9:
        category = "Total Score 9 - 12. Recommend emergency surgery"

    # return score with recommendation 
    return f"Patient's Score is {running_score}. Recommendation: {category}"



johnny_examination = {
    "vomiting": True,
    "rif_pain": True,
    "rebound": "MEDIUM", 
    "fever": True,
    "wbc": "11",
    "crp": 20
}

response = calculate_air_score(johnny_examination)
print(response)
