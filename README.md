# MeowgicMatt
Welcome to Meowgic Matt, the [Magician For Ca(s)ts!](https://vimeo.com/48335984)

This is a python script meant to run in a command line to help automate and speed up some tasks in a podcast production workflow.

Overall, this is designed by [Andrew Whipple](http://andrewwhipple.com) (me!) and SPECIFICALLY set up for my workflow in producing my [podcasts](http://thatpodcastthing.com), so mileage may vary. But feel free to use and modify as you see fit! It's MIT Licensed, so rock and roll.

ALSO VERY IMPORTANT: this is held together with string. There's almost no error checking. If anything is a little bit off, it'll break, and maybe break disasterously. It works for me at the moment, but no promises it will work for you. So use at your own risk.

##Features:

####RSS Management:
You can use Meowgic Matt to create iTunes-complaint RSS feeds, add episodes to the feed, and (if you host your rss file via a git-controlled site) automatic pushing to git.

####Mp3 Management and Conversion:
The file structure of Meowgic Matt is meant to help track the progress of an mp3 file through raw recording, editing, queuing, and a published archive. Additionally, it adds a wrapper to the LAME conversion engine to get mp3 files well-sized, but still nice sounding, for most podcast needs.

####Organization:
This whole script is EXTREMELY opinionated about how to structure the file directory and how to name files, which can be a good thing! In the pursuit of maximum laziness (or as some may call it, "efficiancy") on the part of the podcast producer, if you want to use this script you actually have to stick to a reasonable and well-organized set of conventions. Which is good for keeping track of things. You'll probably thank me when you have to hunt down a rogue mp3 somewhere.

####Lightweight....-ness?
This is just a a little under 400 lines of python scripts, and all data storage is in some JSON files. Nothing fancy.


##Eventual Features:

####One-Step Publishing:
Well, maybe not truly "one-step," but in the future, if you follow naming and organization conventions and use git-controlled sites to host RSS files, you can do super speedy and automated publishing!

####Better Modularity
Some sort of flag system to let you customize Meowgic Matt for your needs. Only want to do mp3 conversion? Awesome, you get a version of the script with only that. Just RSS? Neato, say bye forever (or until you flip a flag) to mp3s.

####Support for more audio filetypes and conversion
If someone knows a good aiff -> mp3 or aac -> mp3 command line converter, I'll link it up.

####Better Data Storing and Flagging
Right now there's just a JSON file that stores information about your shows and Meowgic Matt setup. If I get better at File I/O and parsing/editing JSON programmatically, then hopefully more flags and info can be stored there to make it even easier and more consistent to use. Though I don't think I'll ever go the route of a real database, because that's a bit more heavyweight than I want this tool to be.

####???
You tell me bro. Most likely any new features will be added because, in producing my own shows, I'll want something automated, but if you use this and like it and want something, let me know! No promises, but if I'm bored and have free time, I'll probably tinker with it.


#Requirements:

* A unix command line with standard mkdirs and rms and what have you
* Python. I have 2.7.10, and it works, but I don't know how far back you can go without breaking.
* [LAME Mp3 Encoder](http://lame.sourceforge.net)

#How To Use:

###First Steps:
1. Either download the folder and unzip, or git clone the MeowgicMatt folder wherever you want on your machine.
2. *If you use a Git-controlled site to host RSS, and want to automate git pushes:* Open "code/meowgicMatt.py" and at the top of the file, edit the gitFolder and gitRSSFolder globals to the appropriate file paths for your machine.
3. Navigate to the "code" folder, and run "python meowgicMatt.py"
4. Follow the on-screen instructions to add your first podcasts.

If you ever want to add another podcast to use with Meowgic Matt, the process will be similar, but go enter 'pod' from the main menu and follow the on-screen instructions.

###Conventions:
The file system is structured as follows:

* The code to run, including all the modules, lives in the "Code" folder
* There are six other folders, each featuring a sub-folder for each podcast.
* * "Raw" is meant for unedited recordings of shows
* * "Edited" is for edited mp3s, but are unconverted or otherwise unready for publishing
* * "Queue" is for mp3 files that are converted and completely ready to upload
* * "Published" is an archive for published show mp3s
* * "RSS" is for the RSS feeds for each show
* * "Data" is for (optional) JSON data storing podcast feed information and show notes for individual episodes

To make the best use of the software, documents should be named as follows:

* Podcast subfolders should be named all one word, lower-case. Ex: "mycoolshow"
* RSS feeds should be named IDENTICALLY to the podcast folder, with a .xml extension. Ex: "mycoolshow.xml"
* If using JSON in the "Data" folder to store podcast information, the file for the overall show information should be named IDENTICALLY to the podcast folder. Ex: "mycoolshow.json"
* If using JSON in the "Data" folder to store episode information, each episode file should be named with the podcast folder name with the first letter capitalized, followed by "Ep" and the episode number. Ex: "MycoolshowEp1.json"
* Mp3 files should be named IDENTICALLY to the episode JSON. Ex: "MycoolshowEp1.mp3"

Additionally, it's expected you have your podcasts in mp3 format, and do any conversion from other file formats elsewhere and on your own time. Meowgic Matt only likes mp3s at the moment.

###RSS:

* From the main menu, type 'rss' to access RSS management features.
* Creating a new podcast feed:
* * From the RSS menu, type 'feed'
* * Enter the name of the podcast folder
* * If using JSON (documented below) enter the JSON filename for the podcast
* * Else hit enter leaving it blank to enter feed information individually via the command line.
* Adding a new episode to an existing feed:
* * From the RSS menu, type 'ep'
* * Enter the name of one of the available podcasts listed
* * If using JSON (documented below) enter the JSON filename for this podcast episode
* * Else hit enter leaving it blank to enter feed information individually via the command line.
* If hosting RSS file via a git-controlled site, pushing the RSS to git
* * From the RSS menu, type 'git'
* * If the git folder filepath is not set, quit and enter it in the top of "meowgicMatt.py"
* * Once set, enter the name of the podcast to push the feed.

**JSON For RSS**

Rather than entering things for RSS feed creation via the command line, which can be quite tedious, it can be written into a JSON file and read by the Meowgic Magician itself. In the "Code" folder lives a demo file called "podcast.json" that has the info needed for creating the base feed with overall podcast information. Duplicate this file, rename it according to the name of your shows podcast folder (see Naming Conventions above!) and move into the "Data/podcastname" subfolder.

Similarly, there is a file "episode.json" that is a demo of the information needed for an individual episode. Duplicate this file, rename it according to naming conventions, and fill out the info with the appropriate stuff for that episode, then move it to "Data/podcastname"

###Mp3:

You don't even need to use the actual program, beyond setup, to use the first useful mp3 tool: a set of organized folders to track the production of the mp3 files. YAY ORGANIZATION!

All the other fun stuff Meowgic Matt uses are just wrappers for the LAME conversion engine, so make sure you have that, or you'll run into all kinds of errors.

To do mp3 conversion:

* Make sure you have an edited episode, ready to convert, in mp3 format in the "Edited/podcastname" subfolder.
* From the main menu, type 'mp3'
* Enter the name of the podcast you want to work with.
* Give the episode number [Note: if naming conventions aren't followed, ALL KINDS OF THINGS WILL BREAK]
* Pluck the converted mp3 file from the "Queue/podcastname" subfolder, and publish!

###Meowgic Management:

To add a new podcast, type 'pod' from the main menu and follow the on-screen instructions.

To reset Meowgic Matt to its factory conditions, type 'reset' from the main menu. BUT BE WARNED: this will delete ANYTHING in the subfolders, so if that's the only location for your mp3 files, or RSS stuff, or show notes, or what have you, it will ALL BE GONE. BE VERY VERY VERY CAREFUL WITH RESETING. IT IS A NUCLEAR OPTION.
