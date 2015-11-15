#Meowgic Matt setup module

import sys
import os
import json

#Debug function to call out that the module successfully loaded.
def meow():
    print "msetup loaded"

#Adds a new podcast to Meowgic Matt.
def newPodcastSetup():
    cast = raw_input("Enter the name of a podcast folder: ")
    os.mkdir("../Edited/" + cast)
    os.mkdir("../Published/" + cast)
    os.mkdir("../Queue/" + cast)
    os.mkdir("../Raw/" + cast)
    os.mkdir("../RSS/" + cast)
    os.mkdir("../Data/" + cast)
    finalString = ""
    with open("dataStore.json", "r") as dataReadFile:
        dataString = dataReadFile.read()
        stringStart = dataString[0:-2]
        finalString = stringStart + ',"' + cast + '"]}'
        dataReadFile.close()
    with open("dataStore.json", "w") as dataWriteFile:
        dataWriteFile.write(finalString)
        dataWriteFile.close()
    print("New podcast '" + cast + "' created!")

#Does the overall setup for the file structure of Meowgic Matt.
def setup():
    podcasts = []
    while True:
        cast = raw_input("Enter the name of a podcast folder (or hit enter to end): ")
        if cast != "":
            podcasts.append(cast)
        else:
            break
    os.system("mkdir ../Edited")
    os.system("mkdir ../Published")
    os.system("mkdir ../Queue")
    os.system("mkdir ../Raw")
    os.system("mkdir ../RSS")
    os.system("mkdir ../Data")
    
    castList = '{"Setup Required":"false","podcasts":['
    for castFolder in podcasts:
        if castFolder != "":
            os.mkdir("../Edited/" + castFolder)
            os.mkdir("../Published/" + castFolder)
            os.mkdir("../Queue/" + castFolder)
            os.mkdir("../Raw/" + castFolder)
            os.mkdir("../RSS/" + castFolder)
            os.mkdir("../Data/" + castFolder)
            castList = castList + '"' + castFolder + '"' + ","
    castList = castList[0:-1]
    castList = castList + "]}"
    with open("dataStore.json", "w") as file:
        file.write(castList)
        file.close()            