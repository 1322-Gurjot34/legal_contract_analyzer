import re

def extract_key_info(text):
    info = {}

    # Find dates
    dates = re.findall(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b', text)
    info["Dates Found"] = dates

    # Find money values
    amounts = re.findall(r'₹\s?\d+(?:,\d+)*(?:\.\d+)?|\$\s?\d+(?:,\d+)*(?:\.\d+)?', text)
    info["Amounts Found"] = amounts

    # Find penalty related lines
    penalty_lines = []
    for sentence in text.split("."):
        if "penalty" in sentence.lower() or "fine" in sentence.lower():
            penalty_lines.append(sentence.strip())

    info["Penalty Clauses"] = penalty_lines

    # Find renewal related lines
    renewal_lines = []
    for sentence in text.split("."):
        if "renew" in sentence.lower() or "renewal" in sentence.lower() or "expire" in sentence.lower():
            renewal_lines.append(sentence.strip())

    info["Renewal Clauses"] = renewal_lines

    return info