import operator
from functools import reduce
from analyse import stats

def user_stats(users_df):
    """Calls functions to calculate the means and std deviations
    
    """
    stats["mean_tweets"] = mean(users_df.tweet)
    stats["mean_retweets"] = mean(users_df.retweet)
    stats["mean_replies"] = mean(users_df.reply)
    
    users_df['tweet_deviation'] = users_df['tweet'].map(lambda tweet: (tweet - stats["mean_tweets"]) ** 2)
    users_df['retweet_deviation'] = users_df['retweet'].map(lambda retweet: (retweet - stats["mean_retweets"]) ** 2)
    users_df['replies_deviation'] = users_df['reply'].map(lambda reply: (reply - stats["mean_replies"]) ** 2)
    
    stats["std_dev_tweets"] = std_dev(list(users_df.tweet_deviation))
    stats["std_dev_retweets"] = std_dev(list(users_df.retweet_deviation))
    stats["std_dev_replies"] = std_dev(list(users_df.replies_deviation))
    
    print_stats()
    
def print_stats():
    """Prints the means and standard deviations
    """
    print("Number of Users: " + str(stats["num_of_users"]) + "\n")
    
    print("\nMean tweets per user: " + str(stats["mean_tweets"]))
    print("Mean RTs per user: " + str(stats["mean_retweets"]))
    print("Mean replies per user: " + str(stats["mean_replies"]) + "\n")

    
    print("Standard Deviation of tweets per user: " + str(stats["std_dev_tweets"]))
    print("Standard Deviation of RTs per user: " + str(stats["std_dev_retweets"]))
    print("Standard Deviation of replies per user: " + str(stats["std_dev_replies"]) + "\n")


def mean(list_):
    """Calculates the means for variables of each user
    
    This function calculates the mean of a list
    :param list_:The list to calculate the mean of
    :return the mean of the list
    """
    total = reduce(operator.__add__,list_)
    
    mean = total / stats["num_of_users"]
    return mean

def std_dev(list_):
    """Calculates the stats for variables of each user
    
    This function calculates the standard deviations.
    This calculation is performed by calculating the sum of the deviations between
    each member of the population and the mean squared, and then finding the mean of this sum.
    This value is then square rooted for the standard deviation
    :param list_:The list to calculate the standard deviation of
    :return the standard deviation of the population
    """
    sum_deviations = reduce(operator.__add__,list_)
    
    std_dev= (sum_deviations / stats["num_of_users"]) **0.5
    return std_dev
   