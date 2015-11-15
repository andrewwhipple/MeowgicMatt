# Meowgic Matt RSS module

import sys
import os
import json

#Debug function to call out that the module successfully loaded.
def meow():
    print "mrss loaded"

#Copies the current version of the RSS feed living in the RSS/podcastname subfolder to provided git folder, and pushes to git. 
def pushToGit(baseFolderFilePath, rssFilePath):
    print "\nAvailable podcasts: "
    with open ("dataStore.json") as castList:
        castListData = json.load(castList)
        podcasts = castListData["podcasts"]
        for cast in podcasts:
            print "- " + cast
    podcastName = raw_input("Enter one of the available podcasts: ")
    
    os.system("cp ../RSS/" + podcastName + "/" + podcastName + ".xml " + baseFolderFilePath + rssFilePath)
    print "\nFile Moved!\n"
    
    os.system("git -C " + baseFolderFilePath + " add " + baseFolderFilePath + rssFilePath + podcastName + ".xml")
    os.system("git -C " + baseFolderFilePath + " commit -m 'Update RSS'")
    os.system("git -C " + baseFolderFilePath + " pull")
    os.system("git -C " + baseFolderFilePath + " push origin master")
    print "\nFile (hopefully, unless there was a git error) pushed!\n"

#Adds an episode to an existing RSS feed.
def addEpisode():

    print "\nAvailable podcasts: "
    with open ("dataStore.json") as castList:
        castListData = json.load(castList)
        podcasts = castListData["podcasts"]
        for cast in podcasts:
            print "- " + cast
    podcastFolder = raw_input("Enter one of the available podcasts: ")
    
    #ONLY WORKS IF EVERYTHING IS PROPERLY FORMATTED
    feedFileName = podcastFolder  

    dataFileName = raw_input("Enter JSON filename for episode data (blank if entering info manually by command line): ")
    
    epTitle = ""
    epAuthor = ""
    epSubtitle = ""
    epDescription = ""
    epImage = ""
    epURL = ""
    epPubDate = ""
    epDuration = ""
    epLength = ""

    if dataFileName == "":
        epTitle = raw_input("Ep title: ")
        epAuthor = raw_input("Ep author: ")
        epSubtitle = raw_input("Ep subtitle: ")
        epDescription = raw_input("Ep description: ")
        epImage = raw_input("Ep image link: ")
        epURL = raw_input("Ep mp3 url: ")
        epPubDate = raw_input("Ep pub date (as Wed, 15 Jun 2015 19:00:00 PST): ")
        epDuration = raw_input("Ep duration (as 7:04): ")
        epLength = raw_input("Ep duration (in bytes): ")
    else:
        with open("../Data/" + podcastFolder + "/" + dataFileName + '.json') as dataFile:
            data = json.load(dataFile)
            epTitle = data["epTitle"]
            epAuthor = data["epAuthor"]
            epSubtitle = data["epSubtitle"]
            epDescription = data["epDescription"]
            epImage = data["epImage"]
            epURL = data["epURL"]
            epPubDate = data["epPubDate"]
            epDuration = data["epDuration"]
            epLength = data["epLength"]
        
            dataFile.close()
        
    epString = '<item><title>' + epTitle + '</title><itunes:author>' + epAuthor + '</itunes:author><itunes:subtitle>' + epSubtitle + '</itunes:subtitle><itunes:summary><![CDATA[' + epDescription + '!]]></itunes:summary><itunes:image href="' + epImage + '" /><enclosure url="' + epURL + '" length="' + epLength + '" type="audio/mpeg" /><guid>' + epURL + '</guid><pubDate>' + epPubDate + '</pubDate><itunes:duration>' + epDuration + '</itunes:duration></item>'

    with open("../RSS/" + podcastFolder + "/" + feedFileName + ".xml", "r") as feedReadFile:
        feedTotalString = feedReadFile.read()
    
        recentIndex = feedTotalString.find('<!--MOST RECENT-->')
        startOfFeed = feedTotalString[0:recentIndex + 18]
        endOfFeed = feedTotalString[recentIndex + 18:]
        feedString = startOfFeed + epString + endOfFeed
        feedReadFile.close()
        with open("../RSS/" + podcastFolder + "/" + feedFileName + '.xml', "w") as feedWriteFile:
    
            feedWriteFile.write(feedString) 
            feedWriteFile.close()   
            print "\nEpisode added!\n"

