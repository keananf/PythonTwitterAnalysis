import pandas as pd, re, operator
from collections import defaultdict
from functools import reduce

stats = defaultdict(int)

def popular_hashtags(hashtags, limit = 5):
    """Prints out the most popular hashtags
    
    :param limit: the number of popular hashtags to print. 
    Defaults to 5
    """
    index = 0
    for tag, count in hashtags.iteritems():
        if(index == limit): break
        print(str(count) + ": " + tag)
        index += 1

def analyse_text(df):
    """Function for ascertaining the numbers of types of tweet
  
    This function looks at the first element in the 
    text of the tweet and looks for "@username." Following, it
    checks the words in the text of the Tweet object for "RT" 
    and then sets the corresponding fields in the object. 
    It does this for every tweet's text field.
    :param df: the dataframe representing the data set
    """
    pattern = re.compile("@.")
    
    for text in df.text:
        words = text.split(" ")
        if pattern.match(words[0]):
            stats["num_of_replies"] += 1
        
        if reduce(operator.__or__, map(lambda word: word == "RT", words)): 
            stats["num_of_retweets"] += 1
            
    stats["num_of_tweets"] = len(df.index)
   