def search_keyword_in_contract(text, keyword):
    results = []

    sentences = text.split(".")

    for sentence in sentences:
        if keyword.lower() in sentence.lower():
            results.append(sentence.strip())

    return results