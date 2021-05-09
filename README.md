# Biases in semantic spaces

Distributional Semantics Models (DSMs) reproduce whichever biases are to be found in the data they are trained on. Techniques exist to try and ensure that such biases are not amplified by the learning algorithm, or even to try and remove the bias from the learnt representations. In order to use such algorithms, however, we need to know *where* the biases are to be found. Obvious candidates are semantic subspaces *directly* related to gender, race or disability. But what else?

We are going to look at professions and the kind of attributes associated with them. [Sarah-Jane Leslie and colleagues](https://www.princeton.edu/~sjleslie/expectations%20of%20brilliance.pdf) have shown in a study that philosophy as a profession is strongly associated with particular innate qualities such as being 'talented' and 'sophisticated', and much less with simple dedication and hard work. Such qualities, in turn, are more associated with men than women in standard discourse, leading to fewer women pursuing a philosophical career. This is an example of an indirect bias. Can we find evidence of such indirect biases in vector spaces?


## The data and code

In the *data/* directory, you will find 20,000 vectors from the much larger set released [here](https://fasttext.cc/docs/en/english-vectors.html) (FastText system). Those are 300-dimensional vectors trained on Wikipedia and very large news corpora (16B words). 

You have a small code stub in *explorer.py*, showing you how to load the data and how to perform cosine similarity and nearest neighbours calculations over the semantic space, and allowing you to explore t he data. 

You are to use the stub to perform some simple investigation of your choice on the data. A small example is included in *example-question.py* to get you started.



