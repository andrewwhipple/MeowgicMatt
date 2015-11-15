#Meowgic Matt reset module

import os
import json

#Debug function to call out that the module successfully loaded.
def meow():
    print("mreset loaded")
  
#Resets Meowgic Matt to factory conditions, DELETING EVERYTHING CURRENTLY IN SUBFOLDERS.   
def reset():
    os.system("rm -rf ../Edited/")
    os.system("rm -rf ../Published/")
    os.system("rm -rf ../Queue/")
    os.system("rm -rf ../Raw/")
    os.system("rm -rf ../RSS/")
    os.system("rm -rf ../Data/")
    with open("dataStore.json", "r") as dataReadFile:
        data = json.load(dataReadFile)
        podcasts = data["podcasts"]
        for cast in podcasts:
            os.system("rm -rf " + cast + "/")
        dataReadFile.close()
    with open("dataStore.json", "w") as dataWriteFile:
        resetDataString = '{"Setup Required":"true","podcasts":[]}'
        dataWriteFile.write(resetDataString)
        dataWriteFile.close()
    print "\nMeowgic Matt Reset!\n"    