# Recreating Game of Thrones story in the final episode of season 7 by using Twitter Tweets

During the airing of the final Game of Thrones episode of season 7 the main hashtags have been streamed and saved by the Twitter-API. Around 2.000.000 Tweets have been gathered. This data is the basis for the following code.

From this unstructured Twitterdata I'm trying to recreate the relationships of the characters and recreate the main storyline. Therefore I'm using their mentions in the Tweets and create a graph with gephi to visualize it.

The code follows these steps:

1:
Searching the Tweets for grouped appearence of potential characternames

2:
Scraping the real names of all characters of the official Wikipediapage

3:
Matching the found names with the real names and map them to their pre- and surname

4:
Computing the weight of each linkage between two names by counting their appearence

5:
Saving the edges for further processing in gephi

6: Measuring the relative importance of characters to each other over time


# Attention!
There is no warranty for duplicated prenames to be mapped to the corresponding surname.
Detecting the correct mapping from the tweet context is not supported.
For example mentioning 'Jon'  will be interpreted as 'Jon Snow' [Main character] dropping the possibility of 'Jon Arryn' [Secondary character].
Checking the names for consistency is advisable.
