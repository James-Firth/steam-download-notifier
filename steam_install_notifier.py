from os import listdir
from os.path import isdir, isfile, join, exists
from pynma import PyNMA
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
	NMA_api_key = config_file.readline().strip()
else:
	print "Error: Please add an NMA api key to your config_keys file"
	exit(1)

notifier = PyNMA(NMA_api_key)

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

def notify_android(name, id):
	print "Notifying about " + name
	res = notifier.push("Steam", "Finished Downloading", name, 'http://store.steampowered.com/app/'+k)
	print "NMA results: "
	print res
	return None


print "Beginning Loop..."
while (True):
	for k in downloading.keys():
		tmp_dir = join(root_dir, k)
		if exists(tmp_dir):
			pass
		else:
			print "Download complete! "+downloading[k]
			notify_android(downloading[k], k)
			del downloading[k]
	sleep(60)
	#print "Done sleeping!"
	downloading = get_game_names()
