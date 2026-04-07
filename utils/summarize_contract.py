def summarize_contract(text):
    sentences = text.replace("\n", " ").split(".")

    important_keywords = [
        "agreement",
        "payment",
        "fee",
        "cost",
        "salary",
        "terminate",
        "termination",
        "confidential",
        "non disclosure",
        "renew",
        "renewal",
        "extension",
        "penalty",
        "fine",
        "liability",
        "obligation",
        "party",
        "deadline",
        "delivery",
        "notice"
    ]

    summary_points = []

    for sentence in sentences:
        sentence = sentence.strip()

        if len(sentence) < 40:
            continue

        for keyword in important_keywords:
            if keyword.lower() in sentence.lower():
                if sentence not in summary_points:
                    summary_points.append(sentence)
                break

    if len(summary_points) == 0:
        summary_points = sentences[:5]

    return summary_points[:7]