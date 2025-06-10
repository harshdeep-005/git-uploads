</p>
<h1 align = 'center'>News Aggregator</h1>
<br>

<br>

[![](https://img.shields.io/badge/Made_with-Python3-blue?style=for-the-badge&logo=python)](https://www.python.org "Python3")[![](https://img.shields.io/badge/Made_with-Django-blue?style=for-the-badge&logo=django)](https://www.djangoproject.com/ "Django")

</p>

## Description

News aggregator is a Django project to scrape a news website using Beautiful soup and request module and hence combination of web crawlers and web applications.
Both of these technologies have their implementation in Python.

## Features

Our news aggregator works in 3 steps:<br>
1.It scrapes the news website for the articles.In this Django project, we are scraping a website 'www.theonion.com'<br>
(We have scraped news articles from 'latest' section of 'www.theonion.com' for demonstration)<br>
2.Then it stores the article’s images, links, and title.<br>
3.The stored objects in the database are served to the client. The client gets information in a nice template by clicking the 'Load news' button and select the different options available to you.The options are: India, Business, Sports, Politics, Education<br>

        ----------------------------------------------------------------------------------------
### Screenshots ###
## Latest
![]([https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/latest_light_mode.PNG](https://github.com/harshdeep-005/git-uploads/blob/main/Screenshot%202025-06-10%20183724.png?raw=true))
![]([https://github.com/sam-boghara/News-Aggregator/blob/master/screenshots/latest_night_mode.PNG](https://github.com/harshdeep-005/git-uploads/blob/main/Screenshot%202025-06-10%20183754.png?raw=true))
## Different Types
![](https://github.com/harshdeep-005/git-uploads/blob/main/Screenshot%202025-06-10%20183839.png?raw=true)
## India
![](https://github.com/harshdeep-005/git-uploads/blob/main/Screenshot%202025-06-10%20185710.png?raw=true)
## Sports
![](https://github.com/harshdeep-005/git-uploads/blob/main/Screenshot%202025-06-10%20185727.png?raw=true)
## Politics
![](https://github.com/harshdeep-005/git-uploads/blob/main/Screenshot%202025-06-10%20185753.png?raw=true)
## Education
![](https://github.com/harshdeep-005/git-uploads/blob/main/Screenshot%202025-06-10%20185809.png?raw=true)
## Whatsapp share
![](https://github.com/harshdeep-005/git-uploads/blob/main/Screenshot%202025-06-10%20183929.png?raw=true)
## Telegram share
![](https://github.com/harshdeep-005/git-uploads/blob/main/Screenshot%202025-06-10%20183948.png?raw=true)
## Copy to clipboard
![](https://github.com/harshdeep-005/git-uploads/blob/main/Screenshot%202025-06-10%20184029.png?raw=true)
---------------------------------------------------------------------------------------

## How To Use

#### Software Requirements

Python3, Django

#### Installation
Step 1 : Run cmd as adminstrator

Step 2 : Change the path.

Step 3 : Create a virtual Environment

Step 4 : Run "pip install -r requirements.txt"
Install the dependencies by running:
```html  
    pip install bs4
    pip install requests
    pip install django-social-share
```

#### Run using Command Prompt
Step 5 : RUn "python manage.py runserver"
Navigate to the News-Aggregator folder which has manage.py file then run the following command on cmd

```html
python manage.py runserver
```
Step 6 : open the server through link
### Tech stack

`Backend` : Python3,Beautiful soup <br>
`Framework` : Django <br>
`Database` : Sqlite3 <br>
`Frontend` : Html,CSS,Bootstrap <br>
