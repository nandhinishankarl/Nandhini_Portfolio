# Nandhini_Portfolio
Data Science Portfolio

# [Project 1: Disney Movie Analysis: Project Overview](https://github.com/nandhinishankarl/Web-Scraping/blob/main/Disney_Movie_Dataset_Creation_2.ipynb)

- Scraped the info box from wikipedia for all Disney Films 
- Made use of the ‘BeautifulSoup’ python library for scraping portions of the webpages
- Saved data in the form of a csv file and cleaned it using the ‘pandas’ library. 
- Analyzed the dataset further for the highest grossing Disney film 
- The Lion King was the highest grossing Disney film till date 


<img src="images/Screen%20Shot%202023-03-06%20at%203.58.39%20PM.png" width="300" height="300">&nbsp;&nbsp;&nbsp;

# [Project 2: Midnights Sentiment Analysis : Project Overview](https://github.com/nandhinishankarl/Sentiment-Analysis-Projects/blob/main/Midnights%20Sentiment%20Analysis%20-3.ipynb)

- Created a Python list of urls for all the songs from the Midnights album 
- Created a dataset that contains 3 columns using python's 'pandas' library : title, lyrics and sentiment score.
- Scraped lyrics from the list of urls using Genius.com's API 
- Cleaned the lyrics column by removing unnecessary words and characters/punctuations using Python's re (regular expresson) package
- Created a wordcloud to see which words were prominent and frequently occuring
- Words like 'love', 'fallin' and 'feel' stood out, an indicator that the theme of the album is about falling in love
- Calculated the overall sentiment score for each song using SentimentIntensityAnalyzer 
- Visualized the sentiment scores for all songs from the Midnights Album using the matplotlib library in the form of a bar graph 
- There were 4 songs had highly negative scores, the highest being Anti-Hero, with a score of -0.9954, a song about self-deprecation. 
- There were 9 songs had highly positive scores, which is an indicator of Taylor Swift's happiness in her romantic life.

<img src="images/Screen%20Shot%202023-01-12%20at%2012.23.24%20PM.png" width="400">&nbsp;&nbsp;&nbsp;
<img src="images/Screen%20Shot%202023-01-12%20at%2012.23.41%20PM.png" width="300">&nbsp;&nbsp;&nbsp;

# [Project 3: Spotify Song Popularity Analysis and Prediction - Billboard Hot 100 : Project Overview](https://github.com/nandhinishankarl/Nandhini_Portfolio/blob/main/Spotify_Billboard_Hot_100.ipynb)

- Scraped track information for all songs on the Billboard Hot 100 list using Spotipy (Spotify’s API) on the 4th of March.
- Every song has calculated audio features like danceability, song duration and energy.
- Visualized the top 10 streamed artists using Python's matplotlib library, SZA topped the list with 6 songs. 
- Visualized density plots for audio features using Python's seaborn library, the average duration of a song on the Billboard list is 3.3 minutes. 
- Created a frequency graph based on song emotion using Python's matplotlib library, there are 56 sad songs and 44 happy songs.
- Defined the feature variables needed for prediction (audio features) and the target variable to be predicted (popularity score).
- Used the random forest model to predict popularity scores based on audio features, the accuracy was 70%.


<img src="images/Screen%20Shot%202023-03-06%20at%2011.11.19%20AM.png" width="400">&nbsp;&nbsp;&nbsp;
<img src="images/Screen%20Shot%202023-03-06%20at%2011.14.27%20AM.png" width="400">&nbsp;&nbsp;&nbsp;
<img src="images/Screen%20Shot%202023-03-06%20at%2011.17.01%20AM.png" width="200" height="200">&nbsp;&nbsp;&nbsp;



