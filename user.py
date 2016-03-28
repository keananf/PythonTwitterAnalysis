import re, operator
from functools import reduce

users = {}

class User(object):
    """Class describing an individual Twitter User
    """
    name = ""
    num_of_tweets = 0
    num_of_retweets = 0
    num_of_replies = 0

    def __init__(self, name):
        """Constructor for a User object
        
        :param name: the name of the user
        """
        self.name = name;
        
    def add(self, row):
        """Adds a tweet to the user's list of tweets
        
        :param row: the row representing the tweet
        """
        self.analyse_text(row["text"])
        self.num_of_tweets += 1
        
    def analyse_text(self, text):
        """Function for ascertaining the type of tweet
      
        This function looks at the first element in the 
        text of the tweet and looks for "@username." Following, it
        checks the words in the text of the Tweet object for "RT" 
        and then sets the corresponding fields in the object. 
        :param text: the text of the tweet
        """
        pattern = re.compile("@.")

        words = text.split(" ")
        if pattern.match(words[0]):
            self.num_of_replies += 1
            
        if reduce(operator.__or__, map(lambda word: word == "RT", words)): 
            self.num_of_retweets += 1
