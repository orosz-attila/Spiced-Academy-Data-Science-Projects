import functions as mf

# Instructions for the user
print('With this program you can select two artists/bands and give the number of songs (per artist) to be analyzed.\nFinally, enter some random lyrics.\nThe program will show you then which artist wrote these lyrics more likely.')

# Inputs from user
artist1 = input('Enter the first artist: ')
artist2 = input('Enter the second artist: ') 
number_of_songs = int(input('Enter the number of songs to be analyzed: ')) 
text = input('Enter the lyrics: ') 

# Web scraping songlinks
links_list1 = mf.get_links(artist1, number_of_songs)
links_list2 = mf.get_links(artist2, number_of_songs)

# Creating list of the extracted lyrics from links 
corpus1 = mf.get_corpus(links_list1)
corpus2 = mf.get_corpus(links_list2)
corpus = corpus1 + corpus2
clean_corpus = mf.corpus_cleaner(corpus)

# Creating labels with the name of the artists to the lyrics
labels = mf.creating_labels(artist1, artist2, number_of_songs) 

# Testing classification model with the text entered by the user
mf.ml_model(clean_corpus, labels, text)