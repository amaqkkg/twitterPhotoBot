
# Twitter Photo Bot

automatic photo bot post on twitter
 
### Installing:

1. Clone and installing twython:

	`git clone https://github.com/amaqkkg/twitterPhotoBot.git`

	`sudo apt-get install python-setuptools`

	`sudo easy_install pip`

	`sudo pip install twython`

2. Change TwitterBot.py permission:

	`sudo chmod +x TwitterBot.py`

  

3. Automatic execution with cron job:

	using `sudo crontab -e` on Unix/Linux systems for periodically executing this script.

	you can use this if you want to execute the script every hour:

	`0 * * * * python /address/to/TwitterBot.py`
	
	or go to [crontab-generator](https://crontab-generator.org/) for more settings.