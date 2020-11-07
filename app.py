import os, sys
sys.path.append(os.path.abspath('..'))
from discord import Client
from discord.ext.commands import Bot
# from config import discord_key, owners_ids ## Test
from data.lol_champs import lol_champ_list

discord_key = os.environ.get('discord_key') ## Prod
command_prefix = '!bb '

build_bot = Bot(command_prefix=command_prefix) ## Prod
# build_bot = Bot(command_prefix=command_prefix,
#                  owner_ids=list(owners_ids.values())) ## Test


@build_bot.event
async def on_ready():
	print(f'Bot connected as {build_bot.user}')
	

@build_bot.command()
async def build(ctx, *, champion):
    clean_champ = str(champion).lower().strip()
    lol_list = list(map(lambda x: x.lower().strip(), lol_champ_list))
    if clean_champ in lol_list:
        await ctx.send(f'You have chosen {clean_champ.title()}')
    else:
        suggestion_list = list(filter(lambda x: x[0].lower() == clean_champ[0], lol_champ_list))
        suggestion = ', '.join(suggestion_list)
        if suggestion_list == []:
            await ctx.send(f'We cannot find anything close to {champion}.')
        else:
            await ctx.send(f'We cannot find {champion}, Do you mean one of these? {suggestion}')


build_bot.run(discord_key)