# backend-for-FIPUbot

backend for FIPUbot web-app: https://github.com/mvisnjic/FIPUbot

## How to download and install local

1. clone a repo
   `git clone [project name] # git clone`
2. go to project folder
   `cd [project name] # enter to project dir`
3. install virtual environment (py,python,python3)
   `py -m venv venv # creating venv`

4. activate virtual environment

   1. windows:
      `.venv/Scripts/activate`
   2. linux/unix:
      `source ./venv/bin/activate #activating venv`

5. installing dependencies
   `pip install -r ./requirements.txt`

6. for starting an app
   `flask run`

- leaving virutal environment
  `deactivate`

_It needs about 10 min to install all dependencies, and few minutes for run the app._
_For sending an emails, you need to mkdir .env and put USERNAME = domain name, SERVER = server name, and PASSWORD_

## source

basis of chatbot in python built using: https://towardsdatascience.com/a-simple-chatbot-in-python-with-deep-learning-3e8669997758
