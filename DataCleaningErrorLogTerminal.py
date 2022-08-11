#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning Error Log for APS Data
# ### Run Script in Jupyter and scroll to the end to get full error log

# In[1]:


import pandas as pd
from IPython.display import display, HTML
from datetime import datetime 
import re


from spellchecker import SpellChecker
spell = SpellChecker()

spell.word_frequency.load_text_file('./streetdict.txt')
spell.word_frequency.load_text_file('./customdict.txt')

pd.options.mode.chained_assignment = None  # default='warn'


# #### Import Excel File
# ##### Make sure excel is in the same directory as the project, is named 'accessible-pedestrian-signals.xlsx' and has 3 columns tittled "Location", "Borough" and "Date Installed" 

# In[2]:


# Read excel file
df = pd.read_excel('accessible-pedestrian-signals.xlsx')
# Match pandas dataframe index with Excel row
df.index = df.index + 2
# print DataFrame head
df.head()


# ---
# ## Rows with missing data
# #### Will be empty if no data is missing

# In[3]:


null_errors = df[df.isna().any(axis=1)]
null_errors['Error'] =  'Missing Data'
null_errors


# ---
# ## Rows with duplicate data
# #### Will be empty if no data is duplicated

# In[4]:


duplicate_data = df[df.duplicated()] 
duplicate_data['Error'] = ' Duplicate Data'
duplicate_data


# ---
# ## Date Column Error Checking
# #### Return all entries that have an invalid date
# 

# In[5]:


#Remove missing rows
df2 = df.dropna(subset = ['Date Installed'])

date_errors = df2['Date Installed'] = pd.to_datetime(df2['Date Installed'], errors='coerce')
date_errors = df2.loc[df2['Date Installed'].isnull()]
date_errors['Error'] = 'Date is invalid'

date_errors


# ---
# ## Borough Column Error Checking
# #### Return all entries that have an invalid borough

# In[12]:


#Remove missing rows
df3 = df.dropna(subset = ['Borough'])

borough_errors = df3.loc[(df3['Borough'] != 'Brooklyn') & (df3['Borough'] != 'Queens') 
       & (df3['Borough'] != 'the Bronx') & (df3['Borough'] != 'Bronx')
                       & (df3['Borough'] != 'Manhattan') & (df3['Borough'] != 'Staten Island')]

borough_errors['Error'] = 'Borough spelling, capitalization or type'

borough_errors


# ---
# ## Location Column Error Checking
# 
# ### Abbreviations checked for consistency:
# #### St (Street or Saint), Ave (Avenue), Blvd (Boulevard), Dr (Drive), Expy (Expressway)
# #### Pkwy (Parkway), Pl(Place), Rd (Road), TER (Terrace)

# In[7]:


# Returns the abbreviation contained in the abbrev_errors dataframe
def findabbrev(misspelled):
    list2 =['ST', 'ST.','AVE', 'BLVD','DR', 'EXPY', 'PKWY', 'PL','RD', "TER" ]
    abbrevlist=[]
    for name in misspelled:
        name = name.upper()
        if name in list2:
            abbrevlist.append(name)
    return abbrevlist

#Create 'abbrev_errors' dataframe with data that contains abbreviations
#Regex checks if word is by itself, '(?i)' makes the search case insensitive
abbrev_errors = df[df['Location'].str.contains(r"(?i)\bSt\b|\bAve\b|\bBlvd\b|\bDr\b|\bExpy\b|\bPkwy\b|\bPl\b|\bRd\b|\bTer\b")== True]
abbrev_errors['Abbreviation'] = abbrev_errors['Location'].str.split().apply(findabbrev)
abbrev_errors['Error']= 'Contains abbreviation:  ' + abbrev_errors['Abbreviation'].astype(str)
abbrev_errors.drop(columns =['Abbreviation'], axis=1, inplace=True)

abbrev_errors


# ---
# ## Check Location Column for Street Spelling
# #### Prepping the data for Error Checking

