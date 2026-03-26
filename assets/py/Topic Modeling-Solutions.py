#!/usr/bin/env python
# coding: utf-8

# One of the primary applications of natural language processing is to automatically extract what topics people are discussing from large volumes of text. We need an automated algorithm that can read through the text documents and automatically output the topics discussed. In this lab, we will use Latent Dirichlet Allocation(LDA), a popular algorithm for topic modeling. LDA is a Bayesian network that explains a set of observations through unobserved groups, and each group explains why some parts of the data are similar.

# # Preprocessing

# In[1]:


# Installing nltk for generating stop words. Stop words are commonly used words (such as "the", "a", "an", "in")
# that we want our topic models to ignore (as they are not suggestive to "topics")
#get_ipython().system(' pip install nltk')


# In[2]:


# Loading nltk stop words
import nltk
nltk.download('stopwords')


# In[3]:


# Import other packages
import re # regular expression
import numpy as np # performing calculations on arrays
import pandas as pd # dealing with dataframe

# Gensim, for topic modeling
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

# Plotting tools
import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


# Prepare stop words
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
print(stop_words)


# In[5]:


# Load dataset
# The dataset is available at https://raw.githubusercontent.com/selva86/datasets/master/newsgroups.json
df = pd.read_json("Data/newsgroups.json")
df


# In[6]:


# We are only using the first 1,000 documents because model training can be time-consuming
df = df.iloc[:1000,:]
df


# # Data cleaning

# In[7]:


# Get the first document
data = df.content.values.tolist()
data[0]


# In[8]:


# Removing Emails
email_pattern = re.compile("\S*@\S*\s?") # \S means matching a character, \s means matching a space
                                         # * means matching 0 or multiple times, ? means matching 0 or 1 times
for i in range(len(data)):
    data[i] = re.sub(email_pattern, '', data[i])
print(data[0])


# In[9]:


# Removing new line characters
new_line_pattern = re.compile("\s+") # + means matching 1 or more times
for i in range(len(data)):
    data[i] = re.sub(new_line_pattern, ' ', data[i]) # converting line breaks and multiple spaces into one space
print(data[0])


# In[10]:


# Tokenize words using gensim's simple_preprocess
for i in range(len(data)):
    data[i] = gensim.utils.simple_preprocess(str(data[i]), deacc=True) # deacc=True means removing punctuations
print(data[0])


# In[11]:


# Removing stop words
for i in range(len(data)):
    data[i] = [word for word in data[i] if word not in stop_words]
print(data[0])


# # Including bigrams

# In[12]:


# The basic idea here is we group words that frequently appear together to a phrase
bigram = gensim.models.Phrases(data, min_count=5, threshold=100)
bigram_mod = gensim.models.phrases.Phraser(bigram)
print(bigram_mod[data[0]])


# # Task 1

# What would be the impact of changing the 'min_count' to 1 when generating bigrams? Please redefine the bigrams with the new 'min_count' setting and rerun the experiment. Print the updated word list of data\[0\] with these new bigrams.
# <br>Are there more or fewer words grouped together compared to the original result obtained with a 'min_count' setting of 5? Are these additional or removed bigrams meaningful? Provide an assessment of the advantages and disadvantages of this change and suggest whether the change is advisable.
# <br>Include your codes in the following cell (code) and the discussion in the next cell (markdown).

# In[13]:


bigram_new = gensim.models.Phrases(data, min_count=1, threshold=100)
bigram_mod_new = gensim.models.phrases.Phraser(bigram_new)
print(bigram_mod_new[data[0]])


# 

# # Creating models

# In[14]:


# Convert each document to a list of words including generated bigrams 
bigram = gensim.models.Phrases(data, min_count=5, threshold=100)
bigram_mod = gensim.models.phrases.Phraser(bigram)
data_words_bigrams = []
for i in range(len(data)):
    data_words_bigrams.append(bigram_mod[data[i]])
print(data_words_bigrams[0])


# In[15]:


# Create the Dictionary for topic modeling
id2word = corpora.Dictionary(data_words_bigrams)
id2word


# In[16]:


# Create the Corpus for topic modeling
corpus = [id2word.doc2bow(text) for text in data_words_bigrams]
print(corpus[0])


# In[17]:


# Let's see what are these words
for word in corpus[0]:
    print(id2word[word[0]], word[1])


# In[18]:


# Build the topic model
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=20, # specify the number of topics
                                           random_state=100, # set a random seed so that each output will be the same
                                           update_every=1, # determine how often the model parameters should be updated
                                           chunksize=100, # number of documents to be used in each training chunk
                                           passes=10, # total number of training passes
                                           per_word_topics=True)


# # Analyzing the results

# In[19]:


# Print the keywords in the topics
for topics in lda_model.print_topics():
    print(topics)


# Topic 0 is a represented as 0.029*"death" + 0.026*"moral" + 0.016*"morality" + 0.015*"punishment" + 0.014*"criminal" + 0.012*"trial" + 0.012*"uk" + 0.011*"fair" + 0.011*"al" + 0.010*"islam". It means the top 10 keywords that contribute to this topic are: "death", "moral", "morality", etc., and the weight of "death" on topic 0 is 0.029. The weights reflect how important a keyword is to that topic. So it is reasonable to summarize the topic as "religion".

