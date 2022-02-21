# Movie recommender

<p style='text-align: justify;'>The movie recommender is based on the Collaborative Filtering approach, and creates predictions for movie ratings with Matrix Factorization technique, more precisely, the SVD (Singular Value Decomposition) algorythm of <a href="https://surprise.readthedocs.io/en/stable/" target="_blank">SurPRISE library</a>. Trained on 'small' dataset of <a href="https://grouplens.org/datasets/movielens/" target="_blank">MovieLens</a>. </p> 

<p align="justify">It is <a href="https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app" target="_blank">deployed with Streamlit</a> and can be found here:<p>

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/orosz-attila/movie-recommender/main) 
    
<p style='text-align: justify;'>The notebook for creating the recommendation model is also available on <a href="https://colab.research.google.com/drive/1hqZ6X0jy_CcB1tlPvQHUcGcFvkryhkZK" target="_blank">Jupyter Colab</a>. (Comparing NMF and SVD algorythms and tuning parameters with Gridsearch, cross validation with RMSE and MAE scores.)</p>

 ## Description 

<ol >
    <li style='text-align: justify;'>streamlit_app.py: contains the codes which runs on Streamlit</li>
    <li style='text-align: justify;'>functions_svd.py: contains the codes of all the functions for data transformation and the function for recommendation using the SVD algorythm of SurPRISE</li>
    <li style='text-align: justify;'>config.py: contains the codes for CSS and HTML customization</li>
</ol>

## Requirements / Installation 

surprise==0.1

<p style='text-align: justify;'>For local installation, follow the steps described in the <a href="http://surpriselib.com/" target="_blank">surPRISE documentation</a>. </p>  

With pip (you’ll need numpy, and a C compiler. Windows users might prefer using conda):

    $ pip install numpy
    $ pip install scikit-surprise

With conda (after creating a new environment):

    $ conda install -c conda-forge scikit-surprise

## How to use it? 

Select a movie from the dropdown menu and rate it on a scale from 1 to 5. Add at least 10 movies to your list, finally hit 'Recommend' below: 

https://user-images.githubusercontent.com/89396215/154991104-fc451eea-d8eb-4489-af85-b5b7b7c51ddb.mov

https://user-images.githubusercontent.com/89396215/154570563-e80c6bd9-759e-43ed-ae83-81e8727a1dd3.mov


## Data and other sources
<ul >
    <li style='text-align: justify;'>Movies and ratings data: <a href="https://grouplens.org/datasets/movielens/" target="_blank">MovieLens small database</a> - 100,000 ratings and 3,600 tag applications applied to 9,000 movies by 600 users. Last updated 9/2018.</li>
    <li style='text-align: justify;'>Gifs: <a href="https://iwdrm.tumblr.com/" target="_blank">IWDRM</a></li>
    <li style='text-align: justify;'>Page Icon: <a href="https://www.veryicon.com/icons/system/alphabet/letter-r.html" target="_blank"> Steven Ansell</a></li>
</ul>


 ## Changelog
 - 02-02-22: v1.0 Uploaded  
 - 17-02-22: v1.1 Deployed with Streamlit
 - 21-02-22: v1.1 Updates:
    - config.toml added: dark theme set as default 
    - recommendation function corrected 
    - readme finalized
    - colab notebook finalized

 ## Further developments

<ul >
    <li style='text-align: justify;'>Developing a Hybrid recommender with combining it with a Content-based filtering algorythm</li>
    <li style='text-align: justify;'>Connecting app to an SQL database</li>
    <li style='text-align: justify;'>Adding option of signing-up/logging-in into user account</li>
    <li style='text-align: justify;'>Adding option to save the list of rated movies in the user account</li>
</ul>

 ## License 
<p style='text-align: justify;'>Code of this app is created by Attila Orosz and completely open access under the <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank">Creative Commons BY license</a>. You have the permission to use, distribute, and reproduce these in any medium, provided the source and authors are credited.</p> 
