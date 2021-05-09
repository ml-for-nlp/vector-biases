from utils import readDM, cosine_similarity, neighbours
import sys

fasttext_vecs="./data/fasttext-wiki-news-300d-20000.txt"
print("Reading vectors...")
vectors = readDM(fasttext_vecs)


"""Explore the vector space"""

f = ""

while f != 'q':
    f = input("\nWhat would you like to do? (n = nearest neighbours, s=similarity, q=quit) ")

    while f == 'n':
        w = input("Enter a word or 'x' to exit nearest neighbours: ")

        if w == 'x':
            f = 'x'
        else:
            ns = neighbours(vectors,w,20)
            print(ns)

    while f == 's':
        w = input("Input two words separated by a space or 'x' to exit similarity: ")
        
        if w == 'x':
            f = 'x'
        else:
            w1,w2 = w.split()
            if w1 in vectors and w2 in vectors:
                sim = cosine_similarity(vectors,w1,w2)
                print("SIM",w1,w2,sim)
            else:
                print("Word(s) not found in space.")

