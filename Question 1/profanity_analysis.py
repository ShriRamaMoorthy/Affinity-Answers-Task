#A Simple Python program that can indicate the degree of profanity for each sentence in a file full of Twitter tweets.

import re

# set of racial slurs
racial_slurs = {"bastard","fuck", "idiot", "shit", "stupid", "psycho","retard","moron"}

# function to calculate the degree of profanity
def calculate_profanity(sentence):
    count = 0
    words = re.findall(r'\w+', sentence.lower())
    for word in words:
        if word in racial_slurs:
            count += 1
    return count / len(words)

# read the file containing tweets
with open('tweets.txt', 'r', encoding='utf-8') as file:
    tweets = file.readlines()

# process each tweet and calculate the degree of profanity
for tweet in tweets:
    profanity = calculate_profanity(tweet)
    print("Tweet: " + tweet.strip())
    print("Degree of profanity: " + str(profanity))
    print()
