import pickle
# import classifier as cl

filename = '/Volumes/Hard Disk/Programming/page_svm_imdb_review/app/python/model/model.ml'
infile = open(filename, 'rb')
model = pickle.load(infile)
infile.close()

filename = '/Volumes/Hard Disk/Programming/page_svm_imdb_review/app/python/model/ngram.ml'

infile = open(filename, 'rb')
ngram_vectorizer = pickle.load(infile)
infile.close()

def classify(data):
    test_array = []
    test_array.append(data)
    test_array = ngram_vectorizer.transform(test_array)
    
    result = model.predict(test_array)
    return (result[0])