#Creates a new RSS feed.
def createFeed():
    
    podcastFolder = raw_input("Podcast folder: ")
    
    #OPERATES ON THE OPINIONATED ASSUMPTION THAT FEEDNAME is IDENTICAL TO PODCAST FOLDER NAME
    feedName = podcastFolder
    podTitle = ""
    podLink = ""
    copyrightYearAndName = ""
    podSubtitle = ""
    podSummary = ""
    podAuthor = ""
    podOwnerName = ""
    podOwnerEmail = ""
    podImage = ""
    podCategory = ""
    podSubCategory = ""
    podSubCategory2 = ""
    podKeywoards = ""
    explicit = ""

    dataFileName = raw_input("Enter JSON filename with podcast info (leave blank if entering manually by command line): ")


    if dataFileName == "":
        podTitle = raw_input("Podcast title: ")
        podLink = raw_input("Podcast link: ")
        copyrightYearAndName = raw_input("Copyright year and name: ")
        podSubtitle = raw_input("Podcast subtitle: ")
        podSummary = raw_input("Podcast description: ")
        podAuthor = raw_input("Podcast author: ")
        podOwnerName = raw_input("Podcast owner: ")
        podOwnerEmail = raw_input("Podcast owner email: ")
        podImage = raw_input("Podcast image link: ")
        podCategory = raw_input("Podcast category 1: ")
        podSubCategory = raw_input("Podcast subcategory: ")
        podSubCategory2 = raw_input("Podcast subcategory 2: ")
        podKeywords = raw_input("Podcast keywords (separated by comma and spaces): ")
        explicit = raw_input("Explicit? (yes or no): ")

    else:
        with open("../Data/"+ podcastFolder + '/' + dataFileName + '.json') as dataFile:
            data = json.load(dataFile)
        
            podTitle = data["podTitle"]
            podLink = data["podLink"]
            copyrightYearAndName = data["copyrightYearAndName"] 
            podSubtitle = data["podSubtitle"]
            podSummary = data["podSummary"]
            podAuthor = data["podAuthor"]
            podOwnerName = data["podOwnerName"]                
            podOwnerEmail = data["podOwnerEmail"]
            podImage = data["podImage"]
            podCategory = data["podCategory"]
            podSubCategory = data["podSubCategory"]
            podSubCategory2 = data["podSubCategory2"]
            podKeywords = data["podKeywords"]
            explicit = data["explicit"]
    
    feedName = feedName + '.xml'
    with open("../RSS/" + podcastFolder + "/" + feedName, "w") as feedFile:
        feedString = '<?xml version="1.0" encoding="UTF-8"?><rss xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:atom="http://www.w3.org/2005/Atom" version="2.0"><channel><atom:link href="'+ podLink +'" rel="self" type="application/rss+xml" /><title>' + podTitle + '</title><link>' + podLink + '</link><language>en-us</language><copyright>&#x2117; &amp; &#xA9; ' + copyrightYearAndName + '</copyright><itunes:subtitle>' + podSubtitle + '</itunes:subtitle><itunes:author>' + podAuthor + '</itunes:author><itunes:summary>' + podSummary + '</itunes:summary><description>' + podSummary + '</description><itunes:owner><itunes:name>' + podOwnerName + '</itunes:name><itunes:email>' + podOwnerEmail + '</itunes:email></itunes:owner><itunes:image href="' + podImage + '" /><itunes:category text="' + podCategory + '"><itunes:category text="' + podSubCategory + '"/></itunes:category><itunes:category text="' + podSubCategory2 + '"/><itunes:keywords>' + podKeywords + '</itunes:keywords><itunes:explicit>' + explicit + '</itunes:explicit><!--MOST RECENT--></channel></rss>'
        feedFile.write(feedString)
        feedFile.close()
        print "\nFeed created!\n"
    
        
    