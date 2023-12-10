# --- send_message.py ------------------------------------------------- #
# --------------------------------------------------------------------- #
# Date   :	02/12/2023                                                  #
# Author :	Robin Reggiani                                              #
# --------------------------------------------------------------------- #

# --- Imports --------------------------------------------------------- #
import discord
import milosbot.functions.handle_responses as responses_task
import main
# --------------------------------------------------------------------- #


# --- Data structures ------------------------------------------------- #
# --------------------------------------------------------------------- #

# --- Variables ------------------------------------------------------- #
# --------------------------------------------------------------------- #

# --- Methods & Functions --------------------------------------------- #
async def send_message(message, user_message):
    author = message.author
    try:
        res = responses_task.handle_response(user_message)
        if res is None:
            return
        if not res.isEmbed:
            await message.channel.send(res.description, file=res.imgfile)
            main.reload_files()
        else:
            emb = discord.Embed(title=res.title,
                                description=res.description,
                                type=res.type,
                                colour=res.color)
            if res.image is not None:
                emb.set_image(url=res.image)
            if res.thumbnail is not None:
                emb.set_thumbnail(url=res.thumbnail)
            emb.set_author(name=author, icon_url=author.avatar)
            await message.channel.send(embed=emb)
    except Exception as e:
        print(e)


async def send_intro(message):
    try:
        emb = discord.Embed(title=main.milos_setup['mention_title'],
                            description=main.milos_setup['mention_description'],
                            type='rich',
                            colour=int(main.milos_setup['embed_color'], 16))
        emb.set_author(name=message.author, icon_url=message.author.avatar)
        emb.set_image(url=main.milos_setup['mention_image'])
        emb.set_thumbnail(url=main.milos_setup['mention_thumbnail'])
        emb.set_footer(text=main.milos_setup['mention_footer_text'],
                       icon_url=main.milos_setup['mention_footer_icon'])
        await message.channel.send(embed=emb)
    except Exception as e:
        print(e)
# --------------------------------------------------------------------- #
