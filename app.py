import os
from discord import Client
from discord.ext.commands import Bot
# from config import discord_key, owners_ids ## Test

discord_key = os.environ.get('discord_key') ## Prod
command_prefix = '/bb '

build_bot = Bot(command_prefix=command_prefix) ## Prod
# build_bot = Bot(command_prefix=command_prefix, owner_ids=list(owners_ids.values()))


@build_bot.event
async def on_ready():
	print(f'Bot connected as {build_bot.user}')
	

@build_bot.command()
async def message(ctx, champion):
    await ctx.send(f'Sup bro, you said {champion}')


build_bot.run(discord_key)