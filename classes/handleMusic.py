# --- handleMusic.py ------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# Date          : 07/12/2023                                                                                           #
# Last edit     : 11/12/2023                                                                                           #
# Author(s)     : krone                                                                                                #
# Description   : class to manage YouTube reproduction on Discord's voice channels                                     #
# -------------------------------------------------------------------------------------------------------------------- #


# --- Imports -------------------------------------------------------------------------------------------------------- #
# Discord API wrapper ------------------------------------------------------------------------------------------------ #
import discord
from discord.ext import commands
# YouTube libraries -------------------------------------------------------------------------------------------------- #
from yt_dlp import YoutubeDL
# Python libraries --------------------------------------------------------------------------------------------------- #
import asyncio
import json
# Project constants -------------------------------------------------------------------------------------------------- #

YTDL_OPTIONS = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

FFMPEG_OPTIONS = {
    'options': '-vn'
}
# --- Class | YTDLSource --------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
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
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, FFMPEG_OPTIONS), data=data)


# --- Class | HandleMusic -------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
class HandleMusic():
    # Variables ------------------------------------------------------------------------------------------------------ #
    config: json
    cmd: json
    is_playing: bool
    is_paused: bool
    ytdl: YoutubeDL

    # Init: pass a py json object as config -------------------------------------------------------------------------- #
    def __init__(self):
        #self.config = config
        #self.cmd = cmd
        self.is_playing = False
        self.is_paused = False

        self.YDL_OPTIONS = {'format': 'bestaudio/best'}
        self.FFMPEG_OPTIONS = {'options': '-vn'}

        self.vc = None
        self.ytdl = YoutubeDL(self.YDL_OPTIONS)

    async def play_music(self, voice_channel, url: str):
        # try to connect to voice channel if you are not already connected
        if self.vc is None or not self.vc.is_connected():
            self.vc = await voice_channel.connect()
            # in case we fail to connect
            if self.vc is None:
                return 'Could not connect to the voice channel', 1
        self.is_playing = True
        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: self.ytdl.extract_info(url, download=False))
        song = data['url']
        self.vc.play(discord.FFmpegPCMAudio(song, **self.FFMPEG_OPTIONS))

    async def play_local(self, voice_channel, file_path: str):
        # try to connect to voice channel if you are not already connected
        if self.vc is None or not self.vc.is_connected():
            self.vc = await voice_channel.connect()
            # in case we fail to connect
            if self.vc is None:
                return 'Could not connect to the voice channel', 1
        self.is_playing = True
        self.vc.play(discord.FFmpegPCMAudio(file_path, **self.FFMPEG_OPTIONS))

    async def play(self, interaction: discord.Interaction, url: str):
        try:
            voice_channel = interaction.user.voice.channel
        except:
            return 'You need to connect to a voice channel first!', 1
        if self.is_paused:
            self.vc.resume()
        else:
            if self.is_playing:
                await self.vc.disconnect()
            if url.startswith("https"):
                return await self.play_music(voice_channel, url)
            else:
                return await self.play_local(voice_channel, file_path=url)

    async def pause(self):
        if self.is_playing:
            self.is_playing = False
            self.is_paused = True
            self.vc.pause()

    async def resume(self):
        if self.is_paused:
            self.is_paused = False
            self.is_playing = True
            self.vc.resume()
# -------------------------------------------------------------------------------------------------------------------- #
# --- End of file ---------------------------------------------------------------------------------------------------- #
