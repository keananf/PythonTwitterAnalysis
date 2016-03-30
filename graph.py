import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from collections import defaultdict

dates_dict = defaultdict(lambda: 0)

def graph_distrib(hashtags_distrib):
    """Plots a 3D graph of hashtags and their occurrences on each day
    
    :param hashtags_distrib: The dataframe representing the number of 
    each hashtag per day. 
    """
    fig = plt.figure()
    plot = fig.add_subplot(111, projection = '3d')
    
    hashtags = [tag for tag in hashtags_distrib.index][0:4]
    plots = []
    ylabels =[]
    
    column = 1
    for colour, tag in zip(['r', 'g', 'b', 'y'], hashtags):
        row = pd.DataFrame(hashtags_distrib.loc[tag])
        xs = row.index 
        ys = row[tag] #amount of this hashtag on this day
    
        current_plot = plot.bar(xs, ys, zs = column, zdir='y', color = colour, alpha=0.8)
        #plots.append(current_plot)
        ylabels.append(tag)
        ylabels.append("")
        column += 1
    
        
    plot.set_title("Hashtags vs Occurrences vs Day")
    plot.set_ylabel("Hashtag")
    plot.set_xlabel("Day")
    plot.set_zlabel("Occurrences")
    
    plot.set_xticks(range(0,len(hashtags_distrib.columns)))
    plot.set_xticklabels(range(0,len(hashtags_distrib.index)))
    plot.set_yticklabels(ylabels)
    
    #plot.legend( plots, labels, loc="best" )
    
    plt.show()


def graph_dates(all_dates):
    """Plots the dates_dict of each tweet
    
    :param all_dates: the data frame describing tweets, retweets, and 
    replies per date.
    """
    fig = plt.figure()
    plot = fig.add_subplot(111)
    
    dates = all_dates.index
    width = .35
    x = range(len(dates)) #spacing 
    
    tweet = list(all_dates.tweet) #values  
    plot1 = plot.bar(x, tweet, width, color="b")

    retweet = list(all_dates.retweet) #values  
    plot2 = plot.bar(x, retweet, width, color="g")
    
    reply = list(all_dates.reply) #values  
    plot3 = plot.bar(x, reply, width, color="r")

   
    plot.set_title("Total Tweets vs Days")
    plot.set_ylabel("Total Tweets")
    plot.set_xlabel("Day")
    
    plot.set_xticks(x)
    plot.set_xlim(0, len(dates))
    xticks = plot.set_xticklabels(dates)
    plt.setp(xticks, rotation = 45, fontsize = 13)
    plot.legend( (plot1, plot2, plot3), ('Tweets', 'Retweets', 'Replies'), loc="best" )
    
    plt.show()

def graph_hashtags(hashtags, limit = 10):
    """Prints graph for most popular hashtags
    
    Prints a bar graph for the indicated number of 
    hashtags, from least to greatest.
    :param hashtags: the series describing the hashtags and numbers of occurrences.
    :param limit: the number of hashtags to print
    """
    fig = plt.figure()
    plot = fig.add_subplot(111)
    
    pop_tags = list(reversed([tag for tag,count in hashtags.iteritems()][0:limit]))

    x = range(limit) #spacing 
    y = list(reversed([count for tag,count in hashtags.iteritems()][0:limit])) #values
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

def graph_clients(clients, limit = 10):
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
