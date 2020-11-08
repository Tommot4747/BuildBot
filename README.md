# Welcome to the BuildBot wiki!
This bot was made at [LiquidHacks 2020](https://liquidhacks.devpost.com/) on November 6th-8th.  

![BuildBot](https://cdn.discordapp.com/attachments/774459422113267723/774838697274900480/BB-GIF.gif)  

[Devpost](https://devpost.com/software/build-bot?ref_content=user-portfolio&ref_feature=in_progress)

## Description

BuildBot is a bot made with the intent to help League of Legends players enhance their ranked experience at all ranks. The bot permits you to look up character builds and it will automatically find the top guides based on specific criteria from Mobafire. This will permit you to make that some calculated choices during the short champion selection screen. We hope to incorporate what we evaluate as essential functionality for ranked play and will eventually consider adding fun aspects.

## Technology Stack
- Python
- [Heroku](https://devcenter.heroku.com/)
- [Discord.py](https://discordpy.readthedocs.io/en/latest/index.html)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)
- More dependencies and requirements available in requirements.txt

## Usage Guidelines

| Commands and Parameters | Examples of usage | Description |
| :--- | :--- | --- |
| **acronym** | !bb | Acronym for the bot, use before command. |
| **build** | !bb build <championName> | Provides the best build for that champion as per our algorithm. |
| **counter** | !bb counter <championName> | Provides best and worst picks against given <championName> |
| **stats** | !bb stats <championName> | Will return default tips for the character from the LOL API and Winrates, Banrates, and Pickrates.Will also provide statistics about a given character for anyone who might require them. Helpful for last hitting and other detail-oriented aspects. |
| **info** | !bb info | Outputs command guidelines and documentation links. |

## Team members

- Zach
- Beau
- Alicia
- Tom 
