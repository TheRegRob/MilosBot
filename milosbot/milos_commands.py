# --- milos_commands.py ----------------------------------------------------- #
# --------------------------------------------------------------------- #
# Date   :	02/12/2023                                                  #
# Author :	Robin Reggiani                                              #
# --------------------------------------------------------------------- #

# --- Imports --------------------------------------------------------- #
import discord
import json
from discord.ext import commands
import main
import milosbot.functions.send_message as sending_task


def get_json_pars(cmd: str) -> [str, str]:
    return [main.cmds[cmd]['NAME'], main.cmds[cmd]['DESC']]


class MilosCommands:
    cmd_enjoy: str
    cmd_enrage: str
    cmd_holdon: str

    def __init__(self, reference_event):
        self.bot_events: commands.Bot = reference_event
        self.cmd_enjoy = "enjoy"
        self.cmd_enrage = "enrage"
        self.cmd_holdon = "hold_on"
        self.add_commands()

    def add_commands(self):
        enjoy_json = get_json_pars(self.cmd_enjoy)
        enrage_json = get_json_pars(self.cmd_enrage)
        holdon_json = get_json_pars(self.cmd_holdon)

        @self.bot_events.tree.command(name=enjoy_json[0], description=enjoy_json[1])
        async def cmd_enjoy(interaction: discord.Interaction):
            await sending_task.send_message(interaction, "")

        @self.bot_events.tree.command(name=enrage_json[0], description=enrage_json[1])
        async def cmd_enrage(interaction: discord.Interaction):
            await sending_task.send_message(interaction, "")

        @self.bot_events.tree.command(name=holdon_json[0], description=holdon_json[1])
        async def cmd_holdon(interaction: discord.Interaction):
            await sending_task.send_message(interaction, "")
