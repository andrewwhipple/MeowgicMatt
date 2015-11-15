#Meowgic Matt mp3 conversion module

import sys
import os
import json

#Debug function to call out that the module successfully loaded.
def meow():
    print "mconvert loaded"
    
    
#Get podcast name and mp3 file name
def convert():
    print "\nAvailable podcasts: "
    with open ("dataStore.json") as castList:
        castListData = json.load(castList)
        podcasts = castListData["podcasts"]
        for cast in podcasts:
            print "- " + cast
    podcast = raw_input("\nEnter one of the available podcasts: ")  
    
    epNumber = raw_input("\nPodcast episode number? ")
    
    fileName = podcast.capitalize()
    fileName = fileName + "Ep" + epNumber + ".mp3"
    if fileName != "":
        os.system("lame -m m ../Edited/" + podcast + "/" + fileName + " ../Queue/" + podcast + "/" + fileName)
    print "\nFile successfully converted!\n"

