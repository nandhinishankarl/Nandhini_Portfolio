#!/usr/bin/env python
# coding: utf-8

# ## Spotify Billboard Hot 100

# In[1174]:


pip install spotipy


# In[1902]:


import json
import time

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# ### Use the Billboard Hot 100's Playlist's URI

# In[1903]:


client_id = '456b176f8e9246a0825ac0c4d9ec1f43'
secret = '2ee5e41324c241299208a8b844ae6c7c'
# playlist uri
# from the 4th of February
billboard_uri = 'spotify:playlist:6OML3vQZzyfYfeykXAiOGu'


# In[1904]:


# using the 'client_id' and 'secret' variables for spotify client credentials
# authenticating session
client_credentials_manager = SpotifyClientCredentials(client_id=client_id,client_secret=secret)

# create spotify session object
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# ## Data Scraping

# In[1905]:


billboard_tracks = sp.playlist(billboard_uri)


# In[1906]:


# getting the first song from the Billboard Hot 100's list
# prints out the details of the first song
billboard_tracks['tracks']['items'][0]['track']


# Information we need
# 1. Name (of the artist)
# 2. Name of the song
# 3. Id
# 4. Popularity

# In[1907]:


# retrieving the name of the artist
billboard_tracks['tracks']['items'][1]['track']['artists'][0]['name']


# In[1908]:


# retrieving the name of the song
billboard_tracks['tracks']['items'][1]['track']['name']


# In[1909]:


# retrieving the uri of the song
billboard_tracks['tracks']['items'][1]['track']['uri']


# In[1910]:


# retrieving popularity of the song
billboard_tracks['tracks']['items'][1]['track']['popularity']


# In[1911]:


# creating lists for

# Name of the artist
artist_name = []

# Name of the song
song_name = []

# Id/uri of the song
song_id = []

# Popularity of the song
song_popularity = []


# ### Retrieve songs and song details from the Billboard Playlist

# In[1912]:


# appending song details to each list
for i,j in enumerate(billboard_tracks['tracks']['items']):
    artist_name.append(j['track']['artists'][0]['name'])
    song_name.append(j['track']['name'])
    song_id.append(j['track']['uri'])
    song_popularity.append(j['track']['popularity'])


# In[1913]:


# adding lists to a data frame 
import pandas as pd

billboard_df = pd.DataFrame({"Artist":artist_name, "Song Title": song_name, "Song ID": song_id, 
                             "Song Popularity": song_popularity})


# In[1914]:


billboard_df.head()


# In[1915]:


# we can extract the audio features of the first track
# using audio_features
# the first track on this list is Flowers by Miley Cyrus
sp.audio_features(billboard_df['Song ID'][0])


# Important Features of a track that I want to use for this analysis:
# 
# 1. Danceability: How suitable is this track for dancing? Would you play it at max volumne at the club?
# 
# 2. Energy: Measured on a scale of 0.0 - 1.0. Energetic tracks feel fast, loud, and noisy. 
# 
# 3. Key: The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1. >= -1 <= 11
# 
# 3. Loudness: The overall loudness of a track in decibels (dB).Values typically range between -60 and 0 db.
# 
# 4. Speechiness: Detects the presence of spoken words. For example, if it's a podcast recording, there are more spoken words and the value would be closer to 1.0. If it's between 0.33 - 0.66, the tracks contain both music and speech. This tends to be the case for rap music. If it's less than 0.33, the tracks tend to have more music and less speech.
# 
# 5. Acousticness: A confidence measure from 0.0 to 1.0 of whether the track is acoustic.
# 
# 6. Instrumentalness: Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. 
# 
# 7. Liveness: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
# 
# 8. Valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).
# 
# 9. Tempo: The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
# 
# 10. Duration_ms: Duration in milliseconds. 
# 
# 11. time_signature: An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4". >= 3<= 7

# ### Scraping audio features for all songs

# In[1916]:


# creating lists for the different audio features we need
danceability = []
energy = []
key = []
loudness = []
mode = []
speechiness =[]
acousticness = []
instrumentalness = []
liveness = []
valence = []
tempo = []
duration = []
timesignature = []


# In[1917]:


audio_features = {
   'danceability': [],
   'energy': [],
    'key': [],
   'loudness': [],
    'mode': [],
    'speechiness': [],
   'acousticness': [],
   'instrumentalness': [],
    'liveness': [],
   'valence': [],
   'tempo': [],
    'duration': [],
    'time signature': []
}


# In[1918]:


