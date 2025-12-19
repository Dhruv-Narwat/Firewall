from ml_model import ml_predict
from utils import rule_score, log_result

def analyze_email(text):
    ml = ml_predict(text)
    rule = rule_score(text)
    final = int(0.75 * ml + 0.25 * rule)

    if final >= 80:
        level = "HIGH"
    elif final >= 50:
        level = "MEDIUM"
    else:
        level = "LOW"

    result = {
        "ML Score": ml,
        "Rule Score": rule,
        "Final Score": final,
        "Threat Level": level
    }

    log_result(text, result)
    return result