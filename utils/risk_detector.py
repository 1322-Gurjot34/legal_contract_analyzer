def detect_risks(text):
    risks = []

    risk_keywords = {
        "Penalty Risk": ["penalty", "fine", "late fee", "charges"],
        "Termination Risk": ["terminate", "termination", "cancel", "breach"],
        "Renewal Risk": ["auto renew", "renewal", "renew automatically"],
        "Exclusivity Risk": ["exclusive", "sole rights", "only provider"],
        "Confidentiality Risk": ["confidential", "non disclosure", "NDA"],
        "Legal Dispute Risk": ["court", "lawsuit", "legal action", "dispute"]
    }

    text_lower = text.lower()

    for risk_type, keywords in risk_keywords.items():
        found_sentences = []

        for sentence in text.split("."):
            for keyword in keywords:
                if keyword in sentence.lower():
                    found_sentences.append(sentence.strip())
                    break

        if found_sentences:
            risks.append({
                "Risk Type": risk_type,
                "Sentences": found_sentences[:3]
            })

    return risks