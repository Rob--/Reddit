# TermMatch, Reddit bot
#
# Finds certain terms within subreddits (documents them if needed) and fires an action.

# NOTE: this is the advanced TermMatch. Use this version to document all data.
# This will let you track how many comments have been searched, how many comments contain
# the words you want to search for and how many comments contains the word from each subreddit searched.
# It will save all the data in a database and you need to use filter.py to make this data readable (it outputs as a .txt)
##

import praw
from requests.exceptions import HTTPError, ConnectionError, Timeout
from praw.errors import APIException, RateLimitExceeded, InvalidCaptcha
from socket import timeout
from time import sleep
import sqlite3

#
# Reddit Options
# -

USERNAME = ""
# Your Reddit's bot username.

PASSWORD = ""
# Your Reddit's bot password.

USERAGENT = str("TermMatch, /u/" + USERNAME)
# The bot's user agent. Change this according to your username.

SUBREDDITS = ["all"]
# Subreddits to search.

WORDS = ["the"]
# Words to search for.

SEND_REPLY = False
# If "True", when a match is found the bot will reply with the REPLY_STRING.

REPLY_STRING = "You're welcome."
# If REPLY is "True", this is what will be commented.
# See the README.md file for formatting information.

SEND_PM = False
# If "True", when the bot is unable to comment (due to the RateLimit being exceeded) it will send a PM with the REPLY_STRING.

PM_SUBJECT = "PM's subject."
# The PM's subject.

SLEEP = 1
# How long (in seconds) to sleep between comment searching.
# If you're continually searching subreddits I recommend sleeping to save bandwidth.
# If you're searching smaller subreddits (/r/Android): sleep for 5-10 minutes.
# If you're searching medium subreddits (/r/Skyrim): sleep for 1-5 minutes.
# If you're searching big subreddits (/r/AskReddit): sleep for a 1-30 seconds.

# -
# Reddit Options End
#

#
# SQLite
# -

con = sqlite3.connect("comment_data")
c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS comments (id TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS subreddits (subreddit TEXT, total INT, words INT)")

def exists(id):
    c.execute("SELECT 1 FROM comments WHERE id = \"%s\"" % id)
    if c.fetchone() is None: return False
    else: return True

def insertComment(id):
    c.execute("INSERT INTO comments (id) VALUES (\"%s\")" % id)
    con.commit()
                            
def commentCount():
    c.execute("SELECT * FROM comments")
    con.commit()
    return int((len(c.fetchall())))

def incSRS(subreddit, cWord):
    if subredditExists(subreddit):
        c.execute("UPDATE subreddits SET total = total + 1 WHERE subreddit = \"%s\"" % subreddit)
        if cWord: c.execute("UPDATE subreddits SET words = words + 1 WHERE subreddit = \"%s\"" % subreddit)
    else:
        c.execute("INSERT INTO subreddits VALUES (\"%s\", 0, 0)" % subreddit)
        incSRS(subreddit, cWord)
    con.commit()
       
def subredditExists(subreddit):
    c.execute("SELECT 1 FROM subreddits WHERE subreddit = \"%s\"" % subreddit)
    con.commit()
    if c.fetchone() is None: return False
    else: return True    
    
# -
# SQLite End
#

# 
# Reddit Login
# -

reddit = praw.Reddit(USERAGENT)
try:
    reddit.login(USERNAME, PASSWORD)
    print("Logged in with '%s'." % USERNAME)
except praw.errors.InvalidUserPass:
    print("Invalid username or password. Exiting, press enter.")
    input("")
    raise SystemExit

# -
# Reddit Login End
#

#
# Reddit Search
# -

def work(comment):
    try:
        if SEND_REPLY: comment.reply(REPLY_STRING)
        if SEND_PM: reddit.send_message(comment.author, PM_SUBJECT, REPLY_STRING, raise_captcha_exception=True)
        incSRS(comment.subreddit, True)
        insertComment(comment.id)
    except RateLimitExceeded as e:
        try:
            if SEND_PM: reddit.send_message(comment.author, PM_SUBJECT, REPLY_STRING, raise_captcha_exception=True)
        except InvalidCaptcha: sleep(e.sleep_time)
        except (HTTPError, ConnectionError, Timeout, timeout) as e: print(e)
        except APIException as e: print(e)

while True:
    for subreddit in SUBREDDITS:
        for comment in praw.helpers.comment_stream(reddit, subreddit, limit=1000, verbosity=0):
            incSRS(comment.subreddit, False)
            if not exists(comment.id) and str(reddit.user) != str(comment.author):
                if any(word.lower() in comment.body.lower() for word in WORDS) and not exists(comment.id): work(comment)
sleep(SLEEP)
    
# -
# Reddit Search End
#
