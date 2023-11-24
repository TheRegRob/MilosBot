import discord
import responses

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{username} said: "{user_message}" ({channel})')

    if "gogo" in message.content:
        await message.channel.send("https://tenor.com/view/flex-air-flex-air5-ricardo-bongo-cat-bathtub-gif-19565157")


client.run('OTA4NzI1NjQ0MDM1MjQ0MDMz.GuUfB3.nKJxlHz0ihMpdZxliVDouhdkb8h_PEm7d6o9XQ')
