<p align="center">
  <img src="https://user-images.githubusercontent.com/89396215/148706672-089e1b21-75b3-43a9-b8e4-85428337f7b8.png"/>
</p>

<div align="justify">This repository contains the projects I completed during a Data Science Bootcamp at SPICED Academy in Berlin from September to December 2021.</div>
<br>

## 01. Visual Data Analysis - Animated Scatterplot

<div align="justify">This animated scatterplot visualizes the changes of countries' fertility rate, life expectancy and population between 1960 and 2015. The sizes of the scatters represents the population of each country, the colours shows in which continent they can be found.</div><br>

The notebook with detailed comments and plotly interactivity is also available on [Jupyter Colab](https://colab.research.google.com/drive/1lzhl7rgZrw2-1RxhsBOEjXzb86fvKp2n).<br>

Data source: [Gapminder Foundation](https://www.gapminder.org/data/).<br>

![animation](https://raw.githubusercontent.com/orosz-attila/Spiced-Academy-Data-Science-Projects/master/01_visual_data_analysis_animated_scatterplot/images/animation.gif)

## 02. Supervised Machine Learning: Classification - Kaggle's Titanic Challenge

<div align="justify"> The goal of this project was to built a machine learning model to predict the survival of Titanic passenger based on the features in the dataset of Kaggle's "Titanic - Machine Learning from Disaster".</div><br> 

<div align="justify">Based on the Exploratory Data Analysis (plotted missing values and the correlation between survival and the different data categories) selected the most significant features and dropped the ones which cannot contribute to accurate prediction. In feature engineering using ColumnTransformer, I applied 1) OneHotEncoder: to convert categorical variables into binary features, 2) SimpleImputer: to fill missing values and 3) MinMaxScaler: to normalize continous numerical variable in range 0.0 - 1.0. The data was trained on Scikit-learn's LogisticRegression and RandomForestClassifier models. After evaluating different model's accuracy scores and cross validation, I kept the LogisticRegression model for prediction (cross validation: mean accuracy score 81.28 +- 3.98 %).</div><br> 

The notebook of this project is available [here](https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/blob/master/02_classification_titanic_challange/2.%20Classification%20-%20Titanic%20ML%20Challenge%20.ipynb).

Data source: [Kaggle: Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic/overview).<br>
<br>

## 03. Supervised Machine Learning: Regression - Bicycle Rental Forecast

<div align="justify">The goal of this project was to build a regression model, in order to predict the total number of rented bycicles in each hour based on time and weather features, optimizing the accuracy of the model for RMSLE, using Kaggle's "Bike Sharing Demand" dataset that provides hourly rental data spanning two years.</div><br> 

<div align="justify">After extracting datetime features, some highly correlated variables were dropped via feature selection (correlation analysis, Variance Inflation Factor) to avoid multicollienarity. I compared more linear regression models with one another (PossionRegressor, PolinomialFeatures, Lasso, Ridge, RandomForestRegressor) based on R2 and RMSLE scores. After evaluating the different models, I kept the RandomForestRegressor, and applied GridSearchCV and cross validation to ensure the best fit, finally submitted the predictions with 0.47210 RMSLE.</div><br>

The notebook of this project is available [here](https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/blob/master/03_regression_bycicle_rental_prediction/03_project_bycicle_rental_forecast.ipynb).
<br>

Data source: [Kaggle: Bike Sharing Demand](https://www.kaggle.com/c/bike-sharing-demand/data).<br>
<br>

## 04. Natural Language Processing (NLP): Text Classification

<div align="justify">The main goal of this project was to build a text classification model on song lyrics to predict the artist from a piece of text, additionally, to make user-inputs (artists, lyrics) possible in CLI.</div><br> 

<div align="justify">Through web scraping with BeautifulSoup, the song-lyrics of selected artists are extracted from lyrics.com. During the text pre-processing, word-tokenizer and word-lemmatizer of Natural Language Toolkit (NLTK) is used to "clean" the extracted texts and create the corpus: 1) TreebankWordTokenizer() splits the text into list of words and removes all other punctuation marks, 2) WordNetLemmatizer() reverts words back to their root/base. These steps are required to import and download lexical database such as WordNet. WordNet's Stopwords also removes the most common English words from the corpus. </div><br>
 
<div align="justify">In the model pipeline, Tfidfvectorizer (TF-IDF) transforms the words of the corpus into a matrix, count-vectorizes and normalizes them at once by default. For classification, the multinomial Naive Bayes classifier MultinomialNB() was used which is suitable for classification with discrete features like word counts for text classification.</div><br>

2 versions of this project can be found [here](https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/tree/master/04_nlp_text_classification).

