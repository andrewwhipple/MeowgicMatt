# WELCOME TO MEOWGIC MATT, The Magician For Ca(s)ts


#Import custom meowgic matt modules (which MUST be included in the project folder)
import mrss
import mconvert
import msetup
import mreset

#Other standard imports
import sys
import json
import os

#Sets the environment, either 'dev' (enabling some logging) or 'prod'
env = "prod"

#Optional git info: if the rss is pushed to a server via git, the pushing can be automated. 'gitFolder' is the base folder for the git directory, and 'gitRSSFolder' is the RELATIVE path from the base folder. Aka, gitFolder + gitRSSFolder should give the full file path to where you want the rss feed to go.
gitFolder = ""
gitRSSFolder = ""

#A quick introduction to Meowgic Matt
def welcome():
    print "\nWelcome to Meowgic Matt, the Magician for Ca(s)ts!\n"

#Checks to see if the "Setup Required" flag is set to true or false
def checkDataStore():
    with open("dataStore.json") as dataFile:
        data = json.load(dataFile)
        if (data["Setup Required"] == "true"):
            return True
        else:
            return False    
    return false
    
def setup():
    print "Setting up!"
    msetup.setup()    
    
#Wrapper function to handle RSS features
def rss():
    option = raw_input("\nCreate new feed ('feed'), Add episode to existing feed ('ep'), or push feed via git ('git')?\n")
    if option == "feed":
        mrss.createFeed()
    elif option == "ep":
        mrss.addEpisode()
    elif option == "git":
        if (gitFolder == ""):
            print("\n Git Folder not set! Open the meowgicMatt.py file and set the file paths to where you want the RSS to go.")
            menu()
        else:  
            mrss.pushToGit(gitFolder, gitRSSFolder)
    else: 
        menu()

def mp3():
    mconvert.convert()
    
def oneClick():
    print "Nothing here at ze moment."

    
def resetWrapper():
    confirm = raw_input("\nWARNING: This will delete ALL DATA in these folders, including settings, RSS feeds, any mp3 files, and episode info. \n\nAre you sure you want to continue? ('yes' or 'no')\n")
    if (confirm == "yes"):
        mreset.reset()
        print "\nShutting down Meowgic Matt. Bye!\n"
        sys.exit()
    else:
        menu()  
          
#Main menu loop                
def menu():
    option = raw_input("\nUpdate RSS ('rss'), Prep Mp3 ('mp3'), Create New Podcast ('pod'), Reset ('reset'), or Quit ('quit')?\n")  
    if option == "rss":
        rss()
        menu()
    elif option == "pod":
        msetup.newPodcastSetup()
        menu()
    elif option == "one":
        oneClick()
        menu()
    elif option == "mp3":
        mp3()
        menu()    
    elif option == "reset":
        resetWrapper()
        menu() 
    elif option == "quit":
        print "\nShutting down Meowgic Matt. Bye!\n"
        sys.exit()
    else: 
        menu()
        
#The main function, entry point into the script
def main():
    if env == "dev":
        mrss.meow()
        mconvert.meow()
        msetup.meow()
    #Check if data store flag says it needs to be set up, and if so set up!
    welcome()
    if (checkDataStore()):
        setup()
    menu()
    
main()