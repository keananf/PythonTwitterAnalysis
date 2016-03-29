import re, operator, json, pandas as pd
from functools import reduce
from collections import defaultdict

def _convert_time(date):
    return pd.to_datetime(date.split(" ")[0], format="%d/%m/%Y").isoformat().split("T")[0]

def _convert_hashtags(entities_string):
    
    obj = json.loads(entities_string)
    hashtags = [hashtag["text"] for hashtag in obj["hashtags"]]
    json_obj = {'hashtags': hashtags}
    
    return json.dumps(json_obj)

def tweet_type(text):
    """Function for ascertaining the numbers of types of tweet
  
    This function looks at the first element in the 
    text of the tweet and looks for "@username." Following, it
    checks the words in the text of the Tweet object for "RT" 
    and then sets the corresponding fields in the object.
    :param text: the text of a tweet
    """
    pattern = re.compile("@.")

    words = text.split(" ")
    if pattern.match(words[0]):
        return "reply"
    
    elif reduce(operator.__or__, map(lambda word: word == "RT", words)): 
        return "retweet"
    
    return "tweet"
  
def refine_data(df):
    """Eliminates unnecessary columns
    
    :param: the data frame representing all tweets in the data set
    """
    for column in ["in_reply_to_user_id_str","created_at","geo_coordinates","user_lang",
             "in_reply_to_status_id_str","in_reply_to_screen_name","status_url",
             "user_friends_count","from_user_id_str","user_followers_count","profile_image_url"]:
        df.pop(column)
        
    df['type'] = df['text'].map(tweet_type)
    df['time'] = df['time'].map(_convert_time)
    df['hashtags'] = df['entities_str'].map(_convert_hashtags)
    df.pop("entities_str")
    df.to_csv("../refined_digifest16.csv", index=False)

      
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


def refine_dates(df):
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
    #print(result)
    return result
