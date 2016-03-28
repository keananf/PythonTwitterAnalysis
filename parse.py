from refine import refine_dates, refine_data
import pandas as pd
from analyse import stats, get_hashtags, analyse_text, popular_hashtags, analyse_users
from graph import graph
from user import user_stats

def read_file(filename):
    """Top level function for parsing the data set
    
    Dataset is parsed into a dataframe using pandas. A Tweets object
    is created comprised of individual Tweet objects (represented by a single
    line in the data set.
    :param filename: the path for the csv file to process
    :return the data frame representing all tweets in the data set
    """
    df = pd.DataFrame.from_csv(filename)
    df.reset_index(inplace=True)
    
    return df

def print_results():
    """Top level function for printing out data
    
    :param df_hashtags: the dataframe representing the hashtags
    """
    print("Number of Tweets: " + str(stats["num_of_tweets"]))
    print("Number of RTs: " + str(stats["num_of_retweets"]))
    print("Number of Replies: " + str(stats["num_of_replies"]))
    
def main():
    df = read_file("../#digifest16.csv")
    refine_data(df)

    hashtags = get_hashtags(df)
    dates =refine_dates(df)
    users_df = analyse_users(df)

    analyse_text(df)
    print_results()
    user_stats(users_df)
    popular_hashtags(hashtags, 10)
    
    graph(hashtags, dates)

if __name__ == '__main__':
    main()