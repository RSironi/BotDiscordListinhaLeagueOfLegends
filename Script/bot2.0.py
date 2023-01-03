from discord.ext import commands
import discord
import config as cf
import listinha

BOT_TOKEN = cf.BOT_TOKEN

bot = commands.Bot(command_prefix="!!", intents=discord.Intents.all())

@bot.command()
async def addListinha(ctx, userid: discord.User, champname: str):
    try:
        listinha.add(userid.id, champname)
        await ctx.send("listinha:man_mage:Atualizada:man_mage:")
    except Exception as e:
        print(e)
        await ctx.send("verifique o parâmetro inserido :woman_mage:")
@bot.command()
async def delListinha(ctx, userid: discord.User, champname: str):
    try:
        listinha.delete(userid.id, champname)
        await ctx.send("listinha:man_mage:Atualizada:man_mage:")
    except Exception as e:
        print(e)
        await ctx.send("verifique o parâmetro inserido :woman_mage:")
@bot.command()
async def Listinha(ctx, userid: discord.User):
    try:
        result = listinha.select(userid.id, userid.name)
        await ctx.send(result)
    except Exception as e:
        print(e)
        await ctx.send("verifique o parâmetro inserido :woman_mage:")


@bot.event  # Exceptions
async def on_command_error(ctx, error: discord.DiscordException):
    if isinstance(error, commands.UserNotFound):
        await ctx.send("Usuário não encontrado")
    elif isinstance(error, commands.MissingRequiredArgument): 
        await ctx.send("Falta parâmetros do comando")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Comando não encontrado")
    else:
        raise error

bot.run(BOT_TOKEN)
