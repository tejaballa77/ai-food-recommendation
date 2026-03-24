from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# -------- Knowledge Base --------
documents = [
    "Diabetes patients should avoid sugar and high carbohydrates and prefer fiber and protein rich food.",
    "Hypertension patients should avoid salt and sodium rich food and prefer low sodium vegetables.",
    "Cholesterol patients should avoid fried and oily food and prefer grilled and low fat food.",
    "Fever patients should eat light, liquid and easily digestible food like soup.",
    "Cold patients should avoid cold drinks and prefer warm fluids and hot food.",
    "Cough patients should avoid fried food and consume warm liquids.",
    "Weight loss requires low calorie, high protein food and avoiding sugar and fried items.",
    "Weight gain requires high calorie and protein rich food.",
    "Acidity patients should avoid spicy food and prefer light meals.",
    "Anemia patients should consume iron rich food like leafy vegetables."
]

# Convert to embeddings
doc_embeddings = model.encode(documents)

# Create FAISS index
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_embeddings))


# -------- Retrieve Relevant Knowledge --------
def get_relevant_knowledge(query):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k=1)

    return documents[indices[0][0]]