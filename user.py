import operator
from functools import reduce
from analyse import stats

def user_stats(users_df):
    """Calls functions to calculate the means and std deviations

    """
    stats["mean_tweets"] = mean(users_df.tweet)
    stats["mean_retweets"] = mean(users_df.retweet)
    stats["mean_replies"] = mean(users_df.reply)
    stats["mean_replied"] = mean(users_df.replied)
    stats["mean_retweeted"] = mean(users_df.retweeted)
    stats["mean_mentions"] = mean(users_df.mentions)


    users_df['tweet_deviation'] = users_df['tweet'].map(lambda tweet: (tweet - stats["mean_tweets"]) ** 2)
    users_df['retweet_deviation'] = users_df['retweet'].map(lambda retweet: (retweet - stats["mean_retweets"]) ** 2)
    users_df['replies_deviation'] = users_df['reply'].map(lambda reply: (reply - stats["mean_replies"]) ** 2)

    users_df['replied_deviation'] = users_df['replied'].map(lambda tweet: (tweet - stats["mean_replied"]) ** 2)
    users_df['retweeted_deviation'] = users_df['retweeted'].map(lambda retweet: (retweet - stats["mean_retweeted"]) ** 2)
    users_df['mentions_deviation'] = users_df['mentions'].map(lambda reply: (reply - stats["mean_mentions"]) ** 2)

    stats["std_dev_tweets"] = std_dev(list(users_df.tweet_deviation))
    stats["std_dev_retweets"] = std_dev(list(users_df.retweet_deviation))
    stats["std_dev_replies"] = std_dev(list(users_df.replies_deviation))

    stats["std_dev_replied"] = std_dev(list(users_df.replied_deviation))
    stats["std_dev_retweeted"] = std_dev(list(users_df.retweeted_deviation))
    stats["std_dev_mentions"] = std_dev(list(users_df.mentions_deviation))

    print_stats()

def print_stats():
    """Prints the means and standard deviations
    """
    print("Number of Users: " + str(stats["num_of_users"]) + "\n")

    print("\nMean tweets per user: " + str(stats["mean_tweets"]))
    print("Mean RTs per user: " + str(stats["mean_retweets"]))
    print("Mean replies per user: " + str(stats["mean_replies"]) + "\n")

    print("\nMean user was replied: " + str(stats["mean_replied"]))
    print("Mean user was retweeted: " + str(stats["mean_retweeted"]))
    print("Mean user was mentioned: " + str(stats["mean_mentions"]) + "\n")

    print("Standard Deviation of tweets per user: " + str(stats["std_dev_tweets"]))
    print("Standard Deviation of RTs per user: " + str(stats["std_dev_retweets"]))
    print("Standard Deviation of replies per user: " + str(stats["std_dev_replies"]) + "\n")

    print("Standard Deviation of times user was replied: " + str(stats["std_dev_replied"]))
    print("Standard Deviation of times user was retweeted: " + str(stats["std_dev_retweeted"]))
    print("Standard Deviation of times user was mentioned: " + str(stats["std_dev_mentions"]) + "\n")

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
