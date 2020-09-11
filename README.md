This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Movie Review Sentiment Analyzer on ReactJS

This is the movie review sentiment analyzer on ReactJS. Using Support Vector Machine (SVM) as classifier and N-Gram Vectorizer with highest accuracy of 90% (thanks to [Aaron Kub](https://towardsdatascience.com/sentiment-analysis-with-python-part-1-5ce197074184)), and [FastAPI](https://fastapi.tiangolo.com/) as API framework, Python-based. This project uses IMDB Movie Dataset ([source](http://ai.stanford.edu/~amaas/data/sentiment/)). This page use NPM package - [Axios](https://www.npmjs.com/package/axios) to post API requests.

![Interface](https://raw.githubusercontent.com/jonathanrsmjtk/page_svm_imdb_review/master/Screen%20Shot%202020-09-11%20at%2019.46.35.png)
## How to Unzip
Run this on your terminal after you located on file's directory (or use `cd`):
`gunzip -c aclImdb_v1.tar.gz | tar xopf -
cd aclImdb && mkdir movie_data
for split in train test; do for sentiment in pos neg; do for file in $split/$sentiment/*; do cat $file >> movie_data/full_${split}.txt; echo >> movie_data/full_${split}.txt; done; done; done;` [source: Aaron Kub](https://towardsdatascience.com/sentiment-analysis-with-python-part-1-5ce197074184))

## How to Run
to start this NPM server locally, just do this:
1. Clone and run `npm install` to install all dependencies
2. Run with ReactJS run command:
`npm start`
3. This page will run in `http://localhost:3000`

to start FastAPI server, type this:
`uvicorn python.api.main:app --reload`

in default, FastAPI Uvicorn will run over your localhost in `http://localhost:8000/` or adjust some parameters if you need ([documentation](https://fastapi.tiangolo.com/deployment/)).

If you have some questions, kindly send me mail through jonathanrey18@yahoo.co.id or post your issues above.

