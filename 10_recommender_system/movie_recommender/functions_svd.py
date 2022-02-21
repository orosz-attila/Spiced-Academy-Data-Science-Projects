import streamlit as st
import os
import pandas as pd
import numpy as np

from surprise import SVD
from surprise import Dataset, Reader


PATH = os.path.abspath('')


@st.cache(show_spinner=False)
def load_ratings():
    '''This function loads the ratings dataset into dataframe and returns it'''
    df_ratings = pd.read_csv(PATH + os.sep + 'data/ratings.csv')
    return df_ratings


@st.cache(show_spinner=False)
def load_movies():
    '''This function loads the movies dataset into dataframe and returns it'''
    df_movies = pd.read_csv(PATH + os.sep + 'data/movies.csv')
    df_movies.drop_duplicates(subset="title", keep='first', inplace=True)
    return df_movies


@st.cache(show_spinner=False, allow_output_mutation=True)
def merge_df(df_ratings, df_movies):
    '''
    This function merges ratings and movies dataset and drops the columns we dont need for the model
    Parameters: ratings dataframe, movies dataframe
    Returns: merged dataframe
    '''
    df_merged = pd.merge(df_movies, df_ratings, on='movieId', how='right')
    df_merged.drop(columns=['timestamp', 'genres', 'movieId'], inplace=True)
    df_merged = df_merged[['userId', 'title', 'rating']] 
    return df_merged 


@st.cache(show_spinner=False, allow_output_mutation=True)
def drop_movies(df_merged):
    '''
    This function drops movies under 15 reviews
    Parameter: merged dataframe
    Returns: merged dataframe over 15 reviews
    '''
    df_merged['reviews'] = df_merged.groupby(['title'])['rating'].transform('count')
    df_merged = df_merged[df_merged.reviews > 15][['userId', 'title', 'rating']]
    return df_merged


@st.cache(show_spinner=False, allow_output_mutation=True)
def get_movies_list(df_merged):
    '''
    This function creates a list of movies for submit form.
    Parameter: merged dataframe
    Returns: movies list
    '''
    df_drop = df_merged[df_merged['title'].isna()]
    df_dropped = df_merged.drop(df_drop.index, axis=0)
    df_sorted = df_dropped.sort_values(by=['title'], ascending=True)
    movies_list = df_sorted['title'].unique().tolist()
    movies_list = [''] + movies_list
    return movies_list


def insert_input(df_user, movie_select, rating_select): 
    '''
    This function appends movie and rating added by the user in the sidebar submit form to the user dataframe.
    Parameters: user dataframe (with streamlit session.state), movie, rating
    Returns: dataframe containing all movies and ratings added by the user in the sidebar form.
    '''
    df_new_row = pd.DataFrame([[movie_select, rating_select]],  columns=['title', 'rating'])
    df_user = pd.concat([df_user, df_new_row], axis=0, ignore_index=True)
    df_user.index = df_user.index + 1
    return df_user

    # # df_user = df_user.append({'title': movie_select, 'rating': rating_select}, ignore_index=True)
    # df_user.index = df_user.index + 1
    # return df_user


def remove_last(df_user):
    '''
    This function deletes the last row in the dataframe containing all movies and ratings added by the user in the sidebar form.
    Parameter: user dataframe (with streamlit session.state)
    Return: user dataframe (with streamlit session.state)
    '''
    df_user.drop(df_user.tail(1).index, inplace=True)
    return df_user


def svd_recommender(df_user, df_merged): 
    ''' 
    Recommendation model: 
    Predicts the ratings of the not selected movies for the user and calculates the percentage of matching. 
    Using sklearn-surprise SVD model.  
    Parameters: user dataframe (with streamlit session.state), merged dataframe.
    Returns: dataframe of recommendations with columns: match (%), title. (sorted by match (%))
    '''
    # combining dfs
    df = df_user.copy()
    df['userId'] = 611
    df = df[['userId', 'title', 'rating']]
    df_combined = pd.concat([df_merged, df], axis=0)

    # loading sklearn-surpise reader and data 
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df_combined, reader)

    # movies to predict
    unique_title = df_combined['title'].unique()
    df_user_titles = df_combined.loc[df_combined['userId']==611, 'title']
    movies_to_predict = np.setdiff1d(unique_title, df_user_titles)

    # instantiate and fit model
    algo_svd = SVD(n_factors=110, n_epochs=30)
    algo_svd.fit(data.build_full_trainset())

    # recommendations 
    recommendations_svd = []
    for title in movies_to_predict:
        recommendations_svd.append((title, algo_svd.predict(uid=611,iid=title).est))
    df_recommendation = pd.DataFrame(recommendations_svd, columns=['title', 'predictions']).sort_values('predictions', ascending=False)


    # match % set to index, 
    df_recommendation.rename(columns={'predictions': 'match (%)'}, inplace=True)
    df_recommendation['match (%)'] = df_recommendation['match (%)'] * 20
    df_recommendation['match (%)'] = df_recommendation['match (%)'].astype(int)
    df_recommendation['match (%)'] = df_recommendation['match (%)'].astype(str) + ' %'
    df_recommendation.set_index('match (%)', inplace=True)

    return df_recommendation

if __name__ == "__main__":
    pass  