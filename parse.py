from tweets import analyse_tweets
import pandas as pd
from analyse import user_stats, popular_hashtags, analyse_users
from graph import graph

def read_file():
    """Top level function for parsing the data set
    
    Dataset is parsed into a dataframe using pandas. A Tweets object
    is created comprised of individual Tweet objects (represented by a single
    line in the data set.
    :return the Tweets object representing all tweets in the data set
    """
    df = pd.DataFrame.from_csv("../#digifest16.csv")
    
    for column in ["in_reply_to_user_id_str","created_at","geo_coordinates","user_lang",
             "in_reply_to_status_id_str","in_reply_to_screen_name","status_url",
             "user_friends_count","from_user_id_str","user_followers_count","profile_image_url"]:
        df.pop(column)
    df.reset_index(inplace=True)
    return df

def print_results():
    """Top level function for printing out data
    
    """
    df = read_file()
    stats = analyse_tweets(df)
    analyse_users(df)
    
    print("Number of Tweets: " + str(stats["num_of_tweets"]))
    print("Number of RTs: " + str(stats["num_of_retweets"]))
    print("Number of Replies: " + str(stats["num_of_replies"]))
    print("Number of Users: " + str(stats["num_of_users"]) + "\n")
    user_stats()
    popular_hashtags(10)
    graph(df)
    

if __name__ == '__main__':
    print_results()