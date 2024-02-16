# Basics with Selenium

Repository for development and study of the Selenium module and development of web scrapping applications.

## Projects

## 1. Automating Facebook Posting

The `facebook_automation.py` program opens a new browser, logs in to the user account, opens the status posting field, types a message and finishes posting.

Among the functions developed:

- load the module driver `app.py`
- type in a humanized way to avoid bot detection
- log in to the Facebook website
- open post field and type the message
- carry out the posting and finalize the program

### How to use:

Prerequisites:

- Chrome Browser:

```
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
$ sudo dpkg -i google-chrome-stable_current_amd64.deb
$ sudo apt install -f
```

- pip: `sudo apt install python3-pip`
- curl: `sudo apt install curl`
- Create `.env` file with the following variables:

```
FACEBOOK_LOGIN=<your_login>
FACEBOOK_SENHA=<your_password>
```
    
Download the following files:

```
$ curl -O https://raw.githubusercontent.com/eliasalbuquerque/python-selenium/develop/facebook_automation.py
$ curl -O https://raw.githubusercontent.com/eliasalbuquerque/python-selenium/develop/app.py
$ curl -O https://raw.githubusercontent.com/eliasalbuquerque/python-selenium/develop/config.ini
$ curl -O https://raw.githubusercontent.com/eliasalbuquerque/python-selenium/develop/requirements.txt
```

Install the requirements: 

```
$ pip3 install -r requirements.txt
```

Run the program:

```
$ python3 facebook_automation.py
```

The program will open the Chrome browser, log in and then make a post.



---

## 2. Automating Instagram likes

Using the Selenium module, automation of liking recent posts from a page on Instagram was developed.

Among the functions developed:

- loads the driver and wait: website access settings and waiting times in relation to window elements
- checks the visibility of elements in the DOM according to need, one element, all elements, any elements, clickable element
- type in a humanized way to avoid bot detection
- log in to the instagram website
- like the last post if it hasn't been liked yet

### How to use:


- Chrome Browser:

```
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
$ sudo dpkg -i google-chrome-stable_current_amd64.deb
$ sudo apt install -f
```

- pip: `sudo apt install python3-pip`
- curl: `sudo apt install curl`
- Create a `.env` file with the following variables:

```
INSTAGRAM_LOGIN=<your_login>
INSTAGRAM_SENHA=<your_password>
```
    
Download the following files:

```
$ curl -O https://raw.githubusercontent.com/eliasalbuquerque/python-selenium/develop/instagram_automation.py
$ curl -O https://raw.githubusercontent.com/eliasalbuquerque/python-selenium/develop/app.py
$ curl -O https://raw.githubusercontent.com/eliasalbuquerque/python-selenium/develop/config.ini
$ curl -O https://raw.githubusercontent.com/eliasalbuquerque/python-selenium/develop/requirements.txt
```

Install the requirements: 

```
$ pip3 install -r requirements.txt
```

Run the program:

```
python3 instagram_automation.py
```

The program opens the Chrome browser, opens the Instagram website, logs in, waits for the page to load, accesses the page of interest, opens the latest post, checks if it has already been liked, if not, likes the post and closes the browser.