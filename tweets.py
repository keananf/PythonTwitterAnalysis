import re, json, operator, datetime, pandas as pd
from functools import reduce
from collections import defaultdict

hashtags = defaultdict(lambda: 0) #set up dictionary with everything starting at 0
stats = defaultdict(lambda: 0)
    
def analyse_tweets(df):
    """Finds and returns the totals for each type of tweet
    
    :param df: the dataframe representing the data set
    :return a dictionary containing number of tweets, retweets
    and replies
    """
    stats = analyse_text(df["text"])
    get_hashtags(df["entities_str"])
    df['time'] = change_dates(df['time'])
    return stats


def analyse_text(text_list):
    """Function for ascertaining the numbers of types of tweet
  
    This function looks at the first element in the 
    text of the tweet and looks for "@username." Following, it
    checks the words in the text of the Tweet object for "RT" 
    and then sets the corresponding fields in the object. 
    It does this for every tweet.
    :param text_list: the list of 
    """
    pattern = re.compile("@.")
    
    for text in text_list:
        words = text.split(" ")
        if pattern.match(words[0]):
            stats["num_of_replies"] += 1
        
        if reduce(operator.__or__, map(lambda word: word == "RT", words)): 
            stats["num_of_retweets"] += 1
            
    return stats


def change_dates(dates):
    """Turns all date strings into datetime objects
    
    This function changes the 'time' column to be in iso format,
    so that is can later be graphed
    :param dates: the string representing the date
    :return the datetime object 
    """
    list_ = []
    for date_str in dates:
        date, time = date_str.split(" ")[0].split("/"), date_str.split(" ")[1].split(":")
        day, month, year = int(date[0]), int(date[1]), int(date[2])
        #hour, minutes, seconds = int(time[0]), int(time[1]), int(time[2])
        
        list_.append(datetime.datetime(year, month, day).isoformat())
        
    return pd.Series(data=list_)

def get_hashtags(entities_str_list):
        """Decodes the JSON string that holds the hash tags
        
        This function uses a JSON decoder to parse the entities string
        to find the hashtags object, and then refines this to add the hashtags
        into a list attribute in this Tweet object
        :param entities_str_list: the list of JSON strings containing the hash tags
        """
        for entities_str in entities_str_list:
            obj = json.loads(entities_str)
            
            tags = [hashtag["text"] for hashtag in obj["hashtags"]]
            for tag in tags:
                hashtags[tag] += 1
    