# # Task 2

# Summarize two additional topics (excluding topic 0) based on the top words in the topic (see output above). Analyze the common theme or subject that these topics convey through the frequent use of these top words. Include both your summarization (a single word or phrase) for these two topics and your rationale for the chosen summarization.

# 

# In[20]:


# Compute model coherence score, which measures how good a given topic model is
coherence_model_lda = CoherenceModel(model=lda_model, texts=data_words_bigrams, dictionary=id2word, coherence='c_v')
coherence_lda = coherence_model_lda.get_coherence()
print("Coherence LDA score:", coherence_lda)


# # Task 3

# Rebuild the topic model using a chunksize of 50 and 5 passes. Then print the topics generated by this updated model, and compute the new Coherence LDA score.
# <br> How has this new model affected the composition of the top words in topic 0, and do you find the top words in topic 0 in the old or the new model to be more coherent? Has the new Coherence LDA score increased or decreased compared with the original score, and what implications can be drawn from this change? Discuss the connection between the change in the Coherence LDA score and the changes in chunksize and passes.
# <br>Include your codes in the following cell (code) and the discussion in the next cell (markdown).

# In[21]:


lda_model_new = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=20, # specify the number of topics
                                           random_state=100, # setting a random seed so that each output will be the same
                                           update_every=1, # determines how often the model parameters should be updated
                                           chunksize=50, # number of documents to be used in each training chunk
                                           passes=5, # total number of training passes
                                           per_word_topics=True)

for topics in lda_model_new.print_topics():
    print(topics)
    
coherence_model_lda = CoherenceModel(model=lda_model_new, texts=data_words_bigrams, dictionary=id2word, coherence='c_v')
coherence_lda = coherence_model_lda.get_coherence()
print("Coherence LDA score:", coherence_lda)


# 

# In[22]:


# Finding the dominant topic in each document
count = 0
doc_id_list = []
dominant_topic_list = []
dominant_topic_weight = []
keywords_list = []
text_list = []
for doc in corpus:
    doc_id_list.append(count) # id of the document
    doc_topics = lda_model.get_document_topics(doc) # getting the distribution of topics
    doc_topics = sorted(doc_topics, key=lambda x: x[1], reverse=True) # sorting the topics
    dominant_topic_list.append(doc_topics[0][0]) # getting the most important topic's id
    dominant_topic_weight.append(doc_topics[0][1]) # getting the most important topic's weight
    topic_keywords = []
    for keyword in lda_model.show_topic(doc_topics[0][0]): # each keyword in that topic
        topic_keywords.append(keyword[0]) # adding each keyword to the topic keyword list
    keywords_list.append(topic_keywords)
    text_list.append(df.content.values.tolist()[count]) # getting the full text of the document
    count += 1
dominant_topic_df = pd.DataFrame({'Document ID': doc_id_list, 'Dominant Topic': dominant_topic_list,
                                 'Dominant Topic Weight': dominant_topic_weight, 'Keywords': keywords_list,
                                 'Text': text_list})
dominant_topic_df


# # Task 4

# Print the keywords of the document with index 51, along with the text of the document.
# <br>Provide a summary of the topic based on these keywords (in a single word or phrase). After reading the text, discuss whether the dominant topic truly reflects the main subject matter discussed in this document.
# <br>Include your codes in the following cell (code) and the discussion in the next cell (markdown).

# In[23]:


print(dominant_topic_df['Keywords'][51])
print(dominant_topic_df['Text'][51])


# 

# In[24]:


# Finding the most dominant document in each topic
topic_id_list = list(range(20)) # a list of topic IDs from 0 to 20
highest_weight_list = [0] * 20 # a list with 20 "0"s, will be replaced with larger values
highest_weight_document = [0] * 20
keywords_list = [0] * 20
text_list = [0] * 20
count = 0
for doc in corpus:
    doc_topics = lda_model.get_document_topics(doc) # getting the distribution of topics
    for topic in doc_topics:
        # for each topic, if the topic weight is larger than the current largest weight of that topic
        if topic[1] > highest_weight_list[topic[0]]:
            highest_weight_list[topic[0]] = topic[1] # update that value to this topic weight
            highest_weight_document[topic[0]] = count 
            # update the ID of the most dominant document of that topic to the ID of current document
            topic_keywords = []
            for keyword in lda_model.show_topic(topic[0]):
                topic_keywords.append(keyword[0])
            keywords_list[topic[0]] = topic_keywords # update the keywords to the keywords of current topic
            text_list[topic[0]] = df.content.values.tolist()[count] # update the text to the text of current document
    count += 1
dominant_document_df = pd.DataFrame({'Topic ID': topic_id_list, 'Keywords': keywords_list, 
                                     'Dominant Document': highest_weight_document, 
                                     'Dominant Document Weight': highest_weight_list, 
                                     'Text': text_list})
dominant_document_df


# # Task 5

# Based on what we have learned about topic modeling, can you suggest potential applications for this method? Please provide an example from either academic research or real-life situations and explain the advantages that topic modeling could offer in that context.

# 

# In[ ]:





# In[ ]:




