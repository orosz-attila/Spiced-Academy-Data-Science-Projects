"This is the main file. This version extracts the lyrics directly from the song.html"

import functions_html as mf
import sys
import time


# Instructions for the user
print('Please, enter two artists/bands.')
time.sleep(2)
print('Then enter some lyrics.')
time.sleep(2)
print('The program will show you then which artist wrote these lyrics more likely.')
time.sleep(2)


# Inputs from user
artist1 = input('Enter the first artist: ')
artist2 = input('Enter the second artist: ') 
number_of_songs = int(input('Enter the number of songs to be analyzed: ')) 
print('Enter the lyrics: ')
text = sys.stdin.readlines()


print('Analyzing lyrics...')


# Web scraping songlinks
links_list1 = mf.get_links(artist1, number_of_songs)
links_list2 = mf.get_links(artist2, number_of_songs)


# Creating list of the extracted lyrics from links 
corpus1 = mf.get_corpus(links_list1)
corpus2 = mf.get_corpus(links_list2)
corpus = corpus1 + corpus2
clean_corpus = mf.corpus_cleaner(corpus)


# Creating labels with the name of the artists to the lyrics
labels = mf.creating_labels(artist1, artist2, corpus1, corpus2) 


# Testing classification model with the text entered by the user
mf.ml_model(clean_corpus, labels, text)