import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import mpl_toolkits.mplot3d
from collections import defaultdict

dates_dict = defaultdict(lambda: 0)
 
def graph_hours(hours_series):
    """Prints graph for hours vs tweets during the event
    
    Prints a histogram for the hours of the event, with values being
    the number of tweets in the hour
    :param hours_series: the series describing the hours and numbers of occurrences.
    """
    fig = plt.figure(figsize=(15,6))
    plot = fig.add_subplot(111)
    
    hours = [hour for hour, num_tweets in hours_series.iteritems()]

    x = range(len(hours)) #spacing 
    y = [num_tweets for hour, num_tweets in hours_series.iteritems()] #values
    width = 0.25
    
    plot.bar(x, y, width, color="g")
    plot.set_title("Number of Tweets vs Hour of Event")
    plot.set_ylabel("Number of Tweets")
    plot.set_xlabel("Hour")
    plot.set_xticks(x)
    
    xticks = plot.set_xticklabels(hours)
    plt.setp(xticks, rotation=45, fontsize=13)
    
    plt.show()
    fig.savefig("pop-hours.png")


def graph_hashtags_distrib(hashtags_distrib):
    """Plots a 3D graph of hashtags and their occurrences on each day
    
    :param hashtags_distrib: The dataframe representing the number of 
    each hashtag per day. 
    """
    fig = plt.figure(figsize=(20,15))
    plot = fig.add_subplot(111, projection = '3d')
    
    hashtags = [tag for tag in hashtags_distrib.index][1:5]
    ylabels =[]
    
    column = 1
    for colour, tag in zip(['r', 'g', 'b', 'y'], hashtags):
        row = pd.DataFrame(hashtags_distrib.loc[tag])
        xs = range(0, len(row.index)) 
        ys = row[tag] #amount of this hashtag on this day
    
        plot.bar(xs, ys, zs = column, zdir='y', color = colour, alpha=0.8)
        ylabels.append(tag)
        ylabels.append("")
        column += 1
    
        
    plot.set_title("Hashtags vs Occurrences vs Day")
    plot.set_ylabel("Hashtag")
    plot.set_xlabel("Day")
    plot.set_zlabel("Occurrences")
    
    plot.set_xticks(range(0,len(hashtags_distrib.columns)))
    plot.set_xticklabels(list(hashtags_distrib.columns.values))
    plot.set_yticklabels(ylabels)
    
    plt.show()
    fig.savefig("hashtag-distrib.png")


def graph_users_distrib(users_distrib):
    """Plots a 3D graph of users and their occurrences on each day
    
    :param users_distrib: The dataframe representing the number of 
    each tweets each user posted per day. 
    """
    fig = plt.figure(figsize=(20,15))
    plot = fig.add_subplot(111, projection = '3d')
    
    users = [user for user in users_distrib.index][0:4]
    ylabels =[]
    
    column = 1
    for colour, user in zip(['r', 'g', 'b', 'y'], users):
        row = pd.DataFrame(users_distrib.loc[user])
        xs = range(0, len(row.index)) 
        ys = row[user] #amount of this hashtag on this day
        
        plot.bar(xs, ys, zs = column, zdir='y', color = colour, alpha=0.8)
        ylabels.append(user)
        ylabels.append("")
        column += 1
    
        
    plot.set_title("Users vs Number of Tweets vs Day")
    plot.set_ylabel("User")
    plot.set_xlabel("Day")
    plot.set_zlabel("Number of Tweets")
    
    plot.set_xticks(range(0,len(users_distrib.columns)))
    plot.set_xticklabels(list(users_distrib.columns.values))
    plot.set_yticklabels(ylabels)
    
    plt.show()
    fig.savefig("users-distrib.png")

def graph_users(users_df):
    """Plots the number of times users interacted with eachother
    
    :param users_df: the data frame describing how many times each user was
    mentioned, retweeted, and replied.
    """
    fig = plt.figure()
    plot = fig.add_subplot(111)
    
    users = users_df.index[0:10]
    width = .25
    x = range(len(users)) #spacing 
    
    mentioned = list(users_df.mentioned)[0:10] #values  
    plot1 = plot.bar(x, mentioned, width, color="b")

    x = [num + width for num in x] #set location of next bar
    retweeted = list(users_df.retweeted)[0:10] #values  
    plot2 = plot.bar(x, retweeted, width, color="g")
    
    x = [num + width for num in x] #set location of next bar
    replied = list(users_df.replied)[0:10] #values  
    plot3 = plot.bar(x, replied, width, color="r")

   
    plot.set_title("Total Tweets vs Users")
    plot.set_ylabel("Total Tweets")
    plot.set_xlabel("User")
    
    plot.set_xticks(x)
    plot.set_xlim(0, len(users))
    xticks = plot.set_xticklabels(users)
    plt.setp(xticks, rotation = 45, fontsize = 13)
    plot.legend( (plot1, plot2, plot3), ('Mentioned', 'Retweeted', 'Replied'), loc="best" )
    
    plt.show()
    fig.savefig("users-df.png")


