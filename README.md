steam-download-notifier
=======================

Uses Python and the Android app [Notify My Android](https://www.notifymyandroid.com) to push notifications to your phone when a Steam game finishes downloading.

Great for those really downloads for games you can't wait to play!

##Installation & API Keys

1. Download the zip file or clone this repo and unzip it wherever you'd like.
2. Get a [Steam API Key](http://steamcommunity.com/dev/apikey) (for grabbing game names) and replace the first line of config_keys with it.

2. Get your steam ID # and replace the 2nd line of config_keys with it. If you don't have a custom url steam community url you can find it on your profile. If not use [this tool](http://steamidconverter.com/) to find it quicky

3. Generate an [NMA api key](https://www.notifymyandroid.com/account.jsp) and replace the 3rd line of config_keys with it

4. Replace the 4th line of the config_keys file with the location of your 'downloading' folder for Steam. Found somewhere like C:\Steam\steamapps\downloading

5. Now navigate to where you unzipped the repo and the run the command `python steam_install_notifier.py`

You should be good to go now!
The default is for it to check every minute from the time you start.

### Future Plans:
* Variable check intervals.
* Update and Download notifications separately.
* More notification options.
* More options in general