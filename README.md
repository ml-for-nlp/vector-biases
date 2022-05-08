# Biases in semantic spaces

Distributional Semantics Models (DSMs) reproduce whichever biases are to be found in the data they are trained on. Techniques exist to try and ensure that such biases are not amplified by the learning algorithm, or even to try and remove the bias from the learnt representations. In order to use such algorithms, however, we need to know *where* the biases are to be found. Obvious candidates are semantic subspaces *directly* related to gender, race or disability. But what else?

We are going to look at professions and the kind of attributes associated with them. [Sarah-Jane Leslie and colleagues](https://www.princeton.edu/~sjleslie/expectations%20of%20brilliance.pdf) have shown in a study that philosophy as a profession is strongly associated with particular innate qualities such as being 'talented' and 'sophisticated', and much less with simple dedication and hard work. Such qualities, in turn, are more associated with men than women in standard discourse, leading to fewer women pursuing a philosophical career. This is an example of an indirect bias. Can we find evidence of such indirect biases in vector spaces?


## The data and code

In the *data/* directory, you will find 20,000 vectors from the much larger set released [here](https://fasttext.cc/docs/en/english-vectors.html) (FastText system). Those are 300-dimensional vectors trained on Wikipedia and very large news corpora (16B words). 

You have a small code stub in *bias.py*, showing you how to load the data and how to perform cosine similarity and nearest neighbours calculations over the semantic space. It also implements the idea from [Bolukbasi and colleagues](https://arxiv.org/abs/1607.06520) that a dimension of difference can be computed for a certain protected attribute (e.g. gender), and other terms projected onto it to understand their bias.



## The questions

Using the code stub at your disposal, try and answer the following questions:

* Which adjectives are related to brilliance, and do they tend to be more male than female?

* How would you show the indirect bias investigated by Leslie and colleague using your findings about brilliance adjectives?

* Try other terms to compute the difference vector. Is the specific choice of words important?

* Which other biases could you investigate using the same technique? Give an example. 

