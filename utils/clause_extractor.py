def extract_clauses(text):
    clauses = {
        "Payment Clause": [],
        "Termination Clause": [],
        "Confidentiality Clause": [],
        "Renewal Clause": []
    }

    sentences = text.split(".")

    for sentence in sentences:
        sentence_lower = sentence.lower()

        if "payment" in sentence_lower or "fee" in sentence_lower:
            clauses["Payment Clause"].append(sentence.strip())

        if "terminate" in sentence_lower or "termination" in sentence_lower:
            clauses["Termination Clause"].append(sentence.strip())

        if "confidential" in sentence_lower or "non disclosure" in sentence_lower:
            clauses["Confidentiality Clause"].append(sentence.strip())

        if "renew" in sentence_lower or "extension" in sentence_lower:
            clauses["Renewal Clause"].append(sentence.strip())

    return clauses