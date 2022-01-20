import requests
from bs4 import BeautifulSoup

from nltk.tokenize import TreebankWordTokenizer
# import nltk  
# nltk.download("wordnet") 
from nltk.stem import WordNetLemmatizer

# nltk.download('stopwords')
from nltk.corpus import stopwords 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
# from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB

def get_links(artist, number): 
    """
    This function extracts the links to each songlyrics of the artist selected by the user, 
    and returns a list of links to the song pages with the number selected by the user.   
    """
    
    links_list = []
    
    soup = BeautifulSoup(requests.get('https://www.lyrics.com/artist/' + artist.lower().replace(' ','-') + '/').text, features="lxml")
    extracted_links = [tag.a['href'] for tag in soup.find_all(class_='tal qx')]
    
    for link in extracted_links[:number]:
        song_url = 'https://www.lyrics.com/' + link
        links_list.append(song_url)
    #print (artist, 'has', len(links_list), 'lyrics')
    return links_list


def get_corpus(links_list):
    """  This function creates a list of the lyrics (with the number selected by the user) for one artist, 
    and returns a list of strings (CORPUS), in which each songlyric is an item. 
         If a lyric is already in the list, it does no append it one more time in the list. The iteration restarts.
         If no lyrics from the website can be extracted, it will be passed. 
    """

    CORPUS = []
    
    for link in links_list: 
        song_html = requests.get(link) 
        song_soup = BeautifulSoup(song_html.text, features="lxml")         
        try:
            song_lyrics = song_soup.find(class_='lyric-body').text 
            if song_lyrics in links_list: 
                continue 
            else:    
                CORPUS.append(song_lyrics) 
        except: 
            pass 
    # print(len(CORPUS))
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


def creating_labels(artist1, artist2, number):
    '''
    This function takes the entered artist names and multiplies them with the number of songs selected by the users
    and returns the label as a list. 
    '''

    LABELS = [artist1] * number + [artist2] * number
    return LABELS


def ml_model (CLEAN_CORPUS, LABELS, text):
    """
    Tfidfvectorizer transforms the corpus into a matrix, count-vectorizes and normalizes it at once by default. 
    Stopwords will remove the most common English words from the Corpus. 
    Classification model: MultinomialNB (Naive Bayes) 
    """

    STOPWORDS = stopwords.words('english')

    model = [('tf_idf', TfidfVectorizer(stop_words=STOPWORDS)),
                ('MNB', MultinomialNB())
    ]

    pipeline = Pipeline(model)
    pipeline.fit(CLEAN_CORPUS, LABELS)
    prediction = str(pipeline.predict([text]))  
    print(f'These lyrics are more likely to be written by {prediction}')
    # print(prediction)


# if __name__ == "__main__":
#     pass  