# In[8]:


#Remove missing rows
LocationSpellingErrors = df.dropna(subset = ['Location'])

#Replace special characters with whitespace in order to extract words
LocationSpellingErrors['Location'] = LocationSpellingErrors['Location'].str.replace('(',' ', regex=True)
LocationSpellingErrors['Location'] = LocationSpellingErrors['Location'].str.replace(')',' ', regex=True)
LocationSpellingErrors['Location'] = LocationSpellingErrors['Location'].str.replace('-',' ', regex=True)
LocationSpellingErrors['Location'] = LocationSpellingErrors['Location'].str.replace(',',' ', regex=True)
LocationSpellingErrors['Location'] = LocationSpellingErrors['Location'].str.replace("’",' ', regex=True)
LocationSpellingErrors['Location'] = LocationSpellingErrors['Location'].str.replace("'",' ', regex=True)
LocationSpellingErrors['Location'] = LocationSpellingErrors['Location'].str.replace("/",' ', regex=True)
LocationSpellingErrors['Location'] = LocationSpellingErrors['Location'].str.replace(".",' ', regex=True)

#Split Location Column into Substrings
LocationSpellingErrors['Split_words'] = LocationSpellingErrors['Location'].str.split()


# In[9]:


#Store rows with data type error in 'LocationSpellingErrors' dataframe
LocationTypeError = LocationSpellingErrors[LocationSpellingErrors['Split_words'].isna()]
LocationTypeError['Error']= 'Location entry not valid'
LocationTypeError.drop(columns =['Split_words'], axis=1, inplace=True)
LocationSpellingErrors = LocationSpellingErrors.dropna(subset = ['Split_words'])

#Store rows with insufficient words in 'LocationLengthError' dataframe
#Column contains less than 3 words
LocationLengthError = LocationSpellingErrors[LocationSpellingErrors['Split_words'].map(lambda d: len(d)) < 4]
LocationLengthError['Error']= 'Location entry not complete'
LocationLengthError.drop(columns =['Split_words'], axis=1, inplace=True)


# In[10]:


# Use PySpellChecker library to find misspelt words
def incorrectlist(stlist):
    return spell.unknown(stlist)

# Use PySpellChecker library to find potential corrections to misspelt words
def correctlist(misspelled):
    correctwords=[]
    for word in misspelled:
        correctwords.append(spell.correction(word))
        return correctwords


LocationSpellingErrors['Incorrect Words'] = LocationSpellingErrors['Split_words'].apply(incorrectlist).tolist()
LocationSpellingErrors = LocationSpellingErrors[LocationSpellingErrors['Incorrect Words'].map(lambda d: len(d)) > 0]
LocationSpellingErrors['Potential word'] = LocationSpellingErrors['Incorrect Words'].apply(correctlist).tolist()
LocationSpellingErrors["Error"] = "Location Spelling Error: " + LocationSpellingErrors['Incorrect Words'].astype(str)
LocationSpellingErrors.drop(columns =['Split_words', 'Incorrect Words','Potential word'], axis=1, inplace=True)
LocationSpellingErrors


# ---
# ## Full Error Log
# ### Errors are also exported in an excel file in the project directory
# #### You can remove a specific error check by deleting it from the 'frames' 
# 

# In[14]:


frames = [null_errors, duplicate_data, borough_errors, date_errors, 
          LocationTypeError,LocationLengthError, LocationSpellingErrors, abbrev_errors]
result = pd.concat(frames)

# Sort errors by row index
result.sort_index(inplace=True)
#Label row
result.index.rename('Row', inplace=True)


if len(result.index) == 0:
    print('No Errors Found')
else:
#     Restore values of original dataframe that may have been converted to 'NA'
    result.drop(columns =['Location', 'Borough', 'Date Installed'], axis=1, inplace=True)
    print(str(len(result.index)) +' Errors Found')
    display(result)
#     Export Errors in an excel file
    result.to_excel('errors.xlsx')


# In[ ]:




