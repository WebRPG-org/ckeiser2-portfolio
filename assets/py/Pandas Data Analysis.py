#!/usr/bin/env python
# coding: utf-8

# # Dataframe Basics

# In[1]:


# Import Pandas library
import pandas as pd


# In[2]:


# Set display settings (by default, 60 rows and 20 columns)
pd.options.display.max_rows = 100


# In[5]:


# Read the csv file
data = pd.read_csv('Data/Trans_Atlantic_Slave_Trade.csv', delimiter=",", low_memory=False)
data


# In[6]:


# Display first n rows
data.head(10)


# In[7]:


# Display random sample
data.sample(10)


# In[8]:


# Get info
data.info()


# In[9]:


# Calculate summary statistics
data.describe()


# In[10]:


data.describe(include='all')


# In[11]:


# Create a new dataframe
new_dataframe = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
)
new_dataframe


# # Select Columns and Rows

# In[12]:


# Select columns
data['Captain\'s name'] # using backslash to "escape", so that "'" is read as a literal character and not as the end of a string


# In[13]:


type(data['Captain\'s name'])


# In[14]:


data[['Captain\'s name']]


# In[15]:


type(data[['Captain\'s name']])


# In[16]:


data[['Captain\'s name', 'Crew deaths during voyage', 'Crew at first landing of captives']]


# In[17]:


# Select rows
data[data['Crew deaths during voyage'] >= 10]


# In[18]:


data['Crew deaths during voyage'] >= 10


# In[19]:


data.loc[2, "Captain's name"]


# In[20]:


data.loc[2:4, ["Captain's name", "Crew deaths during voyage"]]


# In[21]:


data.iloc[2, 0]


# In[22]:


data.iloc[2:5, 0:2]


# In[23]:


significant_death_filter = data['Crew deaths during voyage'] >= 20
significant_death_data = data[significant_death_filter]
significant_death_data


# In[24]:


# Write to csv
significant_death_data.to_csv('Data/significant_death_data.csv', index=False)


# In[25]:


significant_death_data_new = pd.read_csv('Data/significant_death_data.csv')
significant_death_data_new


# # Missing Data

# In[26]:


# .isna() / .notna()
data['Crew deaths during voyage'].notna()


# In[27]:


data[data['Crew deaths during voyage'].notna()]


# In[28]:


data['Crew deaths during voyage'].isna().value_counts()


# In[29]:


# Proportion
data['Crew deaths during voyage'].isna().value_counts(normalize=True)


# In[30]:


# Value counts
data['Captain\'s name'].value_counts()


# In[31]:


# Because the .count() method always excludes NaN values, we can also count the number of values in each column 
# and divide by the total number of rows in each column (len()) to find the percentage of not blank data in every column.
data.count() / len(data)


# In[32]:


# .fillna()
data['Crew deaths during voyage'].fillna('no crew death information recorded')


# # Columns

# In[ ]:


# Rename columns
data.rename(columns={'Captain\'s name': 'Name of the Captain'})


# In[33]:


data


# In[34]:


data = data.rename(columns={'Captain\'s name': 'Name of the Captain'})
data


# In[35]:


# Drop columns
data = data.drop(columns=['First place where captives were landed', 'First place where captives were purchased'])
data


# In[36]:


# Add columns
data['Crew_not_dead'] = data['Crew at voyage outset'] - data['Crew deaths during voyage']
data[['Crew at voyage outset', 'Crew deaths during voyage', 'Crew_not_dead']]


# In[38]:


# Sort rows
data.sort_values(by='Crew deaths during voyage', ascending=False)


# # Calculations

# In[39]:


# Mean = average
data['Crew deaths during voyage'].mean()


# In[40]:


# Maximum
data['Crew deaths during voyage'].max()


# In[41]:


# Standard deviation
data['Crew deaths during voyage'].std()


# # Clean and Transform Data

# In[42]:


# Upper case
data['Name of the Captain'].str.upper()


# In[43]:


# Lower case
data['Name of the Captain'].str.lower()


# In[44]:


# Replace characters
data['Name of the Captain'] = data['Name of the Captain'].str.replace('é', 'e')
data['Name of the Captain']


# # Applying Functions

# In[45]:


def make_text_upper_case(text):
    upper_case_text = text.upper()
    return upper_case_text


# In[46]:


make_text_upper_case('Renault, Jacques-Joseph-Fr')


# In[47]:


data['Name of the Captain'][:10].apply(make_text_upper_case)


# # Merge DataFrames

# In[48]:


sub_data1 = data[['Name of the Captain', 'Crew deaths during voyage', 'Crew at first landing of captives', 'Voyage ID']]
sub_data1


