import matplotlib.pyplot as plt, datetime
from collections import defaultdict

dates_dict = defaultdict(lambda: 0)

def refine_dates(all_dates):
    """Retrieves a sorted list of df based on num of tweets

    Ascertains the total number of tweets posted in a day.
    Sorts this dictionary, and returns the most popular df
    :param all_dates: the all_dates Series representing all the df
    :return list of df
    """ 
    return list(reversed([datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S").date() 
                          for date,value in all_dates.iteritems()]))

def print_dates(all_dates):
    """Plots the dates_dict of each tweet
    
    :param all_dates: the all_dates Series representing all the dates
    in the collection
    """
    fig = plt.figure()
    plot = fig.add_subplot(111)
    
    dates = all_dates.index
    width = .35
    x = range(len(dates)) #spacing 
    
    tweet = list(all_dates.tweet) #values  
    plot1 = plot.bar(x, tweet, width, color="b", align = "center")#, 
                     #bottom=[i+j for i, j in zip(all_dates['reply'],all_dates['retweet'])])

    retweet = list(all_dates.retweet) #values  
    plot2 = plot.bar(x, retweet, width, color="g", align = "center")#, bottom=all_dates['reply'])
    
    reply = list(all_dates.reply) #values  
    plot3 = plot.bar(x, reply, width, color="r", align = "center")

   
    plot.set_title("Total Tweets vs Days")
    plot.set_ylabel("Total Tweets")
    plot.set_xlabel("Day")
    
    plot.set_xticks(x)
    plot.set_xlim(0, len(dates))
    xticks = plot.set_xticklabels(dates)
    plt.setp(xticks, rotation = 45, fontsize = 13)
    plot.legend( (plot1, plot2, plot3), ('Tweets', 'Retweets', 'Replies') )
    
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
    
    pop_tags = list(reversed([tag for tag,count in hashtags.iteritems()][0:10]))

    x = range(limit) #spacing 
    y = list(reversed([count for tag,count in hashtags.iteritems()][0:10])) #values
    width = 0.5
    
    plot.bar(x, y, width, color="g", align="center")
    plot.set_title("Number of Hashtags vs Hashtag")
    plot.set_ylabel("Number of Hashtags")
    plot.set_xlabel("Hashtag")
    plot.set_xticks(x)
    
    plot.set_ylim(0, y[-1]*1.25)
    plot.set_xlim(0, limit) 
    xticks = plot.set_xticklabels(pop_tags)
    plt.setp(xticks, rotation=45, fontsize=13)
    
    plt.show()

def graph(hashtag_df, dates_df):
    print_dates(dates_df)
    print_hashtags(hashtag_df)
