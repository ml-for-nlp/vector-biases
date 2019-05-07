from utils import readDM, cosine_similarity, neighbours
import sys

fasttext_vecs="./data/fasttext-wiki-news-300d-20000.txt"
print("Reading vectors...")
vectors = readDM(fasttext_vecs)

profession = "philosopher"
attribute = "brilliant"

ns_prof = neighbours(vectors,profession,50)
print(ns_prof)
ns_att = neighbours(vectors,attribute,50)
print(ns_att)

print(cosine_similarity(vectors,profession,attribute))