entries = []
# looping through tracks to extract the audio features for every song
    
for i,j in enumerate(billboard_df['Song ID']):
    entries.append(sp.audio_features([j]))


# In[1919]:


# appending audio features to each list
for i,j in enumerate(entries):
    audio_features['danceability'].append(j[0]['danceability'])
    audio_features['energy'].append(j[0]['energy'])
    audio_features['key'].append(j[0]['key'])
    audio_features['loudness'].append(j[0]['loudness'])
    audio_features['mode'].append(j[0]['mode'])
    audio_features['speechiness'].append(j[0]['speechiness'])
    audio_features['acousticness'].append(j[0]['acousticness'])
    audio_features['instrumentalness'].append(j[0]['instrumentalness'])
    audio_features['liveness'].append(j[0]['liveness'])
    audio_features['valence'].append(j[0]['valence'])
    audio_features['tempo'].append(j[0]['tempo'])
    audio_features['duration'].append(j[0]['duration_ms'])
    audio_features['time signature'].append(j[0]['time_signature'])


# In[1920]:


billboard_features = pd.DataFrame(audio_features)


# In[1921]:


# Adding them to the billboard data frame
billboard_df['danceability'] = audio_features['danceability']
billboard_df['energy'] = audio_features['energy']
billboard_df['key'] = audio_features['key']
billboard_df['loudness'] = audio_features['loudness']
billboard_df['mode'] = audio_features['mode']
billboard_df['speechiness'] = audio_features['speechiness']
billboard_df['acousticness'] = audio_features['acousticness']
billboard_df['instrumentalness'] = audio_features['instrumentalness']
billboard_df['liveness'] = audio_features['liveness']
billboard_df['valence'] = audio_features['valence']
billboard_df['tempo'] = audio_features['tempo']
billboard_df['duration'] = audio_features['duration']
billboard_df['time signature'] = audio_features['time signature']


# In[1922]:


# Now we have all the data we need for the tracks from the Billboard Hot 100 Playlist 
billboard_df


# In[1923]:


# checking for null values
billboard_na = billboard_df.isna().sum()
# thankfully, there are no null values
# I am extremely pleased
print(billboard_na)


# ## Exploratory Data Analysis

# I want to see which artists are popular from the Billboard Hot 100 List. I would also like to create visualizations for the audio features of billboard hot 100's songs to get an idea of what the overall distribution looks like.

# ### Top 10 streamed artists from the Billboard Hot 100

# In[1924]:


billboard_df['Artist'].value_counts().head(10).plot(kind='bar', color='green')
plt.title('Top 10 Streamed Artists - Billboard Hot 100')


# SZA and tops the list with 6 songs on the billboard hot 100, very impressive! Followed by Morgan Wallen with the same number of songs.  

# ### Overall Distribution of audio features 

# In[1956]:


# Import seaborn
import seaborn as sns
import matplotlib.pyplot as plt

# Features distribution
f, axes = plt.subplots(2, 6, figsize=(20, 10))

# Adjust the subplot layout parameters
f.subplots_adjust(hspace=0.3, wspace=0.4)

sns.distplot( billboard_df['danceability'], color="green", ax=axes[0, 0])
sns.distplot( billboard_df['energy'], color="green", ax=axes[0, 1])
sns.distplot( billboard_df['key'], color="green", ax=axes[0, 2])
sns.distplot( billboard_df['loudness'], color="green", ax=axes[0, 3])
sns.distplot( billboard_df['speechiness'], color="green", ax=axes[0, 4])
sns.distplot( billboard_df['acousticness'], color="green", ax=axes[0, 5])
sns.distplot( billboard_df['instrumentalness'], color="green", ax=axes[1, 0])
sns.distplot( billboard_df['liveness'], color="green", ax=axes[1, 1])
sns.distplot( billboard_df['valence'], color="green", ax=axes[1, 2])
sns.distplot( billboard_df['tempo'], color="green", ax=axes[1, 3])
sns.distplot( billboard_df['duration'], color="green", ax=axes[1, 4])
sns.distplot( billboard_df['time signature'], color="green", ax=axes[1, 5])

f.delaxes(axes[1][3])
plt.show()


