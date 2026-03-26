#!/usr/bin/env python
# coding: utf-8

# # Introduction to TF-IDF
# While calculating the most frequent words in a text can be useful, the most frequent words in a text usually aren’t the most interesting words in a text, even if we get rid of stop words. TF-IDF is a method that builds off word frequency but it more specifically tries to identify the most distinctively frequent or significant words in a document.<br><br>
# TF-IDF = term_frequency * inverse_document_frequency<br>
# term_frequency = number of times a given term appears in document<br>
# inverse_document_frequency = log(total number of documents / number of documents with term) + 1<br><br>
# The reason we take the inverse, or flipped fraction, of document frequency is to boost the rarer words that occur in relatively few documents.

# # TF-IDF: Preprocessing

# In[1]:


import pandas as pd # dealing with dataframe
import json # dealing with json datafiles


# The books is available at: https://babel.hathitrust.org/cgi/pt?id=loc.ark:/13960/t6737fd9d

# In[2]:


# Load the json datafile
file_path = 'Data/loc.ark+=13960=t6737fd9d.json'
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
print(data)


# In[3]:


# Word frequency data of each page
data['features']['pages'][60]['body']


# In[4]:


# Save the frequency of each word in each page to a dataframe
page_list = [] # empty lists to record the information
token_list = []
count_list = []
for i in range(len(data['features']['pages'])): # loop through each page
    if data['features']['pages'][i]['body'] is not None: # if that page has word frequency information
        for token in data['features']['pages'][i]['body']['tokenPosCount']: # loop through each word
            token_count = 0
            for pos_keys in data['features']['pages'][i]['body']['tokenPosCount'][token]: # add up the total occurences of that word
                token_count += data['features']['pages'][i]['body']['tokenPosCount'][token][pos_keys]
            page_list.append(i+1) # add one to page number because there is no page 0
            token_list.append(token) # add the word
            count_list.append(token_count) # add the frequency of the word
word_count_by_page = pd.DataFrame({
    'Page': page_list,
    'Token': token_list,
    'Count': count_list 
}) # save the data to a dataframe
word_count_by_page


# In[5]:


# Group words into lower cases
word_count_by_page = word_count_by_page.groupby([word_count_by_page['Token'].str.lower(), 'Page'])['Count'].sum().reset_index()
word_count_by_page


# In[6]:


# Remove stop words
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

word_count_by_page = word_count_by_page.drop(word_count_by_page[word_count_by_page['Token'].isin(stop_words)].index).reset_index(drop=True)
word_count_by_page


# In[7]:


# Remove punctuations
word_count_by_page = word_count_by_page.drop(word_count_by_page[word_count_by_page['Token'].str.contains('[^A-Za-z\s]', regex=True)].index).reset_index(drop=True)
word_count_by_page


# In[8]:


# Add act number information based on page (these boundaries are created based on close examination)
def add_act_number(page):
    if page >= 53 and page <= 74:
        return "Act I"
    elif page >= 76 and page <= 108:
        return "Act II"
    elif page >= 109 and page <= 139:
        return "Act III"
    elif page >= 140 and page <= 164:
        return "Act IV"
    elif page >= 165 and page <= 179:
        return "Act V"
    
word_count_by_page['Act'] = word_count_by_page['Page'].apply(add_act_number)
word_count_by_page


# In[9]:


# Keep the word frequency in each act only
word_count_by_act = word_count_by_page[word_count_by_page['Act'].notna()]
word_count_by_act


# In[10]:


# Sum word counts for each act
word_count_by_act = word_count_by_act.groupby(['Act', 'Token'])[['Count']].sum().reset_index()
word_count_by_act


# # TF-IDF: Build Model

# In[11]:


# Rename the columns so that they’re consistent with the TF-IDF vocabulary that we’ve been using
word_frequency_df  = word_count_by_act.rename(columns={'Token': 'term', 'Count': 'term_frequency'})
word_frequency_df 


# In[12]:


# Create a separate DataFrame by adding up how many acts each term appears
document_frequency_df = (word_frequency_df.groupby(['Act', 'term']).size().unstack()).sum().reset_index()
document_frequency_df = document_frequency_df.rename(columns={0:'document_frequency'})
document_frequency_df


# In[13]:


# Merge the dataframes together, so that for each term in each act, we got its term frequency in that act, and how many acts
# the term appears in the whole play
word_frequency_df = word_frequency_df.merge(document_frequency_df)
word_frequency_df


# In[14]:


# Calculate total number of acts for inverse document frequency
total_number_of_acts = word_frequency_df['Act'].nunique()
total_number_of_acts


# In[15]:


# Calculate inverse document frequency
import numpy as np # performing calculations on arrays
word_frequency_df['idf'] = np.log((total_number_of_acts) / (word_frequency_df['document_frequency'])) + 1
word_frequency_df


# In[16]:


# Calculate TF-IDF scores
word_frequency_df['tfidf'] = word_frequency_df['term_frequency'] * word_frequency_df['idf']
word_frequency_df


# In[17]:


