''' A script to dl fanfiction from ffnet'''
import requests as re
import sys
from lxml import html

# Basics
#
# Url example:
# https://www.fanfiction.net/s/5782108/1/Harry-Potter-and-the-Methods-of-Rationality 
#           domain       /story/story-id/chap-id/fic-name
#
#   All I need is story id.
#
# Step 1:  Get total number of chapters for a fic.
#

if len(sys.argv) < 3:
    sys.stderr.write("Usage: ficdl.py <url> <type>")
    exit(0)
else:
    storyUrl = sys.argv[1]

# Find the story id
storyId = storyUrl[storyUrl.find('/s/')+3:storyUrl.find('/s/')+10]

# Get number of chapters
chapCount = 0
notFoundText = 'Chapter not found. Please check to see you are not using an outdated url.' 

#req = html.fromstring((re.get('https://www.fanfiction.net/s/' + storyId + '/' + str(chapCount) + '/')).text).xpath('/html/body/div/span/text()[2]')[0]
#print req
while (html.fromstring((re.get('https://www.fanfiction.net/s/%s/%s/' % (storyId,str(chapCount)))).text).xpath('/html/body/div/span/text()[2]')) != notFoundText.split('%'):
    #chap = re.get()
    print "Chapter " + str(chapCount + 1) + " found."
    chap = re.get('https://www.fanfiction.net/s/%s/%s/' % (storyId,str(chapCount)))
    print "Retreived chapter."
    chapCount += 1

print chapCount
