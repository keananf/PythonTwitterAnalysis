import operator
from functools import reduce
from user import users, User
from tweets import hashtags, stats

def popular_hashtags(limit = 5):
    """Prints out the most popular hashtags
    
    :param limit: the number of popular hashtags to print. 
    Defaults to 5
    """
    pop_tags = [tag for tag in sorted(hashtags.__iter__(),key=hashtags.get,reverse=True)]
    index = 0
    for tag in pop_tags:
        if(index == limit): break
        print(str(hashtags[tag]) + ": " + tag)
        index += 1

def analyse_users(df):
    """Analyse the users and their tweets
    
    :param df: the dataframe representing the data set
    """
    row_num = 0
    for user in df["from_user"]:
        if users.__contains__(user):
            users[user].num_of_tweets += 1
        else:
            users[user] = User(user)
            
        users[user].add(df.iloc[row_num])
        row_num += 1
                
    stats["num_of_users"] = users.__len__()
    stats["num_of_tweets"] = row_num
    
def user_stats():
    """Calls functions to calculate the means and std deviations
    
    """
    stats["mean_tweets"] = mean([user.num_of_tweets for user in users.values()])
    stats["mean_retweets"] = mean([user.num_of_retweets for user in users.values()])
    stats["mean_replies"] = mean([user.num_of_replies for user in users.values()])
    
    stats["std_dev_tweets"] = std_dev([(user.num_of_tweets - stats["mean_tweets"]) ** 2 for user in users.values()])
    stats["std_dev_retweets"] = std_dev([(user.num_of_retweets - stats["mean_retweets"]) ** 2 for user in users.values()])
    stats["std_dev_replies"] = std_dev([(user.num_of_replies - stats["mean_replies"]) ** 2 for user in users.values()])
    
    print_stats()
    
def print_stats():
    """Prints the means and standard deviations
    """
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
    