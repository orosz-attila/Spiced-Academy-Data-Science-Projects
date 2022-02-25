<p align="center">
  <img src="https://user-images.githubusercontent.com/89396215/148706672-089e1b21-75b3-43a9-b8e4-85428337f7b8.png"/>
</p>


<div align="justify">This repository contains the projects I completed during a Data Science Bootcamp at SPICED Academy from September to December 2021. These are not finalized versions, yet. I am continously refactoring, correcting and updating the codes.</div>

## 01. Visual Data Analysis - Animated Scatterplot

<div align="justify">This animated scatterplot visualizes the changes of countries' fertility rate, life expectancy and population between 1960 and 2015. The sizes of the scatters represents the population of each country, the colours shows in which continent they can be found.</div><br>

The notebook with detailed comments and plotly interactivy is also available on [Jupyter Colab](https://colab.research.google.com/drive/1lzhl7rgZrw2-1RxhsBOEjXzb86fvKp2n).<br>

Data source: [Gapminder Foundation](https://www.gapminder.org/data/).<br>

![animation](https://raw.githubusercontent.com/orosz-attila/Spiced-Academy-Data-Science-Projects/master/01_visual_data_analysis_animated_scatterplot/images/animation.gif)

## 02. Supervised Machine Learning: Classification - Kaggle's Titanic Challenge

<div align="justify"> The goal of this project was to built a machine learning model to predict the survival of Titanic passenger based on the features in the dataset of Kaggle's "Titanic - Machine Learning from Disaster".</div><br> 

<div align="justify">Based on the Exploratory Data Analysis (plotted missing values and the correlation between survival and the different data categories) selected the most significant features and dropped the ones which cannot contribute to accurate prediction. In feature engineering using ColumnTransformer, I applied 1) OneHotEncoder: to convert categorical variables into binary features, 2) SimpleImputer: to fill missing values and 3) MinMaxScaler: to normalize continous numerical variable in range 0.0 - 1.0. The data was trained on Scikit-learn's LogisticRegression and RandomForestClassifier models. After evaluating different model's accuracy scores and cross validation, I kept the LogisticRegression model for prediction (cross validation: mean accuracy score 81.28 +- 3.98 %).</div><br> 

The notebook of this project is available [here](https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/blob/master/02_classification_titanic_challange/2.%20Classification%20-%20Titanic%20ML%20Challenge%20.ipynb).

Data source: [Kaggle: Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic/overview).<br>


## 03. Supervised Machine Learning: Regression - Bicycle Rental Forecast

<div align="justify">The goal of this project is to predict/forecast the total number of rented bycicles for each hour based on time and weather features, optimizing the accuracy of the model for RMSLE, using Kaggle's "Bike Sharing Demand" dataset that provides hourly rental data spanning two years.</div><br>  

Data source: [Kaggle: Bike Sharing Demand](https://www.kaggle.com/c/bike-sharing-demand/data).<br>

## 10. Recommender systems - Movie Recommender with Collaborative Filtering

<div align="justify">The movie recommender is based on the Collaborative Filtering approach, and creates predictions for movie ratings with Matrix Factorization technique, more precisely, the SVD (Singular Value Decomposition) algorythm of the <a href="https://surprise.readthedocs.io/en/stable/" target="_blank">SurPRISE library</a>. It is trained on 'small' dataset of <a href="https://grouplens.org/datasets/movielens/" target="_blank">MovieLens</a>.</div><br> 

<p align="justify">The online user-interface is built and <a href="https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app" target="_blank">deployed with Streamlit</a> and can be found here:<p>

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/orosz-attila/movie-recommender/main) 
    
<div align="justify">My notebook for creating the recommendation model is also available on <a href="https://colab.research.google.com/drive/1hqZ6X0jy_CcB1tlPvQHUcGcFvkryhkZK" target="_blank">Jupyter Colab</a>. (Comparing NMF and SVD algorythms and tuning parameters with Gridsearch, cross validation with RMSE and MAE scores.)</div><br> 


<p align="justify">A separate repository with updates is available <a href="https://github.com/orosz-attila/Movie-Recommender" target="_blank">here</a>.</p>


https://user-images.githubusercontent.com/89396215/154991104-fc451eea-d8eb-4489-af85-b5b7b7c51ddb.mov


https://user-images.githubusercontent.com/89396215/154570563-e80c6bd9-759e-43ed-ae83-81e8727a1dd3.mov

<br>

## 12. Final Project - Covid-19 Dashboard

<p align="justify">Interactive dashboard with daily update displaying 23 Covid-19 related data categories on plotly map and charts. According to the user selection criteria, the daily data can be displayed on a scatter world map, the trends of country data in line- and barcharts, with the option of comparing countries in multiple data categories.</p>

<p align="justify">The dashboard is <a href="https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app" target="_blank">deployed with Streamlit</a> and can be found here:<p>

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/orosz-attila/covid-19-dashboard) 

<p align="justify">A separate repository with updates is available <a href="https://github.com/orosz-attila/Covid-19-Dashboard" target="_blank">here</a>.</p>

<p align="justify">The notebook of this dashboard project with detailed comments is also available on <a href="https://colab.research.google.com/drive/1StLDRJ7LVoPS10AULBxVOJo8rDqnt3U8" target="_blank">Jupyter Colab</a>.</p>

https://user-images.githubusercontent.com/89396215/154562196-b325952a-d5ba-460e-94f4-ae3114455fe6.mov


https://user-images.githubusercontent.com/89396215/154564184-e39a2c74-825c-4063-b4c1-04924abe5c84.mov


https://user-images.githubusercontent.com/89396215/154564189-415b9fff-b6e9-4265-891c-bf9808465435.mov
