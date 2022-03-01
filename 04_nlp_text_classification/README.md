## 04. Natural Language Processing (NLP): Text Classification


<div align="justify">The main goal of this project was to build a text classification model on song lyrics to predict the artist from a piece of text, additionally, to make user-inputs ((artists, lyrics) possible in CLI.</div><br> 

<div align="justify">Through web scraping with BeautifulSoup, the song-lyrics of selected artists are extracted from lyrics.com. During the text pre-processing, word-tokenizer and word-lemmatizer of Natural Language Toolkit (NLTK) is used to "clean" the extracted texts and create the corpus: 1) TreebankWordTokenizer() splits the text into list of words and removes all other punctuation marks, 2) WordNetLemmatizer() reverts words back to their root/base. These steps are required to import and download lexical database such as WordNet. WordNet's Stopwords also removes the most common English words from the corpus. </div><br>
 
<div align="justify">In the model pipeline, Tfidfvectorizer (TF-IDF) transforms the words of the corpus into a matrix, count-vectorizes and normalizes them at once by default. For classification, the multinomial Naive Bayes classifier MultinomialNB() was used which is suitable for classification with discrete features like word counts for text classification. </div><br>

### Versions

I built 2 versions: 
    - Version 1 extracts song lyrics directly from the htmls. 
    - Version 2 extracts, downloads and saves song lyrics locally in separate .txt files. Then all lyrics will be loaded from the .txt files to create the corpus. 


### Testing in CLI 

![animation](https://raw.githubusercontent.com/orosz-attila/Spiced-Academy-Data-Science-Projects/master/04_nlp_text_classification/text_classification.gif)