import streamlit as st
import random
import os
PATH = os.path.abspath('')


def page_config():
    st.set_page_config(
        page_title="Movie Recommender",
        layout="centered",
        page_icon = PATH + os.sep + 'data/Letter r.png',
    )


def sidebar():
   st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 416px;
        padding-top: 0;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 416px;
        margin-left: -500px;
        padding-top: 0;
    }
    ''',
    </style>
    """,
    unsafe_allow_html=True,
    )


def header_1():
    st.markdown(
        """
    <style>
    .css-sygy1k h1 {
        font-size: 60px;
        padding: 0;
        text-align: left;
        color: rgb(229, 9, 20);
        font-weight: 700;
        margin-top: -10px;
        margin-bottom: -32px;
    }
    </style>    
    """,
        unsafe_allow_html=True,
    )


def header_2():
    st.markdown(
        """
    <style>
    h2 {
        color: white;
        font-size: 24px;
        font-weight: 600;
        text-align: left;
    }
    </style>    
    """,
        unsafe_allow_html=True,
    )


def dropdown():
    st.markdown(
        """
    <style>
    .css-1d0tddh {
        text-overflow: clip;
        overflow: revert;
        white-space: nowrap;
    }
    </style>    
    """,
        unsafe_allow_html=True,
    )


def select_box():
    st.markdown(
        """
    <style>
    .css-16huue1 {
        background: rgb(19, 23, 32) none repeat scroll 0% 0%;
        width: fit-content;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 0.4rem;
        padding-top: 0.4rem;
    }
     </style>    
    """,
        unsafe_allow_html=True,
    )
    

def column_buttons():
    st.markdown(
        """
    <style>
    .css-keje6w {
        text-align: center;
    }    
    """,
        unsafe_allow_html=True,
    )


def warning():
    st.markdown(
        """
    <style>
    p {
        color: white;
        font-size: 24px;
        font-weight: 600;
        text-align: center;
    }    
    """,
        unsafe_allow_html=True,
    )


def warning_margin():
    st.markdown('<div class="stAlert" style="padding-bottom: 0px; margin-top: 200px; text-align: center; background-color: rgba(129, 138, 21, 0.65);">',
        unsafe_allow_html=True,
    )


def alert_color():
    st.markdown(
    """
    <style>
    .st-en {
        background-color: rgba(129, 138, 21, 0.65);
        border: 1px solid rgba(11, 5, 27, 0.55);
    }    
    """,
    unsafe_allow_html=True,
    )


def spinner():
    st.markdown(
    """
    <style>
    .css-1gk2i2l {
        background-color: rgba(129, 138, 21, 0.65);
        border: 1px solid rgba(11, 5, 27, 0.55);
        padding-right: 16px;
        padding-left: 16px;
        padding-bottom: 16px;
        padding-top: 16px;
        display: flex;
        gap: 1rem;
        -moz-box-pack: justify;
        justify-content: center;
        border-bottom-left-radius: 0.25rem;
        border-bottom-right-radius: 0.25rem;
        border-top-right-radius: 0.25rem;
        border-top-left-radius: 0.25rem;
    }    
    """,
        unsafe_allow_html=True,
    )


def footer(): 
    st.markdown("""
    <style>
    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )


def expander_html():
    '''Text of the expander, with inline styling: text-align: justify'''
    st.write(
        """
    <p style='text-align: justify; font-size: 1rem; font-weight: 400; padding: 0px; margin: 0px 0px 1rem;'>Select a movie from the dropdown menu and rate it on a scale from 1 to 5. Add at least 10 movies to your list, finally hit 'Recommend' below.
    </p>
    <p style='text-align: justify; font-size: 1rem; font-weight: 400; padding: 0px; margin: 0px 0px 1rem;'>Created By Attila Orosz. More info on <a href="https://github.com/orosz-attila/Movie-Recommender" target="_blank">Github</a>.
    </p>
    """, 
    unsafe_allow_html=True,
    )


def random_gif():
    '''This function selects randomly a gif url from a list.
    Returns: url'''
    gif_list = ['https://64.media.tumblr.com/tumblr_ldbj01lZiP1qe0eclo1_500.gifv', 
                'https://25.media.tumblr.com/tumblr_m9ldt94Vmx1rzhs87o1_400.gifv',
                'https://64.media.tumblr.com/tumblr_lc738lDRh31qe0eclo1_r1_500.gifv',
                'https://64.media.tumblr.com/tumblr_lg5v1v555R1qe0eclo1_r2_500.gifv', 
                'https://64.media.tumblr.com/cbc95d977b80b456100225ea0045abef/tumblr_lvkqenqVfH1qe0eclo1_r23_500.gifv',
                'https://64.media.tumblr.com/67d5f672a4a3d86a97d863f28688be28/tumblr_nxt51r9wl81qe0eclo2_r1_500.gifv',
                'https://64.media.tumblr.com/tumblr_laonjuZpOg1qe0eclo1_r4_500.gifv',
                'https://64.media.tumblr.com/tumblr_lasmpzzeeO1qe0eclo1_r2_500.gifv',
                'https://64.media.tumblr.com/tumblr_lce2v5RdkQ1qe0eclo1_r3_500.gifv',
                'https://64.media.tumblr.com/tumblr_lf0civt0Fh1qe0eclo1_r2_500.gifv',
                'https://64.media.tumblr.com/38ad849338d5e1eeecfd1880b0497514/tumblr_mh6d6nDLrR1qe0eclo1_r6_500.gifv' 
                ]
    n = random.randint(0,10)
    url = gif_list[n]
    return url 


def background(url):
    '''This function sets a gif in the background.
    Parameters: url of the gif.
    Returns: nothing
    '''
    st.markdown(
        f'''
    <style>
    .main {{
        background-image: url({url});
        background-size: cover;
        background-position-x: center;
        opacity: 90%;
    }}
    </style>
    ''',  
    unsafe_allow_html=True,
    )
