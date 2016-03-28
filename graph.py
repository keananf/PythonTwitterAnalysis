import matplotlib.pyplot as plt, datetime
from tweets import hashtags
from collections import defaultdict

dates_dict = defaultdict(lambda: 0)

def get_dates(all_dates):
    """Retrieves a sorted list of dates based on num of tweets

    Ascertains the total number of tweets posted in a day.
    Sorts this dictionary, and returns the most popular dates
    :param all_dates: the all_dates Series representing all the dates
    :return Sorted list of dates
    """
    for date in sorted([datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").date() for value in all_dates]):
        dates_dict[date] += 1
        
    dates_dict2 = dates_dict.copy()
    return reversed(sorted(dates_dict2.__iter__(), key=dates_dict2.pop, reverse=True))

def print_dates(all_dates):
    """Plots the dates_dict of each tweet
    
    :param all_dates: the all_dates Series representing all the dates
    in the collection
    """
    fig = plt.figure()
    plot = fig.add_subplot(111)
    
    dates = [date for date in get_dates(all_dates)]

    x = range(len(dates)) #spacing 
    y = [dates_dict[date] for date in dates] #values  
    width = .5
    
    plot.bar(x, y, width, color="b", align = "center")
    plot.set_title("Total Tweets vs Days")
    plot.set_ylabel("Total Tweets")
    plot.set_xlabel("Day")
    
    plot.set_xticks(x)
    plot.set_xlim(0, len(dates))
    xticks = plot.set_xticklabels(dates)
    plt.setp(xticks, rotation = 45, fontsize = 13)
    
    plt.show()

def print_hashtags(limit = 10):
    """Prints graph for most popular hashtags
    
    Prints a bar graph for the indicated number of 
    hashtags, from least to greatest.
    :param limit: the number of hashtags to print
    """
    fig = plt.figure()
    plot = fig.add_subplot(111)
    
    pop_tags = [tag for tag in reversed(sorted(hashtags.__iter__(),key=hashtags.get, reverse=True)[0:limit])]

    x = range(limit) #spacing 
    y = [hashtags[tag] for tag in pop_tags] #values
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

def graph(df):
    print_dates(df["time"].values)
    print_hashtags()