# In[49]:


sub_data2 = data[['Crew at voyage outset', 'Date vessel departed with captives', 'Date vessel departed for homeport', 'Voyage ID']]
sub_data2


# In[50]:


pd.merge(sub_data1, sub_data2, on='Voyage ID')


# # Make and Save Plots

# In[51]:


# Barplot
data['Name of the Captain'].value_counts()[:10].plot(kind='bar', title='Most frequent Captain\'s name')


# In[52]:


# Horizontal barplot
data['Name of the Captain'].value_counts()[:10].plot(kind='barh', title='Most frequent Captain\'s name')


# In[53]:


# Save figure
ax = data['Crew deaths during voyage'].value_counts()[:10].plot(kind='bar', title='Most_Frequent_Number_of_Crew_Death')
ax.figure.savefig('Data/Most_frequent_number_of_crew_death')


# # Group by Columns

# In[54]:


data.groupby('Flag of vessel')


# In[55]:


data.groupby('Flag of vessel').count()


# In[56]:


# Groupby and sum
data.groupby('Flag of vessel')[['Crew deaths during voyage']].sum()


# In[57]:


# Group by two columns
death_by_captain_and_country = data.groupby(['Name of the Captain', 'Flag of vessel'])['Crew deaths during voyage'].mean()
death_by_captain_and_country


# In[58]:


# Reset index
death_by_captain_and_country = death_by_captain_and_country.reset_index()
death_by_captain_and_country


# In[59]:


# Pivot table
pivot_table = death_by_captain_and_country.pivot(index='Flag of vessel', columns='Name of the Captain', values='Crew deaths during voyage')
pivot_table


# In[60]:


# Make time series
data.groupby('Year of arrival at port of disembarkation').sum(numeric_only=True).reset_index()


# In[63]:


# Plotting time series
crew_death_by_year = data.groupby('Year of arrival at port of disembarkation')['Crew deaths during voyage'].sum()


# In[62]:


crew_death_by_year.plot()


# In[64]:


# Plotting multiple timeseries
crew_first_landing_by_year = data.groupby('Year of arrival at port of disembarkation')['Crew at first landing of captives'].sum()


# In[65]:


ax = crew_death_by_year.plot(kind='line', legend= True)
crew_first_landing_by_year.plot(ax=ax, legend=True)


# # Task 1

# In[67]:


# Add new columns 'Male_Number', 'Female_Number', 'Boys_Number', 'Girls_Number' by multiplying the 'Total embarked' column
# and columns of related percentages. Create a dataframe called 'male_and_female_number' including columns 'Male_Number',
# 'Female_Number', and 'Voyage ID', and a dataframe called 'boys_and_girls_number' including columns 'Boys_Number', 
# 'Girls_Number', and 'Voyage ID', and merge the two dataframes.
# Add columns# Add columns
data['Total embarked'] * data.count()['percent men'] * data.count()['percent women']
data[['Male_Number', 'Female_Number','Boys_Number', 'Girls_Number']]
male_and_female_number = pd.DataFrame({data[['Male_Number', 'Female_Number', 'Voyage ID']]})
boys_and_girls_number = pd.DataFrame({data[['Boys_Number', 'Girls_Number', 'Voyage ID']]})

pd.merge(male_and_female_number, boys_and_girls_number, on ='Voyage ID')



# # Task 2

# In[ ]:


# Write a function that converts the text in the column 'Vessel owner' into standarized format 'First_name Last_name',
# instead of 'Last_name, First_name', and apply the function to the 'Vessel owner' column.
# Note that there are some 'nan's, you can use 'isinstance(text, str)' as a conditional to handle this issue.









# # Task 3

# In[ ]:


# Calculate the mean percentage of boys by year using the columns 'Year of arrival at port of disembarkation' and 'Percent boys'
# and similarly, the mean percentage of girls by year. Plot both of them in a lineplot, and give it a title.








# # Task 4

# In[ ]:


# Calculate the mean 'Standardized tonnage' by year ('Year of arrival at port of disembarkation') and country ('Flag of vessel')
# and use 'pivot' to plot the mean 'Standardized tonnage' of each country by year in a lineplot, and give it a title.
# The plot should contain 10 lines, each representing the change of a country by year. 








# # Task 5

# In[ ]:


# Calculate the max and mean value in percentages of boys, girls, men, and women, and create a dataframe to store the results.
# Plot the results in a barplot and change the index to be 'Boys', 'Girls', 'Men', and 'Women'.
# The plot should contain 4 indexes, each with two bars, representing max percentage and mean percentage respectively.








