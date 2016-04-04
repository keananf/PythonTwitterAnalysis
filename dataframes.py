import json
import pandas as pd
from collections import defaultdict
from analyse import stats

def _count_tweet_types(tweets):
    """Creates dictionary for a certain day

    This dictionary has entries for retweets, tweets, and
    replies that are mapped to the number of occurrences
    on a particular day. Likewise, it has a dictionary for
    all the hashtags and their occurrences on the day, and users
    and their number of tweets each day
    :param tweets: the Series of tweets on this day
    """
    types = defaultdict(int)
    htags = defaultdict(int)
    unique_users = defaultdict(int)

    #tweet is type of tweet (retweet, tweet, or reply
    for tweet in tweets.type:
        types[tweet] += 1

    #hashtags is list of hashtags for a certain day
    for tags in tweets.hashtags:
        for tag in json.loads(tags)["hashtags"]:
            htags[tag] += 1

    #from_user is list of users who tweeted for a certain day
    for user in tweets.from_user:
        unique_users[user] += 1

    types['hashtags'] = htags
    types['users'] = unique_users
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
    day_group = df.groupby("day")
    days = [day for day, tweets in day_group]

    result = pd.DataFrame(index = days,
                          columns = ["tweet", "retweet", "reply", "hashtags", "users"])
    result.reset_index(inplace=True)

    for day, tweets in day_group:
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
    result = pd.DataFrame(index = hashtags_series.index)

    for date in all_dates.itertuples():
        result[index] = pd.Series(date[5])
        index += 1

    result.fillna(0, inplace=True)
    return result

def users_distribution(all_dates, users_df):
    """Makes a dataframe for users and tweets on each day

    This method looks through the dates dataframe and the
    users_df to create a unique data frame that has
    users and their respective tweet counts on each day, with
    each day being its own column, and each index being a unique user
    :param all_dates: the dates dataframe with hashtags, and number of tweets,
    retweets and replies for each day
    :param users_df: the dataframe representing unique users
    :return a new dataframe representing users and their number of tweets on each day
    """
    index = 0
    result = pd.DataFrame(index = users_df.index)

    for date in all_dates.itertuples():
        result[index] = pd.Series(date[6])
        index += 1

    result.fillna(0, inplace=True)
    return result

def _count_types(tweets):

    types = defaultdict(int)
    total = 0
    for tweet in tweets.type:
        types[tweet] += 1
        total += 1

    types["total"] = total
    return pd.Series(types)

def _count_mentions(df):

    mentions = defaultdict(int)
    for row in df.mentions:
        row = json.loads(row)
        for mention in row["mentions"]:
            mentions[mention] += 1

    return pd.Series(mentions)

def _count_replies(df):
    replies = defaultdict(int)
    replies_df = df[df['type'] == "reply"]
    for user in replies_df.in_reply_to_screen_name:
        replies[user] += 1
    return pd.Series(replies)

def _count_retweets(df):
    retweets = defaultdict(int)
    retweets_df = df[df['type'] == "retweet"]
    for row in retweets_df.mentions:
        row = json.loads(row)
        if(len(row["mentions"])):
            retweets[row["mentions"][0]] += 1

    return pd.Series(retweets)

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
                          columns = ["tweet", "retweet", "reply", "total"])

    for user, tweets in user_group:
        result.loc[user] = _count_types(tweets)

    result["mentioned"] = _count_mentions(df)
    result["replied"] = _count_replies(df)
    result["retweeted"] = _count_retweets(df)


    result.fillna(0, inplace=True)
    result.sort_values(by='total', ascending=False, inplace=True)
    stats["num_of_users"] = len(users)
    return result
