from textblob import TextBlob

# Important keywords employers like to hear
keywords = [
    "teamwork", "leadership", "communication", "problem-solving", 
    "critical thinking", "adaptability", "motivation", "growth", "learning", "responsibility"
]

def analyze_answer(answer, ideal_answer):
    score = 0
    improvements = []

    # Length analysis
    if len(answer.split()) >= 20:
        score += 3
    elif len(answer.split()) >= 10:
        score += 2
    else:
        score += 1
        improvements.append("Try to give slightly longer, detailed answers.")

    # Sentiment analysis
    blob = TextBlob(answer)
    if blob.sentiment.polarity > 0.1:
        score += 3
    elif blob.sentiment.polarity > -0.1:
        score += 2
    else:
        score += 1
        improvements.append("Try to sound a bit more positive and confident.")

    # Keyword matching
    matched_keywords = [kw for kw in keywords if kw.lower() in answer.lower()]
    score += len(matched_keywords)

    if len(matched_keywords) < 2:
        improvements.append("Include important skills/keywords relevant to the job.")

    # Optional: Compare to ideal answer (text similarity simple check)
    ideal_blob = TextBlob(ideal_answer)
    similarity = blob.similarity(ideal_blob) if hasattr(blob, 'similarity') else 0  # textblob has no direct similarity
    # (You can later upgrade to spacy for better similarity)

    return min(score, 10), improvements
