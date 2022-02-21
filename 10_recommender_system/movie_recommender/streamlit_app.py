import streamlit as st
import functions_svd as fn
import config as cf
import pandas as pd
import time 


# permanent css and html configurations 
cf.page_config()
cf.sidebar()
cf.header_1()
cf.header_2()
cf.dropdown()
cf.select_box()
cf.column_buttons()
cf.warning()
cf.warning_margin()
cf.alert_color()
cf.spinner()
cf.footer()


# initializing session state variable for the url of first background 
if 'url' not in st.session_state: 
    st.session_state.url = 'https://64.media.tumblr.com/e143caf373a57a149f7d0ce7d4d461e2/tumblr_ldsq207kj41qe0eclo2_r1_500.gifv'

# rendering background with initial url 
cf.background(st.session_state.url)


# initializing session state for the empty dataframe for user inputs
if 'df_user' not in st.session_state: 
    st.session_state.df_user = pd.DataFrame(columns = ['title', 'rating'])


# initializing session state for 'Delete last entry' button
if 'delete' not in st.session_state:
    st.session_state.delete = 0

def set_delete():
    '''
    Callback function for 'Delete last entry' button. 
    On_click it sets the session.state to 1 that triggers the execution of the codes for this button.
    '''
    st.session_state.delete = 1
    return st.session_state.delete


# initializing session state variable for 'Recommend' button
if 'recommend' not in st.session_state:
    st.session_state.recommend = 0

def set_recommend():
    '''
    Callback function for 'Recommend' button. 
    On_click it sets the session.state to 1 that triggers the execution of the codes for this button.
    '''
    st.session_state.recommend = 1
    return st.session_state.recommend


# initializing session state variable for 'Add_more_movies' button
if 'add_more' not in st.session_state:
    st.session_state.add_more = 0

# on_click callback function for 'Add_more_movies' button
def set_add_more():
    '''
    Callback function for 'Add more movies' button. 
    On_click it sets the session.state to 1 that triggers the execution of the codes for this button.
    '''                                                                                                       
    st.session_state.recommend = 0
    st.session_state.add_more = 1
    return st.session_state.add_more, st.session_state.recommend


# initializing session state variable for restart button
if 'restart' not in st.session_state:
    st.session_state.restart = 0

def set_restart():
    '''
    Callback function for 'Restart' button. 
    On_click it sets the session.state to 1 that triggers the execution of the codes for this button.
    '''  
    st.session_state.recommend = 0
    st.session_state.restart = 1
    return st.session_state.add_more, st.session_state.recommend


# loading and transforming data
df_ratings = fn.load_ratings()
df_movies = fn.load_movies()
df_merged = fn.merge_df(df_ratings, df_movies)
df_merged = fn.drop_movies(df_merged)
movies_list = fn.get_movies_list(df_merged)


# permanent sidebar elements
with st.sidebar:
    title = st.title('REFLUX')
    header1 = st.header('The Movie Recommender') 
    with st.expander("How to use it?"):
        cf.expander_html()
    form = st.form(key="movie_selector", clear_on_submit=True)
    movie_select = form.selectbox('Select / type in a movie title', options=movies_list, index=0)
    rating_select = form.selectbox('Rate this movie ( 5 = best )', ['', 1, 2, 3, 4, 5], index=0)
    add_movie = form.form_submit_button('Add movie')


#if add_movie form_submit_button is clicked on 
if add_movie:
    if not movie_select: 
        cf.background(st.session_state.url)
        st.success('Oops, you did not select a movie!')
        with st.sidebar:
            if st.session_state.df_user.empty == True:
                pass
            else:
                st.write("List of your rated movies:")
                user_ratings = st.dataframe(st.session_state.df_user)
                col1, col2 = st.columns(2)
                with col1:
                    st.button("Delete last entry", key='4', on_click=set_delete)
                with col2:
                    st.button('Recommend', key="1", on_click=set_recommend)       
        st.stop()
    elif not rating_select:
        cf.background(st.session_state.url)
        st.success("Oops, you did not rate the movie!")
        with st.sidebar:
            if st.session_state.df_user.empty == True:
                pass
            else:
                st.write("List of your rated movies:")
                user_ratings = st.dataframe(st.session_state.df_user)
                col1, col2 = st.columns(2)
                with col1:
                    st.button("Delete last entry", key='4', on_click=set_delete)
                with col2:
                    st.button('Recommend', key="1", on_click=set_recommend)   
        st.stop()
    elif movie_select and rating_select:
        st.session_state.url = cf.random_gif()
        cf.background(st.session_state.url)
        st.session_state.df_user = fn.insert_input(st.session_state.df_user, movie_select, rating_select)
        with st.sidebar:
            st.write("List of your rated movies:") 
            user_ratings = st.dataframe(st.session_state.df_user)
            col1, col2 = st.columns(2)
            with col1:
                st.button("Delete last entry", key='4', on_click=set_delete)
            with col2:
                st.button('Recommend', key="1", on_click=set_recommend)


