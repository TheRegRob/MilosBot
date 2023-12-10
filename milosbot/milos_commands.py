# --- milos_commands.py ----------------------------------------------------- #
# --------------------------------------------------------------------- #
# Date   :	02/12/2023                                                  #
# Author :	Robin Reggiani                                              #
# --------------------------------------------------------------------- #
import os
import random

# --- Imports --------------------------------------------------------- #
import discord
import json

from discord.ext import commands
import main
import milosbot.functions.send_message as sending_task

NAME = 0
DESC = 1
RES_FOLD = 2
ARGS = 3


def get_json_pars(cmd: str) -> [str, str, list, list]:
    return [main.cmds[cmd]['NAME'], main.cmds[cmd]['DESC'], main.cmds[cmd]['RES_FOLD'], main.cmds[cmd]['ARGS']]


class MilosCommands:
    cmd_gachiscream: str
    cmd_gachigasm: str
    cmd_gachiquotes: str

    def __init__(self, reference_event):
        self.bot_events: commands.Bot = reference_event
        self.cmd_gachiscream = "gachi_scream"
        self.cmd_gachigasm = "gachi_gasm"
        self.cmd_gachiquotes = "gachi_quotes"
        self.add_commands()

    def add_commands(self):
        gachiscream_json = get_json_pars(self.cmd_gachiscream)
        gachigasm_json = get_json_pars(self.cmd_gachigasm)
        gachiquotes_json = get_json_pars(self.cmd_gachiquotes)

        @self.bot_events.tree.command(name=gachiscream_json[NAME], description=gachiscream_json[DESC])
        async def cmd_gachiscream(interaction: discord.Interaction):
            files_lst = os.listdir(gachiscream_json[RES_FOLD])
            idx = 0 if len(files_lst) == 0 else random.randint(0, len(files_lst) - 1)
            sounds_file = discord.File(gachiscream_json[RES_FOLD] + files_lst[idx])
            await interaction.response.send_message("", file=sounds_file)  # noqa

        @self.bot_events.tree.command(name=gachigasm_json[NAME], description=gachigasm_json[DESC])
        async def cmd_gachigasm(interaction: discord.Interaction):
            files_lst = os.listdir(gachigasm_json[RES_FOLD])
            idx = 0 if len(files_lst) == 0 else random.randint(0, len(files_lst) - 1)
            sounds_file = discord.File(gachigasm_json[RES_FOLD] + files_lst[idx])
            await interaction.response.send_message("", file=sounds_file)  # noqa

        @self.bot_events.tree.command(name=gachiquotes_json[NAME], description=gachiquotes_json[DESC])
        async def cmd_gachiquotes(interaction: discord.Interaction):
            files_lst = os.listdir(gachiquotes_json[RES_FOLD])
            idx = 0 if len(files_lst) == 0 else random.randint(0, len(files_lst) - 1)
            sounds_file = discord.File(gachiquotes_json[RES_FOLD] + files_lst[idx])
            await interaction.response.send_message("", file=sounds_file)  # noqa
