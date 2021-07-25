<p align="center">
  <img src="./resources/extras/logo_readme.jpg" alt="TeamShizu Logo">
</p>
<h1 align="center">
  <b>Shizu - UserBot</b>
</h1>

<b>A stable pluggable Telegram userbot + vc music bot, based on Telethon.</b>   

[![Stars](https://img.shields.io/github/stars/TeamShizu/ShizuUser?style=flat-square&color=yellow)](https://github.com/TeamShizu/ShizuUser/stargazers)
[![Forks](https://img.shields.io/github/forks/TeamShizu/ShizuUser?style=flat-square&color=orange)](https://github.com/TeamShizu/ShizuUser/fork)
[![Size](https://img.shields.io/github/repo-size/TeamShizu/ShizuUser?style=flat-square&color=green)](https://github.com/TeamShizu/ShizuUser/)   
[![Python](https://img.shields.io/badge/Python-v3.9-blue)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/TeamShizu/ShizuUser/graphs/commit-activity)
[![Docker Pulls](https://img.shields.io/docker/pulls/programmingerror/ShizuUser?style=flat-square)](https://img.shields.io/docker/pulls/programmingerror/ShizuUser?style=flat-square)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/TeamShizu/ShizuUser)   
[![Contributors](https://img.shields.io/github/contributors/TeamShizu/ShizuUser?style=flat-square&color=green)](https://github.com/TeamShizu/ShizuUser/graphs/contributors)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
[![License](https://img.shields.io/badge/License-AGPL-blue)](https://github.com/TeamShizu/ShizuUser/blob/main/LICENSE)

----

# Deploy
- [Heroku](#Deploy-to-Heroku)
- [Local Machine](#Deploy-Locally)


# Tutorial 
- Full Tutorial - [![Full Tutorial](https://img.shields.io/badge/Watch%20Now-blue)](https://www.youtube.com/watch?v=9wF7k9qA0Q4)

- Tutorial to get Redis URL and password - [here.](./resources/extras/redistut.md)
---

## Deploy to Heroku
Get the [Necessary Variables](#Necessary-Variables) and then click the button below!  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FTeamShizu%2FShizuUser)

## Deploy Locally
- [Traditional Method](#local-deploy---traditional-method)
- [Easy Method](#local-deploy---easy-method)

### Local Deploy - Easy Method
- Linux - `bash -c "$(curl -fsSL https://git.io/JY9UM)"`
- Windows - `cd desktop ; wget https://git.io/JY9UM -o locals.py ; python locals.py`
- Termux - `sh -c "$(curl -fsSL https://git.io/JY9UM)"`

### Local Deploy - Traditional Method
- Get your [Necessary Variables](#Necessary-Variables)
- Clone the repository: <br />
`git clone https://github.com/TeamShizu/ShizuUser.git`
- Go to the cloned folder: <br />
`cd Shizu`
- Create a virtual env:   <br />
`virtualenv -p /usr/bin/python3 venv`
`. ./venv/bin/activate`
- Install the requirements:   <br />
`pip(3) install -U -r requirements.txt`
- Generate your `SESSION`:
  - For Linux users:
    `bash sessiongen`
     or
    `bash -c "$(curl -fsSL https://git.io/JY9JI)"`
  - For Termux users:
    `sh -c "$(curl -fsSL https://git.io/JqgsR)"`
  - For Windows Users:
    `cd desktop ; wget https://git.io/JY9JI -o Shizu.py ; python Shizu.py`
- Fill your details in a `.env` file, as given in [`.env.sample`](https://github.com/TeamShizu/ShizuUser/blob/main/.env.sample).
(You can either edit and rename the file or make a new file named `.env`.)
- Run the bot:
  - Linux Users:
   `bash resources/startup/startup.sh`
  - Windows Users:
    `python(3) -m pyShizuUser`

## Necessary Variables
- `API_ID` - Your API_ID from [my.telegram.org](https://my.telegram.org/)
- `API_HASH` - Your API_HASH from [my.telegram.org](https://my.telegram.org/)
- `SESSION` - SessionString for your accounts login session. Get it from [here](#Session-String)
- `REDIS_URI` - Redis endpoint URL, from [redislabs](http://redislabs.com/), tutorial [here.](./resources/extras/redistut.md)
- `REDIS_PASSWORD ` - Redis endpoint Password, from [redislabs](http://redislabs.com/), tutorial [here.](./resources/extras/redistut.md)

## Session String
Different ways to get your `SESSION`:
* [![Run on Repl.it](https://replit.com/badge/github/TeamShizu/ShizuUser)](https://replit.com/@TeamShizu/ShizuUser)
* Linux : `bash -c "$(curl -fsSL https://git.io/JY9JI)"`
* PowerShell : `cd desktop ; wget https://git.io/JY9JI ; python Shizu.py`
* Termux : `sh -c "$(curl -fsSL https://da.gd/termux-tel)"`
* TelegramBot : [@SessionGeneratorBot](https://t.me/SessionGeneratorBot)

Made with 💕 by [@TeamShizu](https://t.me/ShizuUpdates). <br />

# License
Shizu is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)

# Credits
* [![TeamShizu-Devs](https://img.shields.io/static/v1?label=TeamShizu&message=devs&color=critical)](https://t.me/ShizuUpdates)
