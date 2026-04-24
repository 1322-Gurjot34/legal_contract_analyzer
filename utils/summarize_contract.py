def summarize_contract(text):
    import re
    from collections import Counter

    # Clean text
    text = text.replace("\n", " ")
    sentences = re.split(r'(?<=[.!?]) +', text)

    # Remove very short/long sentences
    sentences = [s.strip() for s in sentences if 40 < len(s) < 250]

    # Keywords (weighted importance)
    keywords = [
        "agreement", "payment", "fee", "cost", "salary",
        "terminate", "termination", "confidential",
        "renewal", "extension", "penalty", "liability",
        "obligation", "deadline", "notice", "risk"
    ]

    # Count keyword frequency in whole text
    word_freq = Counter(text.lower().split())

    sentence_scores = {}

    for sentence in sentences:
        score = 0
        words = sentence.lower().split()

        for word in words:
            if word in word_freq:
                score += word_freq[word]

        # Boost score if important keywords present
        for keyword in keywords:
            if keyword in sentence.lower():
                score += 20

        sentence_scores[sentence] = score

    # Get top 5 best sentences
    best_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:5]

    return best_sentences