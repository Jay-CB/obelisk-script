# obelisk-script

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL License][license-shield]][license-url]


<br />
<p align="center">

  <h3 align="center">Obelisk-Script</h3>

  <p align="center">
    A Discord Bot script to automate the obelisk bot
    <br />
    <a href="https://github.com/DevJ4Y/obelisk-script"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/DevJ4Y/obelisk-script/issues">Report Bug</a>
    ·
    <a href="https://github.com/DevJ4Y/obelisk-script/issues">Request Feature</a>
  </p>
</p>

![alt text](https://imgur.com/a/LGz8YiB)



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a discord bot script that i made to automate the obelisk bot.

Why did i make it?:
* They changed their bot detection to a new method that i figured a way around
* I wanted to test if it was possible and if i myself could make it
* I also enjoy making bot - even if they are poorly made

The bot has a few features:
* Will check all cooldowns on start and convent them to timestamps - it currently only uses a few of them but they are all there
* The hunt and gather command will run a few seconds after their cooldown with some random in there.
* The Quest and Daily commands are also automated
* A user can send commands to the bot over discord

### Built With

* [Discord.py](https://github.com/Rapptz/discord.py)


## Getting Started

It's easy to use, you will need [Discord.py](https://github.com/Rapptz/discord.py) and Python 3

### Prerequisites

* Discord.py
  ```sh
  python3 -m pip install discord.py
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/DevJ4Y/obelisk-script.git
   ```
2. Install the Discord.py lib

3. Edit the Obot.py and add the account token on the last line - within the ""

<!-- USAGE EXAMPLES -->
## Usage

All these commands are to be sent to the bot via discord

To control the bot from another discord account, first you will need to assign your user as the admin. Anyone can do this if they know how.
```sh
.login
```

ping - Will return a pong to check all is running ok
```sh
ping
```

toggle - toggle on or off both the hunt and gather automation
```sh
toggle h
```
```sh
toggle g
```

stop loop - stops the main think loop for all the commands
```sh
stop loop
```

start loop - starts the main think loop for all the commands
```sh
start loop
```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the GPL - 3.0. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

&lt;J4Y&gt; - [My site](https://www.j4y.dev)

Project Link: [https://github.com/DevJ4Y/obelisk-script](https://github.com/DevJ4Y/obelisk-script)


[forks-shield]: https://img.shields.io/github/forks/DevJ4Y/obelisk-script?style=for-the-badge
[forks-url]: https://github.com/DevJ4Y/obelisk-script/network/members
[stars-shield]: https://img.shields.io/github/stars/DevJ4Y/obelisk-script?style=for-the-badge
[stars-url]: https://github.com/DevJ4Y/obelisk-script/stargazers
[issues-shield]: https://img.shields.io/github/issues/DevJ4Y/obelisk-script?style=for-the-badge
[issues-url]: https://github.comDevJ4Y/obelisk-script/issues
[license-shield]: https://img.shields.io/github/license/DevJ4Y/obelisk-script?style=for-the-badge
[license-url]: https://github.com/DevJ4Y/obelisk-script/blob/main/LICENSE
