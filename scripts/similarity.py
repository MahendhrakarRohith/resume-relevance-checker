from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight embeddings

def compute_similarity(job_desc, resume_text):
    job_embedding = model.encode(job_desc, convert_to_tensor=True)
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    score = util.pytorch_cos_sim(job_embedding, resume_embedding)
    return float(score[0][0])