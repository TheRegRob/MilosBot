# --- milos_commands.py ----------------------------------------------------- #
# --------------------------------------------------------------------- #
# Date   :	02/12/2023                                                  #
# Author :	Robin Reggiani                                              #
# --------------------------------------------------------------------- #
import os
import random
import asyncio

# --- Imports --------------------------------------------------------- #
import discord
from discord.ext import commands
import main
import classes.handleMusic as handleMusic

NAME = 0
DESC = 1
RES_FOLD = 2
ARGS = 3


YDL_OPTIONS = {
    'format': 'bestaudio',
    'noplaylist': True
}
FFMPEG_OPTIONS = {
    'options': '-vn'
}


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume= 0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, ytdl, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url=url,
                                                                          download=False,
                                                                          force_generic_extractor=True))
        if 'entries' in data:
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **FFMPEG_OPTIONS), data=data)


def get_json_pars(cmd: str) -> [str, str, list, list]:
    return [main.cmds[cmd]['NAME'], main.cmds[cmd]['DESC'], main.cmds[cmd]['RES_FOLD'], main.cmds[cmd]['ARGS']]


class MilosCommands:
    cmd_gachiscream: str
    cmd_gachigasm: str
    cmd_gachiquote: str
    cmd_vocal_gachiscream: str
    cmd_vocal_gachigasm: str
    cmd_vocal_gachiquote: str
    music_handle: handleMusic.HandleMusic

    def __init__(self, reference_event):
        self.bot_events: commands.Bot = reference_event
        self.cmd_gachiscream = "gachi_scream"
        self.cmd_gachigasm = "gachi_gasm"
        self.cmd_gachiquote = "gachi_quotes"
        self.cmd_vocal_gachiscream = "vocal_gachi_scream"
        self.cmd_vocal_gachigasm = "vocal_gachi_gasm"
        self.cmd_vocal_gachiquote = "vocal_gachi_quote"
        self.add_commands()
        self.music_handle = handleMusic.HandleMusic()

    def add_commands(self):
        gachiscream_json = get_json_pars(self.cmd_gachiscream)
        gachigasm_json = get_json_pars(self.cmd_gachigasm)
        gachiquote_json = get_json_pars(self.cmd_gachiquote)
        vocal_gachiscream_json = get_json_pars(self.cmd_vocal_gachiscream)
        vocal_gachigasm_json = get_json_pars(self.cmd_vocal_gachigasm)
        vocal_gachiquote_json = get_json_pars(self.cmd_vocal_gachiquote)

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

        @self.bot_events.tree.command(name=gachiquote_json[NAME], description=gachiquote_json[DESC])
        async def cmd_gachiquotes(interaction: discord.Interaction):
            files_lst = os.listdir(gachiquote_json[RES_FOLD])
            idx = 0 if len(files_lst) == 0 else random.randint(0, len(files_lst) - 1)
            sounds_file = discord.File(gachiquote_json[RES_FOLD] + files_lst[idx])
            await interaction.response.send_message("", file=sounds_file)  # noqa

        @self.bot_events.tree.command(name=vocal_gachiscream_json[NAME], description=vocal_gachiscream_json[DESC])
        async def cmd_vocal_gachiscream(interaction: discord.Interaction):
            files_lst = os.listdir(vocal_gachiscream_json[RES_FOLD])
            idx = 0 if len(files_lst) == 0 else random.randint(0, len(files_lst) - 1)
            await self.music_handle.play(interaction, vocal_gachiscream_json[RES_FOLD] + files_lst[idx])
            msg = await interaction.response.send_message("Enjoy your gachi scream", ephemeral= True)  # noqa

        @self.bot_events.tree.command(name=vocal_gachigasm_json[NAME], description=vocal_gachigasm_json[DESC])
        async def cmd_vocal_gachigasm(interaction: discord.Interaction):
            files_lst = os.listdir(vocal_gachigasm_json[RES_FOLD])
            idx = 0 if len(files_lst) == 0 else random.randint(0, len(files_lst) - 1)
            await self.music_handle.play(interaction, vocal_gachigasm_json[RES_FOLD] + files_lst[idx])
            msg = await interaction.response.send_message("Enjoy your gachi gasm", ephemeral= True)  # noqa

        @self.bot_events.tree.command(name=vocal_gachiquote_json[NAME], description=vocal_gachiquote_json[DESC])
        async def cmd_vocal_gachiquote(interaction: discord.Interaction):
            files_lst = os.listdir(vocal_gachiquote_json[RES_FOLD])
            idx = 0 if len(files_lst) == 0 else random.randint(0, len(files_lst) - 1)
            await self.music_handle.play(interaction, vocal_gachiquote_json[RES_FOLD] + files_lst[idx])
            msg = await interaction.response.send_message("Enjoy your gachi quote", ephemeral= True)  # noqa
