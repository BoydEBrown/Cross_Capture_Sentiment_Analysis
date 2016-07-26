from sklearn.feature_extraction.text import CountVectorizer


def tf_idf(data):
    # Initialize CountVectorizer.
    vectorizer = CountVectorizer(stop_words='english')
    #  Learn the vocabulary dictionary and return term-document matrix.
    sparse_matrix = vectorizer.fit_transform(data)


if __name__ == '__main__':
    pass