# We can see the distribution of the scores of audio features from the plots that were generated. Features like danceability, energy, tempo, valence, and duration seem to follow normal distributions. 
# 
# These audio features are relevant when it comes to mainstream pop music. 
# 
# There seems to be a slight negative skew for the loudness graph.  
# 
# From the liveness graph, we can see that the range of values is 0 - 0.75
# Liveness detects the presence of an audience, if it's above 0.8, there is a high possiblity that it was a live performance. Songs that chart on the billboard list tend to be studio recorded versions. So this is expected. 
# 
# From the duration graph, we can see that the mean duration is around 200,000 ms which is 3.3 minutes. 
# Radio stations want songs to be short so they can play more advertisements. Most artists are encouraged to release tracks that are between 3 minutes and 3 minutes 30 seconds. 
# 
# We can see that most values for speechiness fall between 0 and 0.2, if the value is less than 0.3, this means a song has more music and less words. This isn't surprising, most songs on the Billboard Hot 100 list tend to be more music based. 
# 
# We can also see that most songs have a time signature of 4.

# ### Correlation Analysis 

# This can help us determine if there is a strong correlation between different audio features. Are these variables strongly correlated? Let's examine the relationships visually. 

# In[1933]:


billboard_df.corr()


# In[1944]:


f,ax = plt.subplots(figsize=(12, 12))
sns.heatmap(billboard_df.corr(),annot=True, linewidths=0.4,linecolor="white", fmt= '.1f',ax=ax,cmap="Greens")
plt.show() 


# We can see that energy and loudness have a very high correlation score of 0.8. 
# This makes sense because energetic songs tend to be loud too. 
# 
# We can also a see a somewhat high correlation between energy and valence (0.5). Songs with high valence scores tend to be positive, positive songs tend to be upbeat, so that explains it. 

# ### Frequency of songs based on emotion

# In[1900]:


def song_emotion(row):
       if row["valence"] > 0.5:
           return "happy"
       else:
           return "sad"

billboard_df["emotion"] = billboard_df.apply(song_emotion, axis=1)


# In[1901]:


billboard_df['emotion'].value_counts().plot(kind='bar', color="green")
plt.title('Frequency of songs based on emotion')


# The frequency of sad songs is slightly higher than the frequency of happy songs from the billboard hot 100 list! What does this say about our listeners? Do we gravitate towards sad songs so we can wallow in misery? 

# Let's visualize the songs and their emotions based on song popularity scores. 
# 
# This score is based on the total number of plays the track has and how recent those plays are.
# The popularity of a track is a value between 0 and 100, with 100 being the most popular. 
# 
# New songs would have higher popularity scores compared to old songs. 
# 
# For this analysis, I want to create a subset of the dataset that contains really popular songs.

# In[1825]:


popular_songs = billboard_df[billboard_df["Song Popularity"] > 80]


# In[1826]:


popular_songs['emotion'].value_counts()


# Now let's examine the mood of these popular songs. 

# In[1827]:


popular_songs['emotion'].value_counts().plot(kind='bar', color="green")


# The count of sad songs is still slightly higher for extremely popular songs. Does listening to sad music during our worst moments help us process these emotions? Or do we just like to feel sad? I hope it isn't the latter, that would be very concerning. 

# ### Frequency of Popular Songs based on the Key

# In[1710]:


sns.barplot(x = "key", y = "Song Popularity", data = billboard_df, color = "green")
plt.title('Key vs Popularity')
plt.show()


# We can see that songs with a key value of 11 are extremely popular. This falls into pitch class B. 

# ### Frequency of popular songs based on time signature

# In[1711]:


sns.barplot(x = "time signature", y = "Song Popularity", data = billboard_df, color = "green")
plt.title('Time signature vs Popularity')
plt.show()


# Songs with time signature 3 seem to be more popular. 3 beats per bar.

# ## Relationships between Audio Features and Popular Songs

# In[1712]:


sns.jointplot(x = 'valence', y = 'Song Popularity', data = billboard_df, color = "green")


# In[1713]:


sns.jointplot(x = 'tempo', y = 'Song Popularity', data = billboard_df, color = "green")


# In[1714]:


sns.jointplot(x = 'danceability', y = 'Song Popularity', data = billboard_df, color = "green")


# In[1715]:


sns.jointplot(x = 'acousticness', y = 'Song Popularity', data = billboard_df, color = "green")


# In[1716]:


sns.jointplot(x = 'liveness', y = 'Song Popularity', data = billboard_df, color = "green")


# In[1717]:


sns.jointplot(x = 'instrumentalness', y = 'Song Popularity', data = billboard_df, color = "green")


# In[1718]:


sns.jointplot(x = 'tempo', y = 'Song Popularity', data = billboard_df, color = "green")


# In[1719]:


sns.jointplot(x = 'speechiness', y = 'Song Popularity', data = billboard_df, color = "green")


