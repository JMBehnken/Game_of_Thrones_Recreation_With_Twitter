# Import
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import itertools
import requests
import nltk
import sys
import re


# Loading the streamed data
data_path = sys.argv[1]
edge_path = '/build/GoT_edges.csv'


df = pd.read_csv(data_path, parse_dates=[0])
# Shifting the timestamp to fit MESZ
df['created_at'] = df['created_at'] + pd.Timedelta(hours=2)


stop = set(nltk.corpus.stopwords.words())

names = {}
# Looking for the characters names in the tweets
# Fortunately most of the names are capitalized
pattern = re.compile("[^#@A-Za-z]([A-Z][a-z]+)")
# Iterating over each tweet
for tweet in df['text'].values:
    # Sorting the names alphabetical helps mapping them to the correct prename and surname afterwards
    potential_name = sorted(set(re.findall(pattern, tweet)))
    # Iterating over every possible combination of potential names
    for name_1, name_2 in itertools.combinations(potential_name, 2):
        # Checking for proper names and excluding common words
        if len(stop.intersection([name_1.lower(), name_2.lower()]))==0:
            # Counting their frequency to compute an edgeweight
            key = name_1+' '+name_2
            if key in names.keys():
                names[key] += 1
            else:
                names[key] = 1


# Scraping the official wikipediapage to get the real characternames
url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_characters'
html = requests.get(url).text
bs = BeautifulSoup(html, 'lxml')

official_names = []
# Since there are so many names, some prenames are ambiguous
# Therefore secondary characters are scraped first
# Duplicated names will be overwritten by main characters afterwards
for liste in bs.findAll('div', {'class':'div-col columns column-width'}):
    # Scraping secondary characters
    for line in liste.findAll('li'):
        official_names.append(line.get_text().split(' as ')[-1].replace('young ', ''))

for table in bs.findAll('table', {'class':'wikitable'}):
    # Scraping main characters
    for tr in table.findAll('tr'):
        try:
            official_names.append(tr.findAll('td')[1].get_text())
        except:
            pass

# Creating a mapping-dict for names
name_dict = {name.split(' ')[0]:name for name in official_names}
name_dict.update({' '.join(sorted(name.split(' '))):name for name in official_names})

# Attention!
# There is no warranty for duplicated prenames to be mapped to the corresponding surname
# Detecting the correct mapping from the tweet context is not supported
# For example mentioning 'Jon'  will be interpreted as 'Jon Stark' [Main character]
# dropping the possibility of 'Jon Arryn' [Secondary character]


edges = []
# Iterating over every found name
for name, count in names.items():
    name_1, name_2 = name.split(' ')
    # Checking for every name separatly eliminates selfloops
    if name_1 in name_dict.keys() and name_2 in name_dict.keys():
        # Adding weight information and type of the edge for further processing in gephi
        edges.append([name_dict[name_1], name_dict[name_2], np.log(count), 'Undirected'])


# Saving the edges
edges_df = pd.DataFrame(edges, columns=['Source', 'Target', 'Weight', 'Type'])
edges_df.to_csv(edge_path, index=False)
