## 06. The Data Pipeline: Tweets Sentiment Analysis

<p align="center">
  <img src="https://raw.githubusercontent.com/orosz-attila/Spiced-Academy-Data-Science-Projects/master/06_data_pipeline_tweets_sentiment_analysis/structure.svg"/>
</p>


<div align="justify">The challenge of this Data Engineering project was to build a Dockerized Data Pipeline to analyze the sentiment of tweets. At firts, using Tweepy API, I collect tweets in a selected topic and store them in a MondoDB database (tweet_collector). Next, the sentiment of tweets is analyzed and the tweets with the scores are stored in a Postgres database (ETL_job). Finally, tweets with sentiment score are published on Slack channel. (slack_bot)</div><br>


<div align="justify">For the sentiment analysis, SentimentIntensityAnalyzer() of the the Vader library  (Valence Aware Dictionary and sEntiment Reasoner) was used.</div><br>



The folder of this project can be found [here](https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/tree/master/06_data_pipeline_tweets_sentiment_analysis).