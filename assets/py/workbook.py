#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install altair vega_datasets')


# In[2]:


import altair as alt


# In[3]:


chart1 = alt.Chart.from_dict({
    "data":{"url":"https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/bfro_reports_fall2022.csv"},
    "mark":"bar",
    "width":600,
    "encoding":{
    "x":{"bin":True,"field":"humidity", "type":"quantitative", "title":"Humidity_Levels"},
    "y":{"field":"state", "type":"ordinal"},
    "color":{"aggregate":"count","type":"quantitative"}
  } 
    
})


# In[4]:


chart1


# In[5]:


myJekyllDir = '/Users/colto/ckeiser2.github.io/assets/json/'


# In[6]:


chart1.properties(width='container').save(myJekyllDir+'chart1.json')


# In[7]:


chart2 = alt.Chart.from_dict({
    "data":{"url":"https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/bfro_reports_fall2022.csv"},
    "mark":"bar",
    "width":600,
    "encoding":{
    "x":{"bin":True,"field":"precip_probability", "type":"quantitative", "title":"Chance of Rain %"},
    "y":{"field":"state", "type":"ordinal"},
    "color":{"aggregate":"count","type":"quantitative"}
  } 
    
})


# In[8]:


chart2


# In[9]:


chart = alt.HConcatChart(hconcat=[chart1,chart2])


# In[10]:


chart


# In[11]:


chart.save(myJekyllDir + 'Humidity_ChanceofRain_Dashboard.json')


# In[12]:


brush = alt.selection_interval(encodings=['x','y'])


# In[13]:


chart1 = alt.Chart.from_dict({
    "data":{"url":"https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/bfro_reports_fall2022.csv"},
    "mark":"bar",
    "width":600,
    "encoding":{
    "x":{"bin":True,"field":"humidity", "type":"quantitative", "title":"Humidity_Levels"},
    "y":{"field":"state", "type":"ordinal"},
    "color":{"aggregate":"count","type":"quantitative"}
  } 
    
}).add_selection(
    brush
)


# In[14]:


chart2 = alt.Chart.from_dict({
    "data":{"url":"https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/bfro_reports_fall2022.csv"},
    "mark":"bar",
    "width":600,
    "encoding":{
    "x":{"bin":True,"field":"precip_probability", "type":"quantitative", "title":"Chance of Rain %"},
    "y":{"field":"state", "type":"ordinal"},
    "color":{"aggregate":"count","type":"quantitative"}
  } 
    
}).transform_filter(
    brush
)


# In[15]:


chart = chart1 | chart2


# In[16]:


chart


# In[17]:


chart.save(myJekyllDir + 'side_by_side_humidity_RainChance.json')


# In[ ]:





# In[ ]:





# In[ ]:




