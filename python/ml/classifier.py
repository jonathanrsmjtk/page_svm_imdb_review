import re
import sys

train = []
for line in open('/Volumes/Hard Disk/programming/page_svm_imdb_review/aclImdb/movie_data/full_train.txt', 'r'):
    train.append(line.strip())
    
test = []
for line in open('/Volumes/Hard Disk/programming/page_svm_imdb_review/aclImdb/movie_data/full_test.txt', 'r'):
    test.append(line.strip())
    
#Preprocess data. Source: Aaron Kub
REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

def preprocess(data):
    data = [REPLACE_NO_SPACE.sub("", line.lower()) for line in data]
    data = [REPLACE_WITH_SPACE.sub(" ", line) for line in data]
    
    return data

train = preprocess(train)
test = preprocess(test)

from nltk.corpus import stopwords

english_stop_words = stopwords.words('english')
def stopwords_removal(corpus):
    removed_stop_words = []
    for review in corpus:
        removed_stop_words.append(
            ' '.join([word for word in review.split() 
                      if word not in english_stop_words])
        )
    return removed_stop_words

no_stop_words = stopwords_removal(train)

def stem_text(corpus):
    from nltk.stem.porter import PorterStemmer
    stemmer = PorterStemmer()
    return [' '.join([stemmer.stem(word) for word in review.split()]) for review in corpus]

stemmed_reviews = stem_text(train)

def lemmatize_text(corpus):
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    return [' '.join([lemmatizer.lemmatize(word) for word in review.split()]) for review in corpus]

lemmatized_reviews = lemmatize_text(train)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC

target = [1 if i < 12500 else 0 for i in range(25000)]

stop_words = ['in', 'of', 'at', 'a', 'the']
ngram_vectorizer = CountVectorizer(binary=True, ngram_range=(1, 3), stop_words=stop_words)
ngram_vectorizer.fit(train)
X = ngram_vectorizer.transform(train)
X_test = ngram_vectorizer.transform(test)

X_train, X_val, y_train, y_val = train_test_split(
    X, target, train_size = 0.75
)

for c in [0.001, 0.005, 0.01, 0.05, 0.1]:
    
    svm = LinearSVC(C=c)
    svm.fit(X_train, y_train)
    print ("Accuracy for C=%s: %s" 
           % (c, accuracy_score(y_val, svm.predict(X_val))))
    
# Accuracy for C=0.001: 0.88784
# Accuracy for C=0.005: 0.89456
# Accuracy for C=0.01: 0.89376
# Accuracy for C=0.05: 0.89264
# Accuracy for C=0.1: 0.8928
    
final = LinearSVC(C=0.01)
final.fit(X, target)
print ("Final Accuracy: %s" 
       % accuracy_score(target, final.predict(X_test)))

# Final Accuracy: 0.90064