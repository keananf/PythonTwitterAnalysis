import re, operator, json, pandas as pd
from functools import reduce

def _get_day(date):
    return pd.to_datetime(date.split(" ")[0], format="%d/%m/%Y").isoformat().split("T")[0]

def _get_hour(date):
    return pd.to_datetime(date.split(" ")[1], format="%H:%M:%S").isoformat().split("T")[1].split(":")[0]


def _convert_hashtags(entities_string):
    """Reads in the entities string and looks for hashtags
    
    Parses the json entities string and looks for hashtags.
    These are added to a list, which
    is convert to a json object. This functions is mapped
    to the entire text column in the dataframe, so that a column 
    called "hashtags" is produced
    :param text: the entities string to be parsed
    :return a json object representing all hashtags
    """
    obj = json.loads(entities_string)
    hashtags = [hashtag["text"] for hashtag in obj["hashtags"]]
    json_obj = {'hashtags': hashtags}
    
    return json.dumps(json_obj)

def _tweet_type(text):
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
  
def _get_mentions(entities_string):
    """Reads in the entities string and looks for mentions
    
    Parses the json entities string and looks for mentions.
    These are added to a list, which
    is convert to a json object. This functions is mapped
    to the entire text column in the dataframe, so that a column 
    called "mentions" is produced
    :param text: the entities string to be parsed
    :return a json object representing all mentions
    """
    obj = json.loads(entities_string)
    mentions = [mentions["screen_name"] for mentions in obj["user_mentions"]]
    json_obj = {'mentions': mentions}
    
    return json.dumps(json_obj)
  
def refine_data(df):
    """Eliminates unnecessary columns
    
    :param: the data frame representing all tweets in the data set
    """
    for column in ["in_reply_to_user_id_str","created_at","geo_coordinates","user_lang",
             "in_reply_to_status_id_str", "status_url", "user_friends_count",
             "from_user_id_str","user_followers_count","profile_image_url"]:
        df.pop(column)
    
    df.drop_duplicates(["id_str"], inplace=True)
    
    df['type'] = df['text'].map(_tweet_type)
    df['day'] = df['time'].map(_get_day)
    df['hour'] = df['time'].map(_get_hour)
    df['mentions'] = df['entities_str'].map(_get_mentions)
    df['hashtags'] = df['entities_str'].map(_convert_hashtags)
    df.pop("entities_str")
    df.pop("time")
    df.to_csv("data/refined_digifest16.csv", index=False)

