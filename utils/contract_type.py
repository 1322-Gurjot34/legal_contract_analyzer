def detect_contract_type(text):
    text = text.lower()

    if "employee" in text or "salary" in text or "job" in text:
        return "Employment Contract"

    elif "rent" in text or "tenant" in text or "landlord" in text:
        return "Rental Agreement"

    elif "service" in text or "consultant" in text or "project" in text:
        return "Service Agreement"

    elif "confidential" in text or "non disclosure" in text or "nda" in text:
        return "Non-Disclosure Agreement (NDA)"

    elif "sale" in text or "buyer" in text or "seller" in text:
        return "Sales Contract"

    elif "partner" in text or "partnership" in text:
        return "Partnership Agreement"

    elif "lease" in text:
        return "Lease Agreement"

    else:
        return "Unknown Contract Type"