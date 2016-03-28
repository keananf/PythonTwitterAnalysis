import re, operator, pandas as pd
from functools import reduce
from collections import defaultdict

def _convert_time(date):
    return pd.to_datetime(date.split(" ")[0], format="%d/%m/%Y").isoformat().split("T")[0]

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
    df.to_csv("../refined_digifest16.csv", index=False)


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
        
def _count_types(dates):
    
    types = defaultdict(int)
    for tweet in dates:
        types[tweet] += 1
        
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
                          columns = ["tweet", "retweet", "reply"])

    result.reset_index(inplace=True)
    for time, tweets in time_group:
        result.loc[index] = _count_types(tweets.type) 
        index += 1 
    
    result.fillna(0, inplace=True)
    return result
