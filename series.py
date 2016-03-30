from collections import defaultdict
import json, re
import pandas as pd

def create_hashtags_series(df):
    """Decodes the JSON string that holds the hash tags
    
    This function uses a JSON decoder to parse the hashtags column
    to find the hashtags object, and then refines this to add the hashtags
    into a new series based on number of total occurrences
    :param df: the dataframe representing the data set
    :return the series representing the hashtags based on number of usages
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

def create_applications_series(df):
    """Analyse the days and their tweets
    
    This function groups the df by sources, and then creates a dictionary
    which maps each source to their number of uses.
    These are added to a series representing this distribution
    :param df: the dataframe representing the data set
    :return the dataframe representing the sources and occurrences
    """
    source_group = df.groupby("source")
    sources = defaultdict(int)
    pattern = re.compile("(<.+>)(.+)(</a>)")
    
    for source,tweets in source_group:
        m = pattern.match(source)
        if m:    
            sources[m.group(2)] += len(tweets.index)
        
            
    series = pd.Series(data=sources)
    series.sort_values(ascending=False, inplace=True)
    return series
