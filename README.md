My Reddit bots.
================
+ TermMatch
  * Simple bot that searches for given words and either replies or sends a PM (or both) within given subreddits.

================

#Usage
+ You will **need** Python 3.4.1 to use this bot.
  * To directly install Python 3.4.1 for 32 bit click [here](https://www.python.org/ftp/python/3.4.1/python-3.4.1.msi).
  * To directly install Python 3.4.1 for 64 bit click [here](https://www.python.org/ftp/python/3.4.1/python-3.4.1.amd64.msi).

+ You will need PRAW to use this bot.
  * To install PRAW, go to [this GitHub page] and press "*Download ZIP*"
  * If you want to directly install PRAW, click [here](https://github.com/praw-dev/praw/archive/master.zip).
  * Copy the PRAW file to your Desktop and make sure it's extracted.
  
  1) Open CMD and go to your Python directory and then into Scripts. (e.g. `cd A:\Python\Scripts`).  
  2) Type into CMD `pip install C:\Users\Rob\Desktop\[folder name]`. (replace `[folder name` to the name of the .ZIP you downloaded. Also replace my directory to PRAW's directory).  
  3) This will install the PRAW library. If you ever need to uninstall PRAW just type into CMD `pip freeze`, look for PRAW or something similar and type `pip uninstall [name]` (replace name with the name that came up in the freeze command about PRAW.  

+ Once you've got both Python 3.4.1 and PRAW installed you can run the bot.
  * Download the bot's source code (e.g. find.py) to a text document and save the file as a `.py` (make sure the file is now a python file).
  * If there are multiple files, save all of them in the same location (preferably in a folder, e.g. `Desktop/NameOfBot`.

#License
```
The MIT License (MIT)

Copyright (c) 2014 Rob--

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
