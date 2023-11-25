import discord
import responses


async def send_message(message, user_message):
    try:
        res = responses.handle_response(user_message)
        if not res.isEmbed:
            await message.channel.send(res.description)
        else:
            emb = discord.Embed(title=res.title,
                                description=res.description,
                                type=res.type,
                                colour=res.color)
            emb.set_image(url=res.image)
            emb.set_thumbnail(url=res.thumbnail)
            await message.channel.send(embed=emb)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'OTA4NzI1NjQ0MDM1MjQ0MDMz.GuUfB3.nKJxlHz0ihMpdZxliVDouhdkb8h_PEm7d6o9XQ'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said '{user_message}' ({channel})")

        await send_message(message, user_message)

    client.run(TOKEN)
