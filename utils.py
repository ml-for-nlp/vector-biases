import numpy as np
from sklearn.decomposition import PCA
from sklearn.metrics import pairwise_distances

def read_external_vectors(vector_file):
    vocab = []
    vectors = []
    with open(vector_file) as f:
        dmlines=f.read().splitlines()
    for l in dmlines:
        items=l.split()
        target = items[0]
        vocab.append(target)
        vec=[float(i) for i in items[1:]]       #list of lists  
        vectors.append(vec)
    m = np.array(vectors)
    return m, vocab


def compute_PCA(m,dim):
    m -= np.mean(m, axis = 0)
    pca = PCA(n_components=dim, svd_solver='arpack')
    pca.fit(m)
    return pca.transform(m)

def compute_cosines(m):
    return 1-pairwise_distances(m, metric="cosine") / 2 #Dividing by 2 to avoid negative values. See https://stackoverflow.com/questions/37454785/how-to-handle-negative-values-of-cosine-similarities


def compute_nearest_neighbours(cosines, word_idx, num_nns, vocab):
    word_cos = np.array(cosines[word_idx])
    ranking = np.argsort(-word_cos)
    neighbours = [(vocab[n], round(word_cos[n],5)) for n in ranking][:num_nns+1]
    return neighbours