# Sort the dataframe to get top 5 words with highest TF-IDF scores in each act
word_frequency_df.sort_values(by=['Act', 'tfidf'], ascending=[True,False]).groupby(['Act']).head(5)


# # Task 1

# Examine the top 5 words based on TF-IDF score for each act. Refer to the definition of TF-IDF and address the following questions: (1) What characteristics must a word possess to become a "top word" with the highest TF-IDF score? (2) How does a TF-IDF score differ from raw word frequency? (3) Which types of words would become top words when using raw word frequency?

# For these top words its important for them to have a mixture of 'term_frequency' and 'document_frequency'. In order for them to have a high TF-IDF score. This indicates that these words are distinct and significant words in the document. This differs from raw word frequency as this is trying to measure the significance/impactfulness to these words and their importance/impact to the overall document. The types of words that would be the top words would be common phrases or words with less impact like 'and', 'the' etc

# # Task 2

# In[18]:


# Compute the top one word with the highest TF-IDF score for each page (instead of act).
# Use "word_count_by_page" dataframe and copy the codes to produce the word frequency for each page,
# then generate the document frequency of each word, merge the two dataframes, calculate the total number of pages,
# compute IDF, TF-IDF, and finally, sort by Page and TF-IDF. Group by "Page" and select the top 1 word for each page.


page_list2 = []
token_list2 = []
count_list2 = []
for i in range(len(data['features']['pages'])): # loop through each page
    if data['features']['pages'][i]['body'] is not None: # if that page has word frequency information
        for token in data['features']['pages'][i]['body']['tokenPosCount']: # loop through each word
            token_count2 = 0
            for pos_keys in data['features']['pages'][i]['body']['tokenPosCount'][token]: 
                token_count2 += data['features']['pages'][i]['body']['tokenPosCount'][token][pos_keys]
            page_list2.append(i+1) 
            token_list2.append(token) 
            count_list2.append(token_count) 
word_count_by_page2 = pd.DataFrame({
    'Page': page_list,
    'Token': token_list,
    'Count': count_list 
}) 

document_frequency_df2 = (word_count_by_page2.groupby(['Token', 'Token']).size().unstack()).sum().reset_index()



word_frequency_df2 = word_count_by_page2.merge(document_frequency_df2)
word_frequency_df2['idf'] = np.log((total_number_of_acts) / (word_frequency_df['document_frequency'])) + 1
word_frequency_df2['tfidf'] = word_frequency_df['term_frequency'] * word_frequency_df['idf']



word_frequency_df2.sort_values(by=['Page', 'tfidf'], ascending=[True,False]).groupby(['Page']).head(1)


# # TF-IDF with Scikit-Learn

# In[19]:


# Load the dataset of US inaugural addresses
US_inaugural = pd.read_csv('Data/US_Inaugural_Addresses.csv')
US_inaugural


# In[20]:


# Initialize TfidfVectorizer, using English stopwords and converting words to lowercase
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english', lowercase=True)


# In[21]:


# Generate a dataframe of tfidf values using TfidfVectorizer
tfidf_matrix = tfidf_vectorizer.fit_transform(US_inaugural['Text']) # Generate a matrix
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out()) # Convert matrix to dataframe
tfidf_df.set_index(US_inaugural['Title'], inplace=True) # Replace the index to be the name of the inaugural speeches
tfidf_df


# In[22]:


# Reorganize the DataFrame so that the words are in rows rather than columns
tfidf_df.stack().reset_index()


# In[23]:


# Calculate the word with highest TF-IDF score in each inaugural address
tfidf_df = tfidf_df.stack().reset_index()
tfidf_df = tfidf_df.rename(columns={0:'tfidf', 'Title': 'document','level_1': 'term'})
tfidf_df.sort_values(by=['document','tfidf'], ascending=[True,False]).groupby(['document']).head(1)


# # Task 3

# In[24]:


# Compute the top one word with the highest TF-IDF score for each inaugural address without including stopwords.
# Define a new tfidfvectorizer without including stopwords, and copy the codes with that new tfidfvectorizer to fit_transform,
# convert the generated matrix to a DataFrame, set the index as title of the address, and reorganize the dataframe,
# then rename the columns, and finally sort values and select the top 1 word of each inaugural address
# (Don't be surprised if you find they are mostly the same word. That's why stop words removal is important!)


tfidf_vectorizer2 = TfidfVectorizer(lowercase=True)
tfidf_matrix2 = tfidf_vectorizer2.fit_transform(US_inaugural['Text'])
tfidf_df2 = pd.DataFrame(tfidf_matrix2.toarray(), columns=tfidf_vectorizer2.get_feature_names_out()) 
tfidf_df2.set_index(US_inaugural['Title'], inplace=True) 

tfidf_df2.stack().reset_index()
tfidf_df2 = tfidf_df2.stack().reset_index()
tfidf_df2 = tfidf_df2.rename(columns={0:'tfidf', 'Title': 'document','level_1': 'term'})
tfidf_df2.sort_values(by=['document','tfidf'], ascending=[True,False]).groupby(['document']).head(1)





# In[25]:


# for declarative statistical visualization
get_ipython().system('pip install altair')


