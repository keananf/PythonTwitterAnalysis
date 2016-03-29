import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from collections import defaultdict

dates_dict = defaultdict(lambda: 0)

def print_distrib(hashtags_distrib):
    """Plots the dates_dict of each tweet
    
    :param hashtags_distrib: 
    """
    fig = plt.figure()
    plot = fig.add_subplot(111, projection = '3d')
    
    hashtags = [tag for tag in hashtags_distrib.index][0:4]
    labels = []
    column = 1
    tag_num = 1
    for colour, tag in zip(['r', 'g', 'b', 'y'], hashtags):
        row = pd.DataFrame(hashtags_distrib.loc[tag])
        xs = row.index 
        ys = row[tag] #amount of this hashtag on this day
    
        current_plot = plot.bar(xs, ys, zs = tag_num, zdir='y', color = colour, alpha=0.8)
        labels.append(current_plot)
        column += 1
        tag_num += 1
    
        
    plot.set_title("Hashtags vs Occurrences vs Day")
    plot.set_ylabel("Hashtag")
    plot.set_xlabel("Day")
    plot.set_zlabel("Occurrences")
    
    #plot.set_xticks(x)
    #plot.set_xlim(0, len(dates))
    #xticks = plot.set_xticklabels(dates)
    #plt.setp(xticks, rotation = 45, fontsize = 13)
    #plot.legend( (plot1, plot2, plot3), ('Tweets', 'Retweets', 'Replies'), loc="best" )
    
    plt.show()


def print_dates(all_dates):
    """Plots the dates_dict of each tweet
    
    :param all_dates: the all_dates df representing all the dates
    in the collection
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

def print_hashtags(hashtags, limit = 10):
    """Prints graph for most popular hashtags
    
    Prints a bar graph for the indicated number of 
    hashtags, from least to greatest.
    :param hashtags 
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

def graph(dates_df,hashtag_series, hashtag_distrib):
    """Top level function for creating graphs
    
    :param hashtag_series: the series describing the hashtags and numbers of occurrences. 
    :param dates_df: the data frame describing tweets, retweets, and 
    replies per date.
    :param hashtag_distrib: the dataframe detailing hashtags and their occurrences
    on EACH day
    """
    print_dates(dates_df)
    print_hashtags(hashtag_series)
    print_distrib(hashtag_distrib)
