# calculate post anaesthesia recovery score
def calculate_post_anaesthesia_recovery_score(examination: dict):
    
# start with a score of 0
    running_score = 0

# see activity (cant move = 0, move 2 extremities = 1, moves all extremities = 2)
    activity = examination['activity']
    if activity == 'cant move':
        running_score = running_score + 0
    elif activity == 'moves 2 extremities':
        running_score = running_score + 1
    elif activity == 'moves all extremities':
        running_score == running_score + 2

# see respiration (apneic = 0, breathing limited/dyspnea = 1, breathing deeply/cough freely = 2)
    respiration = examination['respiration']
    if respiration == 'apneic':
        running_score = running_score + 0
    elif respiration == 'dyspnea':
        running_score = running_score + 1
    elif respiration == 'breathing deeply and cough freely':
        running_score = running_score + 2
        
# see circulation (<20% = 0, 20-49% = 1, >49% = 2)
    circulation = examination['circulation']
    if circulation <=19:
        running_score = running_score + 0
    elif 20>= circulation <=49:
        running_score = running_score + 1
    elif circulation >49:
        running_score = running_score + 2

# see consciousness (non-responsive = 0, rousable on calling = 1, fully awake = 1)
    consciousness = examination['consciousness']
    if consciousness == 'non-responsive':
        running_score = running_score + 0
    elif consciousness == 'rousable on calling':
        running_score = running_score + 1
    elif consciousness == 'fully awake':
        running_score = running_score + 2

# see oxygen saturation (<= 90% with supplemental O2 = 0, supplemental O2 to maintain >= 90% = 1, 92% on room air = 2)
# this does not account for on room air + less than 92%
    if examination['on_oxygen'] == True:
        if examination['oxygen_sat'] <= 90:
            running_score = running_score + 0
        if examination['oxygen_sat'] >= 90:
            running_score = running_score + 1
    else:
        running_score = running_score + 2   

# categorise recovery level
    if running_score >= 9:
        rec_category = 'safe discharge from PACU'
    elif running_score < 8:
        rec_category = 'individual status is suboptimal, further monitoring and management required in PACU to stabilise individual'

# return score with recovery level
    return f"Patient's score is {running_score}. Recommendation: {rec_category}"

seth_examination = {
    'activity': 'moves 2 extremities',
    'respiration': 'dyspnea',
    'circulation': '19',
    'consciousness': 'rousable on calling',
    'oxygen_on': True,
    'oxygen_sat': 85
}

response = calculate_post_anaesthesia_recovery_score(seth_examination)
print(response)
