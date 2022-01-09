import functions as mf
import argparse

# if default not selected, enter arguments in bash: python execute_argparse.py -a1 "Massive Attack" -a2 "Bob Marley" -n 20  

text = input('Enter the lyrics: ')

parser = argparse.ArgumentParser(description = 'Select two artists, then enter the lyrics. The program will show which artist has most likely wrote the lyrics')

parser.add_argument("-a1", "--artist1",
                     help="Selecting the first artist",
                     type=str)
#                     default='Massive Attack')

parser.add_argument("-a2", "--artist2",
                     help="Selecting the second artist",
                     type=str)
#                     default='Bob Marley')

parser.add_argument("-nr", "--number_of_songs",
                     help="Selecting the number of songs for extracting",
                     type=int)
#                      default=20)
 
args = parser.parse_args() 

# Web scraping songlinks
links_list1 = mf.get_links(args.artist1, args.number_of_songs)
links_list2 = mf.get_links(args.artist2, args.number_of_songs)

# Creating list of the extracted lyrics from links 
corpus1 = mf.get_corpus(links_list1)
corpus2 = mf.get_corpus(links_list2)
corpus = corpus1 + corpus2
clean_corpus = mf.corpus_cleaner(corpus)

# Creating labels with the name of the artists to the lyrics
labels = mf.creating_labels(args.artist1, args.artist2, args.number_of_songs)

mf.ml_model(clean_corpus, labels, text)