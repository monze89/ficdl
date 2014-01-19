''' A script to dl fanfiction from ffnet'''
import requests as re
import sys
from lxml import html
import subprocess

# Basics
#
# Url example:
# https://www.fanfiction.net/s/5782108/1/Harry-Potter-and-the-Methods-of-Rationality 
#           domain       /story/story-id/chap-id/fic-name
#
#   All I need is story id.
#
# Step 1:  Get total number of chapters for a fic.
# Step 2:  Get title and author name.
# Step 3:  Put all content in one html file.
# Step 4:  Use calibre to convert the file to required format
#

if len(sys.argv) < 2:
    sys.stderr.write("Usage: ficdl.py <url> <type>[default is mobi]")
    exit(0)
else:
    if len(sys.argv) == 3:
        fType = sys.argv[2]
        if fType in ['mobi','Mobi','MOBI']:
            filType = 'mobi'
        if fType in ['epub','Epub','EPUB']:
            filType = 'epub'
        if fType in ['pdf','Pdf','PDF']:
            filType = 'pdf'
    else:
        filType = 'mobi'
    storyUrl = sys.argv[1]


# Find the story id
storyId = storyUrl[storyUrl.find('/s/')+3:storyUrl.find('/s/')+10]

# Get number of chapters
chapCount = 1
author = ''
title = ''
finalStory = ''
notFoundText = 'Chapter not found. Please check to see you are not using an outdated url.' 
chap = re.get('https://www.fanfiction.net/s/%s/%s/' % (storyId,str(chapCount)))

# Loop till you get notfoundtext.
# Add all the relevant text to finalStory
while (html.fromstring(chap.text).xpath('/html/body/div/span/text()[2]')) != notFoundText.split('%'):
    
    # Get author and title
    if title == '':
        title = html.fromstring(chap.text).xpath('//*[@id="profile_top"]/b')[0].text
    if author == '':
        author = html.fromstring(chap.text).xpath('//*[@id="profile_top"]/a[1]')[0].text
    
    # Add chapter text to final story
    finalStory += "<h1>Chapter " + str(chapCount) + "</h1>"
    finalStory += html.tostring((html.fromstring(chap.text).xpath('//*[@id="storytext"]'))[0])

    print "Chapter " + str(chapCount ) + " found."
    print "Retreived chapter."

    chapCount += 1
    chap = re.get('https://www.fanfiction.net/s/%s/%s/' % (storyId,str(chapCount)))

print chapCount-1
print title
print author

# Open a html file, and put this in the file
filTitle = title.replace(' ','_')
htfil = open(filTitle + '.html','w+')
htfil.write(finalStory)
htfil.close()

# Convert the book using ebook-convert - (Does most of the job for now)
print "Converting the file......"
subprocess.call(['ebook-convert',filTitle + '.html',title + '-' + author + '.' + filType])
subprocess.call(['rm',filTitle + '.html'])
print "Saved file to " + title + '-' + author + '.' + filType

