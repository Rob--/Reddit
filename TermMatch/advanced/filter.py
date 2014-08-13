import sqlite3

con = sqlite3.connect("comment_data")

c1 = con.cursor()
c1 = con.execute("SELECT * FROM subreddits ORDER BY total DESC")
maxT = 0
maxLength1 = 0
while True:
    row = c1.fetchone()
    if row is None:
        break
    else:
        maxT += 1
        if len(row[0]) > maxLength1:
            maxLength1 = len(row[0])
            
maxLength1 += (len(str(maxT)) + 1)
c1 = con.execute("SELECT * FROM subreddits ORDER BY words DESC")
maxLength2 = 0
while True:
    row = c1.fetchone()
    if row is None:
        break
    else:
        if len(str(row[1])) > maxLength2:
            maxLength2 = len(str(row[1]))
        
c1 = con.execute("SELECT * FROM subreddits ORDER BY words DESC")
maxLength3 = 0
while True:
    row = c1.fetchone()
    if row is None:
        break
    else:
        if len(str(row[2])) > maxLength3:
            maxLength3 = len(str(row[2]))
        
c1 = con.execute("SELECT * FROM subreddits ORDER BY words DESC")
maxLength4 = 0
while True:
    row = c1.fetchone()
    if row is None:
        break
    else:
        a = (row[2] / row[1]) * 1000
        b = str(a).split(".")[0]
        if len(b) > maxLength4:
            maxLength4 = len(b)

# this will ultimately decide upon the output
# currently this will order all subreddits by the number of
# comments searched through it in descending order (high -> low)
# "SELECT * FROM subreddits ORDER BY words DESC" to order by number of matches
c1 = con.execute("SELECT * FROM subreddits ORDER BY total DESC")
x = "Subreddit: "
y = "Total: "
z = "Words: "
q = "Words p/ thousand: "
while len(x) < maxLength1 + 1:
    x = " " + x
while len(y) < maxLength2:
    y = " " + y
while len(z) < maxLength3:
    z = " " + y

file = open("stats.txt", "w")
f = ("%s |  %s|  %s|  %s|\n" % (x, y, z, q))
file.write(f)
s = "-"
while len(s) < len(f) - 1:
    s += "-"
file.write("%s\n" % s)
c_ = 0
while True:
    row = c1.fetchone()
    if row is None:
        break
    else:
        c_ += 1
        a = row[0]
        b = str(row[1])
        c = str(row[2])
        while len(a) < maxLength1 - (len(str(maxT)) + 1):
            a = " " + a
        z_ = 0
        while not z_ == (len(str(maxT)) - len(str(c_))):
            z_ += 1
            a = " " + a
        a = str(c_) + ")" + a
        while len(b) < (maxLength2 + len(y) - len(b) + 2) - 1:
            b = " " + b
        b += " "
        while len(c) < (maxLength3 + len(z) - 2) - 1:
            c = " " + c
        c += " "
        d = (row[2] / row[1]) * 1000
        e = str(d)
        f = e.split(".")
        g = f[0]
        h = f[1]
        h = h[:2]
        while len(h) != 2:
            h += "0"
        while len(g) < maxLength4:
            g = " " + g
        i = g + "." + h
        while len(i) < (maxLength4 + len(q) - 3) - 1:
            i = " " + i
        i += " "
        file.write("%s  |  %s|  %s|  %s|\n" % (a, b, c, i))
file.close()