# In[1720]:


sns.jointplot(x = 'duration', y = 'Song Popularity', data = billboard_df, color = "green")


# In[1721]:


sns.jointplot(x = 'key', y = 'Song Popularity', data = billboard_df, color = "green")


# All the audio features seem to have medium-weak correlations with the popularity scores except for instrumentalness. We can't really see any relationship between instrumentalness and popularity. 
# Perhaps this is related to the size of the dataset, data was scraped for only 100 songs from the Billboard Hot 100 list.
# 
# Maybe we would be able to see strong correlation results if the dataset was bigger? 

# ## Feature Engineering

# The metric that I am considering for popular songs is a popularity score that is greater than 80. 
# I will be converting scores into a binary format based on this metric. If popularity > 80, then 1, else 0. This is the target variable that I am interested in predicting. 
# 
# In the process of feature engineering, we have to convert variables into a format that is suitable for machine learning algorithms. 

# ### Target Variable Conversion

# In[1828]:


def popularity_convertor(row):
       if row["Song Popularity"] > 80:
           return 1
       else:
           return 0

billboard_df["Song Popularity"] = billboard_df.apply(popularity_convertor, axis=1)


# ### Dropping highly correlated columns

# Energy and loudness are highly correlated with a score of 0.8.
# Having two columns that are highly correlated means that there is a potential linear relationship between them. They will equally be able to predict the outcome, which means removing one would be a good idea.
# 
# We also don't need the emotion column for prediction, it was based entirely on the valence column. 

# In[1829]:


billboard_df.drop(["emotion", "loudness"], axis=1, inplace = True)


# ### Dropping columns that are irrelevant for popularity prediction

# We don't need Song ID because it doesn't have any impact on the popularity score of the song. We also don't need the name of the song for the purpose of prediction. 
# Since most values in the instrumentalness column seem to be 0s, it doesn't really play a role in popularity score prediction. The joinplot also depicted a non existent correlation between instrumentalness and popularity.
# For this dataset, I will be dropping the column. 
# 
# I will also be dropping the name of the artist. For the purpose of prediction, I am only interested in using audio features. 

# In[1830]:


billboard_df.drop(["Song Title", "Song ID", "Artist"], axis=1, inplace = True)


# ### Turning categorical variables into dummies

# Dummy variables are basically indicators of the presence or absence of a categorical variable. In this case, I am choosing the time signature column. This column has values that are either 3s or 4s. I want to split this into separate columns. 

# In[1831]:


billboard_df["time signature"] = billboard_df["time signature"].astype("category")
billboard_df = pd.get_dummies(billboard_df, columns=["time signature"])


# ### Defining the feature dataset and the target variable

# In[1832]:


y = billboard_df["Song Popularity"]
x = billboard_df.drop(["Song Popularity"], axis=1)


# In[1958]:


y


# In[1833]:


x.head()


# ### Normalization

# Normalization can be used to transform the columns of the data frame to the same scale. I will be using Min-Max Scaling. This is a technique that's used to subtract the minimum value from each column's max value, it is then divided by the range. The new column will have a minimum value of 0 and a maximum value of 1. 

# In[1834]:


# Normalization
import numpy as np


x_norm = (x - np.min(x))/(np.max(x)-np.min(x)).values
x_norm.head()


# ## Model Implementation

# In[1959]:


# Train test split
from sklearn.model_selection import train_test_split
X_train, X_Test, y_train, y_test = train_test_split(x_norm, y, test_size = 0.2, random_state = 420)


# The model that I have chosen for the prediction of popularity scores is the random forest classifier. Random forest combines the predictions of many decision trees to give the a good accuracy. 

# In[1842]:


from sklearn.ensemble import RandomForestClassifier
RFC_Model = RandomForestClassifier()
RFC_Model.fit(X_train, y_train)
RFC_Predict = RFC_Model.predict(X_Test)
RFC_Accuracy = accuracy_score(y_test, RFC_Predict)
print("Accuracy: " + str(RFC_Accuracy))

RFC_AUC = roc_auc_score(y_test, RFC_Predict) 
print("AUC: " + str(RFC_AUC))


# The accuracy using the random forest model is 70%, which is satisfactory. But I would like to use a bigger dataset with more songs next time to see how it affects the performance.

# ### Predicted Values

# In[958]:


predictions = RFC_Model.predict(X_Test)
predictions


# 1 represents a high popularity score of over 80 and 0 represents a low popularity score that falls below 80. 

# In[959]:


y_test


# These are the true values.
