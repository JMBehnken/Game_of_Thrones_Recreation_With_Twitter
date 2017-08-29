# Linking Game of Thrones characters in the final episode of season 7 by using their Twitter frequency

During the airing of the final Game of Thrones episode of season 7 the main hashtags have been streamed and saved by the Twitter-API. Around 2.000.000 Tweets have been gathered. This data is the basis for the following code.

From this unstructured Twitterdata I'm trying to recreate the relationships of the characters. Therefore I'm using their mentions in the Tweets and create a graph with gephi to visualize it.

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
