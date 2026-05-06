from difflib import SequenceMatcher
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')

database_sentences = [
    "Artificial intelligence is transforming healthcare.",
    "Machine learning improves automation systems.",
    "Deep learning is a subset of artificial intelligence."
]

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def check_plagiarism(text):

    uploaded_sentences = nltk.sent_tokenize(text)

    plagiarism_results = []

    for sentence in uploaded_sentences:

        for db_sentence in database_sentences:

            score = similarity(
                sentence.lower(),
                db_sentence.lower()
            )

            if score > 0.7:

                plagiarism_results.append({
                    "uploaded_sentence": sentence,
                    "matched_sentence": db_sentence,
                    "similarity_score": round(score * 100, 2)
                })

    originality_score = max(
        0,
        100 - (len(plagiarism_results) * 10)
    )

    return originality_score, plagiarism_results
