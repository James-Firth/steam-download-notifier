Steam Download Notifier
=======================

Uses Python (2.7) and the iOS/Android app [Pushover](https://pushover.net) to push notifications to your phone when a Steam game finishes downloading.

Great for those really long downloads for games you can't wait to play!

##Installation & API Keys

1. Download the zip file or clone this repo and unzip it wherever you'd like.
2. Get a [Steam API Key](http://steamcommunity.com/dev/apikey) (for grabbing game names) and replace the first line of config_keys with it.

2. Get your steam ID # and replace the 2nd line of config_keys with it. If you don't have a custom url steam community url you can find it on your profile. If not use [this tool](http://steamidconverter.com/) to find it quicky

3. Register a [Pushover Application](https://pushover.net/apps/build) and replace the 3rd line of config_keys with it

4. Replace the 4th line of config_keys with your Pushover User Key

5. Replace the 5th line of the config_keys file with the location of your 'downloading' folder for Steam. Found somewhere like C:\Steam\steamapps\downloading

6. Now navigate to where you unzipped the repo and the run the command `python steam_install_notifier.py`

You should be good to go now!
The default is for it to check every minute from the time you start.

### Testing
* I've only tested it with my steam profile which is public. If private steam profiles don't work, please add it as an issue!
* Only tested on Windows 7 so far.

### Future Plans:
* Variable check intervals.
* Update and Download notifications separately.
* More notification options.
* More options in general

### Libraries used:
* [steamapi](https://github.com/scottrice/steamapi) to make the steam Web API calls through Python easier.
Note: Both of these are licensed under the MIT License and the License remains in the appropriate folder.

### Legal Notes:

* This is licensed under the [MIT License](https://tldrlegal.com/license/mit-license) so pretty well do what you want, just please attribute me if you change it and don't blame me if something explodes.
* Be aware of the API call limits of Steam and NMA
** So don't download/update more than 800 games per hour or 100,000 per day
