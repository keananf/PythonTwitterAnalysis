import pandas as pd, json, re, operator
from collections import defaultdict
from functools import reduce

stats = defaultdict(int)

def get_hashtags(df):
    """Decodes the JSON string that holds the hash tags
    
    This function uses a JSON decoder to parse the entities string
    to find the hashtags object, and then refines this to add the hashtags
    into a list attribute in this Tweet object
    :param df: the dataframe representing the data set
    :return the data frame representing the hashtags based on number of usages
    """
    hashtags = defaultdict(int)
    for htags in df.hashtags:
        obj = json.loads(htags)
        
        tags = [hashtag for hashtag in obj["hashtags"]]
        for tag in tags:
            hashtags[tag] += 1
            
    series = pd.Series(data=hashtags)
    series.sort_values(ascending=False, inplace=True)
    return series

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

def _count_types(dates):
    
    types = defaultdict(int)
    for tweet in dates:
        types[tweet] += 1
        
    return pd.Series(types)

def analyse_users(df):
    """Analyse the users and their tweets
    
    This function groups the df by users, and then calls a function
    to analyse each user based on the types of each tweet in their group.
    These are added to a series representing the row (1 user), and then
    added to the data frame.
    :param df: the dataframe representing the data set
    """
    user_group = df.groupby("from_user")
    users = [user for user, tweet in user_group]
    result = pd.DataFrame(index = users, 
                          columns = ["tweet", "retweet", "reply"])
    
    for user, tweets in user_group:
        result.loc[user] = _count_types(tweets.type)  
    
    result.fillna(0, inplace=True)
    stats["num_of_users"] = len(users)
    return result


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
   