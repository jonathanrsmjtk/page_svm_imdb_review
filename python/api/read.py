
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Volumes/Hard Disk/Programming/page_svm_imdb_review/app/python/ml/')

from model_call import classify
import schemas

#Read post opinion to classify and call model file as classifier

def check_tweet_sentiment(tweets: schemas.TweetClassify):
    sentiment_res = classify(tweets.data)
    if sentiment_res == 0:
        sentiment_res = "Negative"
    elif sentiment_res == 1:
        sentiment_res = "Positive"
    return {'data':tweets.data, 'sentiment':sentiment_res}



