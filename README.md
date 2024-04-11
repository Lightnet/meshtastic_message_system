# meshtastic_message_system

# License: MIT

# Created By: Lightnet

# Information:
  This is just prototype plan stage.

  Using the javascript to reduce coding. As vanjs is about 2 kB. For develop UI web components.

  It would have some basic feature. 

  Create web infereface is not easy task when building with the meshtastic which is handle different in logic. As for the query message it need some setup.

  Meshtastic has limited data send is 50 kb. Just check the doc. Work in progress specs.

# Notes:
 This is early stage testing.

 Will try to keep it very simple code for web server build.

 For reason for the account is to prevent unauth access for web server or other ways to chat message.


# flask default:
 * static
 * templates

# Set up DEV:
```
pip3 install --user pipenv
```

## Install packages:
```
pipenv install -r requirements.txt
```

## run shell env:
```
pipenv shell
```

# Save package:
```
pipenv requirements > requirements.txt

pipenv run pip3 freeze > requirements.txt
```
 * https://stackoverflow.com/questions/51845562/how-to-freeze-a-requirement-with-pipenv

# run server:
```
flask --app flash_server run
```

```
py app.py
#or
python app.py
```
https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application

https://www.geeksforgeeks.org/how-to-run-a-flask-application/

# Using the Meshtastic Python Library:
 * https://meshtastic.org/docs/development/python/library/
 * https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