def graph_dates(all_dates):
    """Plots the dates_dict of each tweet
    
    :param all_dates: the data frame describing tweets, retweets, and 
    replies per date.
    """
    fig = plt.figure()
    plot = fig.add_subplot(111)
    
    dates = all_dates.day
    width = .2
    x = range(len(dates)) #spacing 
    
    tweet = list(all_dates.tweet) #values  
    plot1 = plot.bar(x, tweet, width, color="b")

    x = [num + width for num in x] #set location of next bar
    retweet = list(all_dates.retweet) #values  
    plot2 = plot.bar(x, retweet, width, color="g")
    
    x = [num + width for num in x] #set location of next bar
    reply = list(all_dates.reply) #values  
    plot3 = plot.bar(x, reply, width, color="r")

   
    plot.set_title("Total Tweets vs Days")
    plot.set_ylabel("Total Tweets")
    plot.set_xlabel("Day")
    
    plot.set_xticks(x)
    plot.set_xlim(0, len(dates))
    xticks = plot.set_xticklabels(dates)
    plt.setp(xticks, rotation = -45, fontsize = 13)
    plot.legend( (plot1, plot2, plot3), ('Tweets', 'Retweets', 'Replies'), loc="best" )
    
    plt.show()
    fig.savefig("dates.png")

def graph_hashtags(hashtags, limit = 10):
    """Prints graph for most popular hashtags
    
    Prints a bar graph for the indicated number of 
    hashtags, from least to greatest.
    :param hashtags: the series describing the hashtags and numbers of occurrences.
    :param limit: the number of hashtags to print
    """
    fig = plt.figure()
    plot = fig.add_subplot(111)
    
    pop_tags = list(reversed([tag for tag,count in hashtags.iteritems()][1:limit+1]))

    x = range(limit) #spacing 
    y = list(reversed([count for tag,count in hashtags.iteritems()][1:limit+1])) #values
    width = 0.5
    
    plot.bar(x, y, width, color="g")
    plot.set_title("Number of Hashtags vs Hashtag")
    plot.set_ylabel("Number of Hashtags")
    plot.set_xlabel("Hashtag")
    plot.set_xticks(x)
    
    plot.set_ylim(0, y[-1]*1.25)
    plot.set_xlim(0, limit) 
    xticks = plot.set_xticklabels(pop_tags)
    plt.setp(xticks, rotation=45, fontsize=13)
    
    plt.show()
    fig.savefig("pop-hashtags.png")

def graph_applications(clients, limit = 10):
    """Prints graph for most popular clients
    
    Prints a bar graph for the indicated number of 
    clients, from least to greatest.
    :param clients: the series describing the clients and numbers of occurrences.
    :param limit: the number of clients to print
    """
    fig = plt.figure()
    plot = fig.add_subplot(111)
    
    pop_clients = list(reversed([tag for tag,count in clients.iteritems()][0:limit]))

    x = range(limit) #spacing 
    y = list(reversed([count for tag,count in clients.iteritems()][0:limit])) #values
    width = 0.5
    
    plot.bar(x, y, width, color="b")
    plot.set_title("Number of uses of Clients vs Client")
    plot.set_ylabel("Number of uses of Clients")
    plot.set_xlabel("Client")
    plot.set_xticks(x)
    
    plot.set_ylim(0, y[-1]*1.25)
    plot.set_xlim(0, limit) 
    xticks = plot.set_xticklabels(pop_clients)
    plt.setp(xticks, rotation=45, fontsize=13)
    
    plt.show()
    fig.savefig("pop-apps.png")

def hashtag_wordcloud(hashtags):
    """Creates a wordcloud of hashtags, based on occurrences

    The wordcloud is created using the hashtags series, which
    is converted to a list of tuples, so that it can work with
    the wordcloud module. The size of each hashtag is dependent 
    upon the number of occurrences, and they scale accordingly
    :param hashtags: the hashtags series mapping hashtags to total occurrences
    """
    list_hashtags = hashtags.to_dict().items()
    wordcloud = WordCloud(background_color = 'black', width = 1200, height = 1000).fit_words(list_hashtags)

    plt.figure()
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
