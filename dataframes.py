import json
import pandas as pd
from collections import defaultdict
      
def _count_tweet_types(tweets):
    """Creates dictionary for a certain day
    
    This dictionary has entries for retweets, tweets, and 
    replies that are mapped to the number of occurrences
    on a particular day. Likewise, it has a dictionary for 
    all the hashtags and their occurrences on the day
    :param tweets: the Series of tweets on this day
    """
    types = defaultdict(int)
    htags = defaultdict(int)
    
    #tweet is type of tweet (retweet, tweet, or reply
    for tweet in tweets.type:
        types[tweet] += 1
    
    #hashtags is list of hashtags for a certain day
    for tags in tweets.hashtags:
        for tag in json.loads(tags)["hashtags"]:
            htags[tag] += 1
 
    types['hashtags'] = htags
    return pd.Series(types)


def create_dates(df):
    """Analyse the days and their tweets
    
    This function groups the df by dates, and then calls a function
    to analyse each date based on the types of each tweet in their group.
    These are added to a series representing the row (1 day), and then
    added to the data frame.
    :param df: the dataframe representing the data set
    :return the dataframe representing the dates' activity
    """
    index = 0
    time_group = df.groupby("time")
    times = [time for time,tweets in time_group]
    
    result = pd.DataFrame(index = times, 
                          columns = ["tweet", "retweet", "reply", "hashtags"])
    result.reset_index(inplace=True)
    
    for time, tweets in time_group:
        result.loc[index] = _count_tweet_types(tweets) 
        index += 1 
    
    result.fillna(0, inplace=True)
    return result

def hashtag_distribution(all_dates, hashtags_series):
    """Makes a dataframe for hashtags and daily occurrences
    
    This method looks through the dates dataframe and the
    hashtags_series to create a unique data frame that has
    hashtags and their respective occurrences on each day, with
    each day being its own column, and each index being a unique hashtag
    :param all_dates: the dates dataframe with hashtags, and number of tweets, 
    retweets and replies for each day
    :param hashtags_series: the series of hashtags with total occurrences. 
    :return a new dataframe representing hashtags and their occurrences on each day
    """
    index = 0
    tags = [tag for tags in all_dates.hashtags for tag in tags]
    
    result = pd.DataFrame(index = hashtags_series.index)
    
    for date in all_dates.itertuples():
        result[index] = pd.Series(date[5])
        index += 1
    
    result.fillna(0, inplace=True)
    return result
