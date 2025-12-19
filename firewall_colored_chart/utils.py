import csv
import os

LOG_FILE = "logs.csv"

def rule_score(text):
    words = ["password", "winner", "click", "account", "verify", "login"]
    score = sum(20 for w in words if w in text.lower())
    return min(score, 100)

def log_result(text, result):
    file_exists = os.path.exists(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Email", "Final Score", "Threat Level"])

        writer.writerow([
            text.replace("\n", " ")[:80],
            result["Final Score"],
            result["Threat Level"]
        ])