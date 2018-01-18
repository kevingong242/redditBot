#Reddit bot that will look through a subreddit (nba)
#return the titles of each thread that includes a specific keyword

from bs4 import BeautifulSoup

import praw
import time
import re
import requests
import bs4
import json

def authenticate():
#Function is meant to login reddit and let the user know that the bot is running    
    print('Authenticating...\n')
    reddit = praw.Reddit('threadbot', user_agent = "Kevin's thread finder")
    print('Authenticated as {}\n'.format(reddit.user.me()))
    return reddit

def run_threadbot(reddit, threads_found,data):
    print("Getting 50 comments...\n")
    #LOOPS THROUGH THREAD TITLES
    for submission in reddit.subreddit('nba').hot(limit = 50):
        if "Booker" in submission.title and submission not in threads_found:
            threads_found.append(submission)
            data.append({
                'title': submission.title,
                'url': submission.shortlink
            })
            with open("threads_found.txt", "a") as f:
                f.write(submission.title + "\n")
            
            with open("threads_found.json", "w") as outfile:
                json.dump(data,outfile)
                
    
    print('Waiting 10 seconds...\n')
    time.sleep(10)
    
def get_saved_threads():
    with open("threads_found.txt", "r") as f:
        threads_found = f.read()
        threads_found = threads_found.split("\n")
    return threads_found
    
    
def thread_data():
    data = []
    return data
    
def main():
    reddit = authenticate()
    threads_found = get_saved_threads()
    data = thread_data()
    while True:
        run_threadbot(reddit, threads_found, data)


if __name__ == '__main__':
    main()