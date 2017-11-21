# BitBotBroker
BitBotBroker - Bot for automatic broker operations with BitCoins

## How to execute the application

1.- Create a virtual env: 

1.1.- Go to your home directory:

	`cd`

1.2.- Install virtualenvwrapper

	`sudo -H pip3 install virtualenvwrapper`

1.3.- Edit .bashrc

	`vim .bashrc`

1.4.- And paste inside

	`export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3 # What python interpreter I want to use for creating a virtualenv. This is NOT the interpreter that I will use during development`
	`export VIRTUALENV_PYTHON=/usr/bin/python3 # This is the interpreter I will use during development. It is optional. You can specify version of the interpreter when mkvirtualenv (creating an virtualenv) with the flag "-ppython3.5" or "-ppython2.7"`
	`source /usr/local/bin/virtualenvwrapper.sh # Execute the script to load environment variables. Source means execute script in current bash, not a new one.`
	
1.5.- If you're using another command line, run bash

	`bash`	
	
1.6.- Close the opened terminal and open a new one that will load the new config

1.7.- Create the virtual env (bitbotbroker can be the name of your choice for the virtual env):

	`mkvirtualenv bitbotbroker`	

1.8.- You can exit from this virtual env:

	`deactivate`
	
1.9.- Or return to it

	`workon bitbotbroker`

1.10.- Or even delete the virtualenv

	`rmvirtualenv bitbotbroker`		

2.- Install dependencies (within a virtualenv or not)

	`cd application`
	
	`sudo pip install -r requirements.txt`

3.- Check libs installed:

	`pip freeze`
	
4.- Configure config.ini file with the desired options

5.- Execute the application and pass the config file as an argument

	`python bitbotbroker config.ini`
