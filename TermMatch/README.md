TermMatch
================

### > Description
A simple Reddit bot developed with PRAW.
The bot connects to a SQLite DB and simply searches a stream of comments from the give subreddits and finds matches of the words given.

### > What does it do?
The bot searches for words under the `WORDS` array from subreddits under the `SUBREDDITS` array.
Every time it searches a comment and finds a match it will add the comment to a database, it also sends a reply comment or PM (if enabled) with the message set in the `REPLY_MESSAGE` variable.  

### > Usage
You can format your message to fit Reddit's markdown. e.g:  
If the REPLY_STRING is:  
`"*This* is italic, **this** is bold. [Here's a link.](http://google.com) and here's quote:\n> Quote."`  
The comment/PM will look like:  
"*This* is italic, **this** is bold. [Here's a link.](http://google.com)
> Quote"  
