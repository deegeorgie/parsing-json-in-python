import json
import urllib

url = 'http://python-data.dr-chuck.net/comments_192696.json'
print ' '

print "Retrieving", url
uh = urllib.urlopen(url)
data = uh.read()
print ("Retrieved:", len(data), "characters")
print ' '
print data

#converts data into a python object
comments = json.loads(data)

#we single out the element comments which is of interest to us...
comment_data = comments['comments']
print 'Count:', len(comment_data)
print ' '
total = 0

for item in comment_data:
	num = int(item['count'])
	#print num
	total = total + int(item['count'])
print 'Sum:', total