# In[26]:


# Some fancy visualizations to highlight the words with highest TF-IDF score in each inaugural address
import altair as alt

top_tfidf = tfidf_df.sort_values(by=['document','tfidf'], ascending=[True,False]).groupby(['document']).head(10)

# Terms in this list will get a red dot in the visualization
term_list = ['war', 'peace']

# adding a little randomness to break ties in term ranking
top_tfidf_plusRand = top_tfidf.copy()
top_tfidf_plusRand['tfidf'] = top_tfidf_plusRand['tfidf'] + np.random.rand(top_tfidf.shape[0])*0.0001

# base for all visualizations, with rank calculation
base = alt.Chart(top_tfidf_plusRand).encode(
    x = 'rank:O',
    y = 'document:N'
).transform_window(
    rank = "rank()",
    sort = [alt.SortField("tfidf", order="descending")],
    groupby = ["document"],
)

# heatmap specification
heatmap = base.mark_rect().encode(
    color = 'tfidf:Q'
)

# red circle over terms in above list
circle = base.mark_circle(size=100).encode(
    color = alt.condition(
        alt.FieldOneOfPredicate(field='term', oneOf=term_list),
        alt.value('red'),
        alt.value('#FFFFFF00')        
    )
)

# text labels, white for darker heatmap colors
text = base.mark_text(baseline='middle').encode(
    text = 'term:N',
    color = alt.condition(alt.datum.tfidf >= 0.23, alt.value('white'), alt.value('black'))
)

# display the three superimposed visualizations
(heatmap + circle + text).properties(width = 600)


# # Task 4

# Based on our explorations of TF-IDF scores, address the following questions: (1) What limitations do you think the TF-IDF method has? (2) Can you suggest another potential application for this method? Please provide an example from either academic research or real-life situations and explain the advantages that TF-IDF calculation could offer in that context.

# Some of the limitations we have seen from TF-IDF scores from this assignmnet has been that without the usage of stopwords the data collected can be filled with commonly used words that lack a clear description of the text. This may be a problem as searching for the right words to take out of our text search is difficult as you want clear results but also don't want to dictate too much what exact words get removed from the results. An interesting application that came to mind for TF-IDF scores is if this practice were to be used by online moderators of online games, or social media platforms to check for hate speech or other harmful language to help with the report system. This could help as this specific form of moderation hasn't been perfected when it comes to manual user review of reports of hate speech or other use of language that breaks a platforms terms of service. So having this practice as a visualization tool and another way to make more competant automation or manual review of reports would be helpful.

# # Sentiment Analysis

# We use VADER for sentiment analysis, which stands for Valence Aware Dictionary and sEntiment Reasoner, calculates the sentiment of texts by referring to a lexicon of words that have been assigned sentiment scores as well as by using a handful of simple rules.

# In[27]:


# Install VADER Sentiment analysis
get_ipython().system('pip install vaderSentiment')


# In[28]:


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER so we can use it later
sentimentAnalyser = SentimentIntensityAnalyzer()


# In[29]:


sentimentAnalyser.polarity_scores("I like sentiment analysis")


# In[30]:


sentimentAnalyser.polarity_scores("I don't like sentiment analysis")


# In[31]:


# Calculate sentiment score for a text
def calculate_sentiment(text):
    # Run VADER on the text
    scores = sentimentAnalyser.polarity_scores(text)
    # Extract the compound score
    compound_score = scores['compound']
    # Return compound score
    return compound_score


# # Task 5

# Calculate the sentiment score of Trump's tweets by applying the "calculate_sentiment" function to the "text" column of the "trump" dataframe. Afterward, print the texts and sentiment scores for the first five tweets in the dataframe. Do the sentiment scores align with your understanding of the text? Keep in mind that the sentiment score ranges from -1 (totally negative) to 1 (totally positive).<br>
# Include your codes in the following cell (code) and the discussion in the next cell (markdown).

# In[32]:


trump = pd.read_csv("Data/trump.csv")

sentimentAnalyser2 = SentimentIntensityAnalyzer()

first_five_tweets = trump['text'].head(5)

def calculate_sentiment(tweet_text):
    scores2 = sentimentAnalyser2.polarity_scores(tweet_text)
    compound_score2 = scores2['compound']
    print(f'Scores: {scores2}')
    print(f'Compound Score: {compound_score2}')
    return compound_score2

first_five_tweets = trump['text'].head(5)

for i, tweet_text in enumerate(first_five_tweets):
    sentiment_score = calculate_sentiment(tweet_text)
    print(f'Tweet {i + 1}: {tweet_text}\nSentiment Score: {sentiment_score}\n')


# I would say that Trump's tweets tend to be on the more negative side and this can be especially seen in Tweets 4 and 5. Tweets 1, 2 and 3 are not good representations of Trumps views as a whole as they don't take into account the language he uses in his speech in Fayetteville and the article "Will Media Apologize to Trump?". But strictly looking at tthe text from the tweets the scores to align with general mood he is in as in Tweet 1, 2, 3 the language is relatively neutral or joyful although the language he uses in his shows or links may differ from that.
