from refine import refine_data
from dataframes import create_dates, hashtag_distribution, analyse_users,\
    users_distribution
from series import create_hashtags_series, create_applications_series, create_hours_series
import pandas as pd
from analyse import stats, analyse_text, popular_hashtags
from graph import graph_dates, graph_hashtags_distrib, graph_hashtags, graph_applications, graph_users_distrib, graph_users, graph_hours, hashtag_wordcloud
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
    df = read_file("data/#digifest16.csv")
    refine_data(df)
    
    hours_series= create_hours_series(df)
    
    applications_series = create_applications_series(df)
    hashtag_series = create_hashtags_series(df)
    dates_df = create_dates(df)
    hashtag_distrib = hashtag_distribution(dates_df,hashtag_series)
    users_df = analyse_users(df)
    users_distrib = users_distribution(dates_df, users_df)
    analyse_text(df)
    print_results()
    user_stats(users_df)
    popular_hashtags(hashtag_series, 10)
   
    hashtag_wordcloud(hashtag_series) 
    graph_hours(hours_series)
    graph_applications(applications_series)
    graph_hashtags(hashtag_series)
    graph_dates(dates_df)
    graph_users(users_df)
    graph_hashtags_distrib(hashtag_distrib)
    graph_users_distrib(users_distrib)

if __name__ == '__main__':
    main()