![animation](https://raw.githubusercontent.com/orosz-attila/Spiced-Academy-Data-Science-Projects/master/04_nlp_text_classification/text_classification.gif)<br>
<br>

## 05. Dashboard (SQL, Cloud Computing)

Coming soon...
 

## 06. The Data Pipeline: Tweets Sentiment Analysis


<p align="center">
  <img src="https://raw.githubusercontent.com/orosz-attila/Spiced-Academy-Data-Science-Projects/master/06_data_pipeline_tweets_sentiment_analysis/structure.svg"/>
</p>


<div align="justify">The challenge of this Data Engineering project was to build a Dockerized Data Pipeline to analyze the sentiment of tweets. At first, using Tweepy API, tweets are collected in a selected topic and stored in a MondoDB database (tweet_collector). Next, the sentiment of tweets is analyzed and the tweets with the scores are stored in a Postgres database (ETL_job). Finally, tweets with sentiment score are published on a Slack channel. (slack_bot)</div><br>

<div align="justify">For the sentiment analysis, SentimentIntensityAnalyzer() of the the Vader library  (Valence Aware Dictionary and sEntiment Reasoner) was used.</div><br>

The folder of this project can be found [here](https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/tree/master/06_data_pipeline_tweets_sentiment_analysis).<br>
<br>

## 07. Time Series Analysis: Temperature Forecast

<div align="justify">In this project, I applied the ARIMA model for a short-term temperature forecast. After visualizing the trend, the seasonality and the remainder of the time series data (daily mean temperature in Berlin-Treptow from 1979-2020), I run tests such as ADF and KPSS for checking stationarity (time dependence).</div><br> 

<div align="justify">For determining the parameters of the ARIMA model (p, d, q), I present two approaches:</div><br> 

  1. Inspecting the lags of the Autocorrelation (ACF) and Partial Auto Correlation Functions (PACF) plots. 
  2. Using alkaline-ml Auto-Arima process which automatically finds the most optimal order setting that has the lowest AIK. 

<div align="justify">The prediction with the tuned ARIMA model achieved a MAE score as low as 1.72.</div><br>

The notebook with plotly interactivity is also available on [Jupyter Colab](https://colab.research.google.com/drive/1nRPrfqCVFn-EHhl5GenxREuNRYeWV_h8#scrollTo=PynGYIu55aHb).<br>


Data source: [European Climate Assessment Dataset](https://www.ecad.eu).<br>
<br>

## 08. Markov Chain Monte Carlo (MCMC): Predicting and simulating customer behaviour in a supermarket.

<div align="justify">The goal of this project was to predict and visualize customer behaviour between departments/aisles in a supermarket, applying Markov Chain modeling and Monte-Carlo simulation.</div><br>

The project included the following tasks:

1. Data Analysis
2. Calculating Transition Probabilities between the aisles
3. Implementing a Customer Class
4. Running MCMC (Markov-Chain Monte-Carlo) simulation for a single class customer 
5. Extending the simulation to multiple customers
6. Animation/Visualization

The folder of this project can be found [here](https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/tree/master/08_mcmc_predicting_customer_behaviour).<br>

## 09. Deep Learning - Artificial Neural Network

<div align="justify">The goal of this project was to build an Artificial Neural Network that recognizes objects on images made by the webcam:  </div><br>

The project included the following tasks:

1. Implementing a Feed-Forward Neural Network
2. Backpropagation from Scratch
3. Building Neural Network with Keras
4. Training Strategies / Hyperparameters of Neural Networks
5. Convolutional Neural Networks (CNN) 
6. Classifying images made with webcam with Pre-trained Networks (Comparing MobileNetV2, InceptionV3)
7. Image Detection 

The folder of this project can be found [here](https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/tree/master/09_deep_learning).<br>


## 10. Recommender systems - Movie Recommender with Collaborative Filtering

<div align="justify">The movie recommender is based on the Collaborative Filtering approach, and creates predictions for movie ratings with Matrix Factorization technique, more precisely, the SVD (Singular Value Decomposition) algorythm of the <a href="https://surprise.readthedocs.io/en/stable/" target="_blank">SurPRISE library</a>. It is trained on 'small' dataset of <a href="https://grouplens.org/datasets/movielens/" target="_blank">MovieLens</a>.</div><br> 

<p align="justify">The online user-interface is built and <a href="https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app" target="_blank">deployed with Streamlit</a> and can be found here:<p>

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/orosz-attila/movie-recommender/main) 
    
<div align="justify">My notebook for creating the recommendation model is also available on <a href="https://colab.research.google.com/drive/1hqZ6X0jy_CcB1tlPvQHUcGcFvkryhkZK" target="_blank">Jupyter Colab</a>. (Comparing NMF and SVD algorythms and tuning parameters with Gridsearch, cross validation with RMSE and MAE scores.)</div><br> 


<p align="justify">A separate repository with updates is available <a href="https://github.com/orosz-attila/Movie-Recommender" target="_blank">here</a>.</p>


https://user-images.githubusercontent.com/89396215/154991104-fc451eea-d8eb-4489-af85-b5b7b7c51ddb.mov


https://user-images.githubusercontent.com/89396215/154570563-e80c6bd9-759e-43ed-ae83-81e8727a1dd3.mov

<br>

## 11. Software Engineering

...coming soon


## 12. Final Project - Covid-19 Dashboard

<p align="justify">Interactive dashboard with daily update displaying 23 Covid-19 related data categories on plotly map and charts. According to the user selection criteria, the daily data can be displayed on a scatter world map, the trends of country data in line- and barcharts, with the option of comparing countries in multiple data categories.</p>

<p align="justify">The dashboard is <a href="https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app" target="_blank">deployed with Streamlit</a> and can be found here:<p>

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/orosz-attila/covid-19-dashboard) 

<p align="justify">A separate repository with updates is available <a href="https://github.com/orosz-attila/Covid-19-Dashboard" target="_blank">here</a>.</p>

<p align="justify">The notebook of this dashboard project with detailed comments is also available on <a href="https://colab.research.google.com/drive/1StLDRJ7LVoPS10AULBxVOJo8rDqnt3U8" target="_blank">Jupyter Colab</a>.</p>

https://user-images.githubusercontent.com/89396215/154562196-b325952a-d5ba-460e-94f4-ae3114455fe6.mov


https://user-images.githubusercontent.com/89396215/154564184-e39a2c74-825c-4063-b4c1-04924abe5c84.mov


https://user-images.githubusercontent.com/89396215/154564189-415b9fff-b6e9-4265-891c-bf9808465435.mov
