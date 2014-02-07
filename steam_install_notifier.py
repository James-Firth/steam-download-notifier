import httplib, urllib
from os import listdir
from os.path import isdir, isfile, join, exists
from time import sleep
from sys import exit
import steamapi

#setup Steam API stuff
if isfile("config_keys"):
	config_file =open("config_keys", 'r')
	steam_api_key = config_file.readline().strip()
else:
	print "Error: Please add a steam key to your config_keys file"
	exit(1)
steamapi.core.APIConnection(api_key=steam_api_key)

if isfile("config_keys"):
	steam_id = config_file.readline().strip()
else:
	print "Error: Please add a steam key to your config_keys file"
	exit(1)

me = steamapi.user.SteamUser(steam_id)
myGames = me.games

#Setup PyNMA
if isfile("config_keys"):
	pushover_token = config_file.readline().strip()
else:
	print "Error: Please add an Pushover App Token key to your config_keys file"
	exit(1)

if isfile("config_keys"):
	pushover_user_key = config_file.readline().strip()
else:
	print "Error: Please add your Pushover Use Key to your config_keys file"
	exit(1)

#other variables
if isfile("config_keys"):
	root_dir = config_file.readline().strip()
else:
	print "Error: Please add the path to your steam/steamapps/downloading folder to your config_keys file"
	exit(1)

downloading = {}


def find_downloading():
	for f in listdir(root_dir):
		tmp = join(root_dir, f)
		if isdir(tmp):
			if(str(f) not in downloading.values()):
				downloading[f] = f
			else:
				print "already in there : "+str(f)
	return downloading

def get_game_names():
	downloading = find_downloading()
	for g in myGames:
		tmp_id = str(g.id)
		if str(tmp_id) in downloading:
			del downloading[tmp_id]
			downloading[tmp_id] = g.name
	return downloading

downloading = get_game_names()

def send_notification(name, id):
	print "Notifying about " + name
	res = notifier.push("Steam", "Finished Downloading", name, 'http://store.steampowered.com/app/'+k)
	conn = httplib.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
	  urllib.urlencode({
	    "token": pushover_token,
	    "user": pushover_user_key,
	    "title": "Steam Download Complete",
	    "message": name+" is now downloaded.",
	  }), { "Content-type": "application/x-www-form-urlencoded" })
	conn.getresponse()
	return None


print "Beginning Loop..."
while (True):
	for k in downloading.keys():
		tmp_dir = join(root_dir, k)
		if exists(tmp_dir):
			pass
		else:
			print "Download complete! "+downloading[k]
			send_notification(downloading[k], k)
			del downloading[k]
	sleep(60)
	#print "Done sleeping!"
	downloading = get_game_names()
