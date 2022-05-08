from utils import read_external_vectors, compute_cosines, compute_nearest_neighbours

fasttext_vecs="./data/fasttext-wiki-news-300d-20000.txt"
print("Reading vectors...")
m, vocab = read_external_vectors(fasttext_vecs)
cosines = compute_cosines(m)

# EXAMPLE CODE

# Compute nearest neighbours of a word
word = 'man'
word_idx = vocab.index(word)
neighbours = compute_nearest_neighbours(cosines, word_idx, 20, vocab)
print(neighbours)


# Compute similarity between two words
word1 = 'man'
word2 = 'woman'
print("Similarity",word1,word2,cosines[vocab.index(word1)][vocab.index(word2)])


# Compute difference vector and project adjective onto it (see Bolukbasi paper)
word1 = 'brilliant'
word2 = 'pretty'
diff = m[vocab.index('woman')] - m[vocab.index('man')] #femaleness
print("Projection of",word1,"onto difference vector:",m[vocab.index(word1)].dot(diff))
print("Projection of",word2,"onto difference vector:",m[vocab.index(word2)].dot(diff))



# QUESTIONS

print("\nQUESTION: Which adjectives are related to brilliance, and do they tend to be more male than female?\n\n")
#Insert your code here

print("\nQUESTION: How would you show the indirect bias investigated by Leslie and colleague using your findings about brilliance adjectives?\n\n")
#Insert your code here

print("\nQUESTION: Try other terms to compute the difference vector. Is the specific choice of words important?\n\n")
#Insert your code here

print("\nQUESTION: Which other biases could you investigate using the same technique? Give an example.\n\n")
#Insert your code here
