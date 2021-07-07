#!/usr/bin/env python3

"""Script for connecting discordBot to the discord Server"""

## os allows interaction with bash
import os
## importing discord api
import discord
## import for handling .env files
from dotenv import load_dotenv

load_dotenv()
## Discord token read into program from an environment variable fro security
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

## client represents connection to discord, similar to a sftp object
## handles events, tracks state, and interacts with Discord APIs
client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds: # loop through client.guilds data matching for guild name in .env
        if guild.name == GUILD:
            break
    print(f'{client.user} has connected to the following server:')  # print the bots name
    print(f'{guild.name}(id: {guild.id})')  # print the server name and id
    
    ## Print out the members of the server
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client.run(TOKEN)
