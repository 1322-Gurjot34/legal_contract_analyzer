def calculate_contract_score(risks):
    score = 100

    for risk in risks:
        risk_type = risk["Risk Type"]

        if risk_type == "Penalty Risk":
            score -= 15
        elif risk_type == "Termination Risk":
            score -= 20
        elif risk_type == "Renewal Risk":
            score -= 10
        elif risk_type == "Exclusivity Risk":
            score -= 15
        elif risk_type == "Confidentiality Risk":
            score -= 10
        elif risk_type == "Legal Dispute Risk":
            score -= 20

    if score >= 80:
        level = "Low Risk"
    elif score >= 50:
        level = "Medium Risk"
    else:
        level = "High Risk"

    return score, level