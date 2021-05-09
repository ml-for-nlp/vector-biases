from utils import readDM, cosine_similarity, neighbours
import sys

fasttext_vecs="./data/fasttext-wiki-news-300d-20000.txt"
vectors = readDM(fasttext_vecs)


print("\nQUESTION: Which other adjectives are related to brilliance, and how many are more male than female?\n\n")

ns_brilliant = neighbours(vectors,"brilliant",20)
male_bias = 0

for ns in ns_brilliant:
    sim_man = cosine_similarity(vectors,ns,"man")
    sim_woman = cosine_similarity(vectors,ns,"woman")
    print(ns,"man",sim_man,"woman",sim_woman)

    diff = sim_man - sim_woman
    if diff > 0.01:
        male_bias+=1

print("MALE BIAS:",male_bias / len(ns_brilliant))
