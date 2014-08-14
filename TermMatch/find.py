# TermMatch, Reddit bot by /u/AndroidL
#
# Finds certain terms within subreddits (documents them if needed) and fires an action.

import praw
from requests.exceptions import HTTPError, ConnectionError, Timeout
from praw.errors import APIException, RateLimitExceeded, InvalidCaptcha
from socket import timeout
from time import sleep
import sqlite3

# > Options

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
# If you're searching smaller subreddits (/r/Android): sleep for 300-600 seconds (5-10 minutes).
# If you're searching medium subreddits (/r/Skyrim): sleep for 60-300 seconds (1-5 minutes).
# If you're searching big subreddits (/r/AskReddit): sleep for a 1-30 seconds.

# > Login

reddit = praw.Reddit(USERAGENT)
try: reddit.login(USERNAME, PASSWORD)
except praw.errors.InvalidUserPass: raise SystemExit

# > SQLite

con = sqlite3.connect("comment_data")
c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS comments (id TEXT)")

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

# > Search

def work(comment):
    try:
        if SEND_REPLY: comment.reply(REPLY_STRING)
        if SEND_PM: reddit.send_message(comment.author, PM_SUBJECT, REPLY_STRING, raise_captcha_exception=True)
        insertComment(comment.id)
        print("Added '%s' to database." % comment.id)
    except RateLimitExceeded as e:
        try:
            if SEND_PM: reddit.send_message(comment.author, PM_SUBJECT, REPLY_STRING, raise_captcha_exception=True)
        except InvalidCaptcha: sleep(e.sleep_time)
        except (HTTPError, ConnectionError, Timeout, timeout) as e: print(e)
        except APIException as e: print(e)

while True:
    for subreddit in SUBREDDITS:
        for comment in praw.helpers.comment_stream(reddit, subreddit, limit=1000, verbosity=0):
            if not exists(comment.id) and str(reddit.user) != str(comment.author):
                if any(word.lower() in comment.body.lower() for word in WORDS) and not exists(comment.id): work(comment)
    sleep(SLEEP)
