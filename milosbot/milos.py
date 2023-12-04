# --- milos.py --------------------------------------------------------- #
# --------------------------------------------------------------------- #
# Date   :	02/12/2023                                                  #
# Author :	Robin Reggiani                                              #
# --------------------------------------------------------------------- #

# --- Imports --------------------------------------------------------- #
import discord
from discord import Intents
from discord.ext import commands
from main import token
import milosbot.functions.send_message as sending_task
from milosbot import milos_commands

# --------------------------------------------------------------------- #

# --- Constants ------------------------------------------------------- #
# --------------------------------------------------------------------- #

# --- Data structures ------------------------------------------------- #
# --------------------------------------------------------------------- #

# --- Variables ------------------------------------------------------- #
TOKEN = token['milos_token']
milosIntents: Intents
milosCommands: milos_commands
# --------------------------------------------------------------------- #


# --- Events ---------------------------------------------------------- #
def client_events(milos_bot):
    @milos_bot.event
    async def on_ready():
        print(f'{milos_bot.user} is now running')
        print(f'Guild: {milos_bot.guilds}')
        try:
            sync = await milos_bot.tree.sync()

            print(f"Sync {len(sync)} commands(s)")
        except Exception as ex:
            print(ex)

    @milos_bot.event
    async def on_message(message):
        if message.author == milos_bot.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f"{username} said '{user_message}' ({channel})")
        await sending_task.send_message(message, user_message)

    #@milos_bot.tree.command()
    #async def settings(ctx: discord.Interaction):
        #await ctx.response.send_message('Settings run')
        #milos_bot.tree.clear_commands(guild=ctx.guild)
        #await milos_bot.tree.sync(guild=ctx.guild)
# --------------------------------------------------------------------- #


# --- Methods & Functions --------------------------------------------- #
def milos_run():
    global milosIntents
    global milosCommands
    milosIntents = discord.Intents.default()
    milosIntents.message_content = True
    milos_bot = commands.Bot(command_prefix=commands.when_mentioned_or("/"), intents=milosIntents)
    milosCommands = milos_commands.MilosCommands(reference_event=milos_bot)
    client_events(milos_bot)
    milos_bot.run(TOKEN)
# --------------------------------------------------------------------- #
