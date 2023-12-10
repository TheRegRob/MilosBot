# --- milos.py --------------------------------------------------------- #
# --------------------------------------------------------------------- #
# Date   :	02/12/2023                                                  #
# Author :	Robin Reggiani                                              #
# --------------------------------------------------------------------- #

# --- Imports --------------------------------------------------------- #
import discord
from discord import Intents
from discord.ext import commands

import main
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
        try:
            sync = await milos_bot.tree.sync()

            print(f"Sync {len(sync)} commands(s)")
        except Exception as ex:
            print(ex)

    @milos_bot.event
    async def on_message(message):
        if (message.author == milos_bot.user or
                str(message.content).startswith("http")):
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f"{username} said '{user_message}' ({channel})")
        # -------- Krone's part ----------------------------------------
        ctx = await milos_bot.get_context(message)
        is_mention = False
        if milos_bot.user.mentioned_in(message) and message.mention_everyone is False:
            if message.reference is None:
                is_mention = True
            else:
                reply_msg = await ctx.channel.fetch_message(message.reference.message_id)
                if reply_msg.author != milos_bot.user:
                    is_mention = True
        # --------------------------------------------------------------
        if is_mention:
            await sending_task.send_intro(message)
        else:
            await sending_task.send_message(message, user_message)
# --------------------------------------------------------------------- #


# --- Methods & Functions --------------------------------------------- #
def milos_run():
    global milosIntents
    global milosCommands
    milosIntents = discord.Intents.default()
    milosIntents.message_content = True
    milos_bot = commands.Bot(command_prefix=str(commands.when_mentioned_or("/")),
                             intents=milosIntents,
                             allowed_mention=discord.AllowedMentions(everyone=True))
    milosCommands = milos_commands.MilosCommands(reference_event=milos_bot)
    client_events(milos_bot)
    milos_bot.run(TOKEN)
# --------------------------------------------------------------------- #
