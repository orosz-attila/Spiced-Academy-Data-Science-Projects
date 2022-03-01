# only done once! we have to download the WordNet database locally
# import nltk 
# nltk.download("wordnet") 
# nltk.download('stopwords')


import requests
import os
from bs4 import BeautifulSoup

from nltk.tokenize import TreebankWordTokenizer
from nltk.stem import WordNetLemmatizer

from nltk.corpus import stopwords 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB


def get_links(artist, number): 
    """
    This function extracts the links to each song-lyrics of the artist selected by the user, 
    and returns a list of links to the song pages with the number selected. 
    Default number=200.   
    """
    
    links_list = []
    
    soup = BeautifulSoup(requests.get('https://www.lyrics.com/artist/' + artist.lower().replace(' ','-') + '/').text, features="lxml")
    extracted_links = [tag.a['href'] for tag in soup.find_all(class_='tal qx')]
    
    for link in extracted_links[:number]:
        song_url = 'https://www.lyrics.com/' + link
        links_list.append(song_url)
    return links_list


def download_lyrics(artist, links_list):
    '''This function downloads and saves the lyrics from the links in .txt files in local folder.'''
    directory = f"{artist}"
    PATH = os.path.abspath('')
    full_path = os.path.join(PATH, directory)

    os.mkdir(full_path) 

    for link in links_list:
        song_html = requests.get(link)
        try: 
            song_soup = BeautifulSoup(song_html.text,features="lxml")
            song_title = song_soup.find(class_='lyric-title').text
            f = open(f'{full_path}/{song_title}.txt', 'w') # excisting file w same song title ll be automatically overwritten --> no duplications
            f.write(song_soup.find(class_='lyric-body').text) 
        except: # Song urls without lyrics will be skipped
            pass 
        f.close()


def load_corpus(artist): 
    '''This function loads the lyrics into the corpus from the local .txt files'''
    CORPUS = []

    directory = f"{artist}"
    PATH = os.path.abspath('')
    full_path = os.path.join(PATH, directory)

    for filename in os.listdir(directory):
        
        song_file = open(f'{full_path}/{filename}', 'r') 
        lyrics_text = song_file.read() 
        CORPUS.append(lyrics_text)
    return CORPUS



def corpus_cleaner(CORPUS):
    """
    This function transforms all letters to lower case, tokenizes and lemmatizes words,
    and returns a clean corpus. 
    """

    CORPUS = [s.lower() for s in CORPUS]    

    CLEAN_CORPUS = []

    tokenizer = TreebankWordTokenizer() 
    lemmatizer = WordNetLemmatizer()

    for doc in CORPUS:
        tokens = tokenizer.tokenize(text=doc)
        clean_doc = " ".join(lemmatizer.lemmatize(token) for token in tokens)
        CLEAN_CORPUS.append(clean_doc)
    return CLEAN_CORPUS


def creating_labels(artist1, artist2, corpus1, corpus2):
    '''
    This function takes the entered artist names and multiplies them with the number of songs selected by the users
    and returns the label as a list. 
    '''
    LABELS = [artist1] * len(corpus1) + [artist2] * len(corpus2)
    return LABELS


def ml_model (CLEAN_CORPUS, LABELS, text):
    """
    Tfidfvectorizer transforms the corpus into a matrix, count-vectorizes and normalizes it at once by default. 
    Stopwords will remove the most common English words from the Corpus. 
    Classification model: MultinomialNB (Naive Bayes) 
    """
    text = ' '.join(text)
    STOPWORDS = stopwords.words('english')

    model = [('tf_idf', TfidfVectorizer(max_features = 1000, min_df = 2, max_df = 0.5, ngram_range = (1,2), stop_words=STOPWORDS)),
            ('MNB', MultinomialNB(alpha = 0.1))
    ]

    pipeline = Pipeline(model)
    pipeline.fit(CLEAN_CORPUS, LABELS)
    prediction = pipeline.predict([text]) 
    probability = pipeline.predict_proba([text]).max().round(2)*100
    print(f'These lyrics are more likely ({probability} %) to be written by: {prediction[0]}')