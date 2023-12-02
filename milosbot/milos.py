# --- milos.py --------------------------------------------------------- #
# --------------------------------------------------------------------- #
# Date   :	02/12/2023                                                  #
# Author :	Robin Reggiani                                              #
# --------------------------------------------------------------------- #

# --- Imports --------------------------------------------------------- #
import discord
from discord import Intents
from main import env
import milosbot.functions.send_message as sending_task

# --------------------------------------------------------------------- #

# --- Constants ------------------------------------------------------- #
# --------------------------------------------------------------------- #

# --- Data structures ------------------------------------------------- #
# --------------------------------------------------------------------- #

# --- Variables ------------------------------------------------------- #
TOKEN = env['milos_token']
milosIntents: Intents
milosClient: discord.Client
# --------------------------------------------------------------------- #


# --- Events ---------------------------------------------------------- #
def client_events(milosClient):
    @milosClient.event
    async def on_ready():
        print(f'{milosClient.user} is now running')

    @milosClient.event
    async def on_message(message):
        if message.author == milosClient.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f"{username} said '{user_message}' ({channel})")
        await sending_task.send_message(message, user_message)
# --------------------------------------------------------------------- #


# --- Methods & Functions --------------------------------------------- #
def milos_run():
    global milosIntents
    global milosClient
    milosIntents = discord.Intents.default()
    milosIntents.message_content = True
    milosClient = discord.Client(intents=milosIntents)
    client_events(milosClient)
    milosClient.run(TOKEN)
# --------------------------------------------------------------------- #
