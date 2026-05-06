from sentence_transformers import SentenceTransformer, util
import nltk

nltk.download('punkt')

model = SentenceTransformer('all-MiniLM-L6-v2')

database_sentences = [
    "Artificial intelligence is transforming healthcare.",
    "Machine learning improves automation systems.",
    "Deep learning is a subset of artificial intelligence."
]

def check_plagiarism(text):
    uploaded_sentences = nltk.sent_tokenize(text)

    plagiarism_results = []

    for sentence in uploaded_sentences:
        sentence_embedding = model.encode(sentence, convert_to_tensor=True)

        for db_sentence in database_sentences:
            db_embedding = model.encode(db_sentence, convert_to_tensor=True)

            similarity = util.cos_sim(sentence_embedding, db_embedding).item()

            if similarity > 0.7:
                plagiarism_results.append({
                    "uploaded_sentence": sentence,
                    "matched_sentence": db_sentence,
                    "similarity_score": round(similarity * 100, 2)
                })

    originality_score = max(0, 100 - (len(plagiarism_results) * 10))

    return originality_score, plagiarism_results