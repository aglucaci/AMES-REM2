#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import sys
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
#import os
from tqdm import tqdm
import numpy as np
import altair as alt
from vega_datasets import data
alt.data_transformers.enable('default', max_rows=None)


# In[3]:


df_tmalign = pd.read_csv(os.path.join("..", 
                         "tables", 
                         'TM_Align_Results.csv'), index_col=0)

#df_tmalign


# In[3]:


df_tn93 = pd.read_csv(os.path.join("..", 
                      "results", "TN93",
                      'tn93_rem2.dst'))

#df_tn93


# In[4]:


df_tmalign["Short_Name of Chain_1:"] = ""
df_tmalign["Short_Name of Chain_2:"] = ""

def parseName(name):
    parsed_name = name
    parsed_name = parsed_name.split("_")
    if "Node" in parsed_name[0]:
        parsed_name = parsed_name[0]
    else:
        parsed_name = "_".join(parsed_name[0:3])
    #end if
    return parsed_name
#end method

for index, row in tqdm(df_tmalign.iterrows()):
    id1 = row["Name of Chain_1:"]
    id2 = row["Name of Chain_2:"]
    
    # Parse names
    id1_parsed = parseName(id1)
    id2_parsed = parseName(id2)
    
    # dfmi.loc[:, ('one', 'second')]
    
    #df_tmalign.loc[:, ("Short_Name of Chain_1:", index)] = id1_parsed
    #df_tmalign.loc[:, ("Short_Name of Chain_2:", index)] = id2_parsed
    
    df_tmalign["Short_Name of Chain_1:"][index] = id1_parsed
    df_tmalign["Short_Name of Chain_2:"][index] = id2_parsed
#end for




# In[5]:


#df_tmalign


# In[6]:


df_tmalign["TN93"] = ""

for index, row in tqdm(df_tn93.iterrows()):
    id1_parsed = parseName(row["ID1"])
    id2_parsed = parseName(row["ID2"])
    distance =   row["Distance"]
    
    df = df_tmalign[df_tmalign["Short_Name of Chain_2:"] == id1_parsed]
    df2 = df[df["Short_Name of Chain_1:"] == id2_parsed]
    df_tmalign["TN93"][df2.index] = distance
    
    df = df_tmalign[df_tmalign["Short_Name of Chain_1:"] == id1_parsed]
    df2 = df[df["Short_Name of Chain_2:"] == id2_parsed]
    df_tmalign["TN93"][df2.index] = distance
        
    #break
    #print(df2.index[0])
    #break


# In[7]:


#df


# In[8]:


#df2


# In[9]:


#df_tmalign


# In[10]:


#df_tmalign[df_tmalign["TN93"] == ""]


# In[11]:

output_csv = os.path.join("..", 
                         "tables", 
                         'TM_Align_Results_with_GeneticDistance-Complete.csv')

print("# Saving data to:", output_csv)

df_tmalign.to_csv(output_csv)


# In[12]:


source = df_tmalign

rmsd = alt.Chart(source).mark_bar().encode(
    alt.X("RMSD=", bin=alt.Bin(step=0.001), title='RMSD'),
    y='count()',
)

tm = alt.Chart(source).mark_bar().encode(
    alt.X("Normalized_Average_TM_Score", bin=alt.Bin(step=0.001), title='TM-Score (Averaged)'),
    y='count()',
)

source["TN93"] = pd.to_numeric(source["TN93"])

tn93 = alt.Chart(source).mark_bar().encode(
    alt.X("TN93", bin=alt.Bin(step=0.005
                                ), title='TN93 genetic distance'),
    y='count()',
)

#rmsd | tm | tn93


# In[13]:


source = df_tmalign

chart = alt.Chart(source).mark_point(size=1).encode(
    x=alt.X('RMSD=', title='RMSD'),
    y=alt.Y('Normalized_Average_TM_Score', title='TM-Score (Averaged)')
)

chart_flip = alt.Chart(source).mark_circle(size=5).encode(
    y=alt.Y('RMSD='),
    x=alt.X('Normalized_Average_TM_Score')
)

#chart | chart_flip


#chart




# In[14]:


source = df_tmalign

chart = alt.Chart(source).mark_point(size=1).encode(
    x=alt.X('TN93', title='TN93'),
    y=alt.Y('RMSD=', title='RMSD')
)

chart2 = alt.Chart(source).mark_point(size=1).encode(
    x=alt.X('TN93', title='TN93'),
    y=alt.Y('Normalized_Average_TM_Score', title='TM Score (Averaged)')
)

#chart_flip = alt.Chart(source).mark_circle(size=5).encode(
#    y=alt.Y('RMSD='),
#    x=alt.X('Normalized_Average_TM_Score')
#)

#chart | chart_flip


#chart | chart2

#c  = alt.HConcat(chart, chart2)
#c = chart | chart2
#c.save('mychart.png', scale_factor=2.0)




# In[15]:


source = df_tmalign

chart = alt.Chart(source).mark_line(size=2).encode(
    x=alt.X('TN93', title='TN93'),
    y=alt.Y('RMSD=', title='RMSD')
)

chart2 = alt.Chart(source).mark_line(size=2).encode(
    x=alt.X('TN93', title='TN93'),
    y=alt.Y('Normalized_Average_TM_Score', title='TM Score (Averaged)')
)

#chart_flip = alt.Chart(source).mark_circle(size=5).encode(
#    y=alt.Y('RMSD='),
#    x=alt.X('Normalized_Average_TM_Score')
#)

#chart | chart_flip


#chart

#chart | chart2




# # End of file
# 

# In[16]:

