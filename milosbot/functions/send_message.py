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
            emb.set_image(url=res.image)
            emb.set_thumbnail(url=res.thumbnail)
            await message.channel.send(embed=emb, file=[res.imgfile, res.thumbfile])
    except Exception as e:
        print(e)
# --------------------------------------------------------------------- #
