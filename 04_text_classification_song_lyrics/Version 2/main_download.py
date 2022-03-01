"This is the main file. This version uses the downloaded .txt files to create the lyrics corpus."


import functions_download as mf
import sys
import time


# Instructions for the user
print('Please, enter two artists/bands.')
time.sleep(2)
print('Then enter some lyrics.')
time.sleep(2)
print('The program will show you then which artist wrote these lyrics more likely.')
time.sleep(2)


artist1 = input('Enter the first artist: ')
artist2 = input('Enter the second artist: ') 


# Inputs from user
print('Enter the lyrics: ')
text = sys.stdin.readlines()


print('Downloading lyrics...')


# Web scraping songlinks
links_list1 = mf.get_links(artist1, 200)
links_list2 = mf.get_links(artist2, 200)


# Downloading lyrics
mf.download_lyrics(artist1, links_list1)
mf.download_lyrics(artist2, links_list2)


# Creating list of the extracted lyrics from the downloaded txt files 
corpus1 = mf.load_corpus(artist1)
corpus2 = mf.load_corpus(artist2)
corpus = corpus1 + corpus2
clean_corpus = mf.corpus_cleaner(corpus)


print('Analyzing lyrics...')


# Creating labels with the name of the artists to the lyrics
labels = mf.creating_labels(artist1, artist2, corpus1, corpus2) 


# Testing classification model with the text entered by the user
mf.ml_model(clean_corpus, labels, text)