# if 'Delete last row' button is clicked on
if st.session_state.delete == 1:
    if st.session_state.df_user.empty == True:
        st.success("Oops, your list is empty!")
        st.session_state.delete = 0
        with st.sidebar:
            st.write("List of your rated movies:") 
            user_ratings = st.dataframe(st.session_state.df_user)
            col1, col2 = st.columns(2)
            with col1:
                st.button("Delete last entry", key='4', on_click=set_delete)
            with col2:
                st.button('Recommend', key="1", on_click=set_recommend)
    else:            
        cf.background(st.session_state.url)
        st.session_state.delete = 0
        st.session_state.df_user = fn.remove_last(st.session_state.df_user)
        with st.sidebar:
            st.write("List of your rated movies:") 
            user_ratings = st.dataframe(st.session_state.df_user)
            col1, col2 = st.columns(2)
            with col1:
                st.button("Delete last entry", key='4', on_click=set_delete) 
            with col2:
                st.button('Recommend', key="1", on_click=set_recommend)
        with st.spinner('Last entry deleted!'):
            time.sleep(1)
else:
    pass


# if 'Recommend' button is clicked on
if st.session_state.recommend == 1:
    if st.session_state.df_user.empty == True:
        st.success("Oops, your list is empty!")
        st.session_state.recommend = 0
        with st.sidebar:
            st.write("List of your rated movies:") 
            user_ratings = st.dataframe(st.session_state.df_user)
            col1, col2 = st.columns(2)
            with col1:
                st.button("Delete last entry", key='4', on_click=set_delete)
            with col2:
                st.button('Recommend', key="1", on_click=set_recommend)
    else: 
        st.session_state.url = 'https://64.media.tumblr.com/tumblr_lf89wxB3ja1qe0eclo1_r34_500.gifv'
        cf.background(st.session_state.url)
        st.session_state.recommend = 0
        st.session_state.df_user['rating'] = st.session_state.df_user['rating'].astype(int)
        with st.spinner('Please wait, your recommendations are in the oven!'):   
            df_recommended = fn.svd_recommender(st.session_state.df_user, df_merged)
        with st.sidebar:
            st.write("Recommended movies for you:") 
            recommendations = st.dataframe(df_recommended)
            col1, col2 = st.columns(2)
            with col1: 
                st.button('Add more movies', key=2, on_click=set_add_more) 
            with col2:
                st.button("Restart", key=3, on_click=set_restart) 
        with st.spinner('Ready! Check your recommendations!'): 
            time.sleep(2)
        time.sleep(10)
        st.success("Hit 'Add more movies' to continue or 'Restart' to erase your list")
else:
    pass 


# if 'Add_more_movies' button is clicked on
if st.session_state.add_more == 1:
    st.session_state.url = cf.random_gif()
    cf.background(st.session_state.url)
    st.session_state.add_more = 0
    with st.sidebar:
        st.write("List of your rated movies:") 
        user_ratings = st.dataframe(st.session_state.df_user)
        col1, col2 = st.columns(2)
        with col1:
            st.button("Delete last entry", key='4', on_click=set_delete) 
        with col2:
            st.button('Recommend', key="1", on_click=set_recommend)
else:
    pass 


# if 'Restart' button is clicked on
if st.session_state.restart == 1:
    st.session_state.url = 'https://64.media.tumblr.com/38ad849338d5e1eeecfd1880b0497514/tumblr_mh6d6nDLrR1qe0eclo1_r6_500.gifv' 
    cf.background(st.session_state.url)
    st.session_state.restart = 0
    st.session_state.df_user = pd.DataFrame(columns = ['title', 'rating'])
else:
    pass 