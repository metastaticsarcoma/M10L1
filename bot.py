import discord
from discord.ext import commands
from discord import app_commands
import random 

import Paginator
PreviousButton = discord.ui.Button(label="◀", style=discord.ButtonStyle.danger)
NextButton =  discord.ui.Button(label="▶", style=discord.ButtonStyle.danger)
PageCounterStyle = discord.ButtonStyle.grey
InitialPage = 0 
timeout = 60 # funcion del paginador 

from Messages import ComandoAyudaEmbed
from Messages import BotonComandosEmbed
from Messages import Secondarytemplate
from Messages import OrigenComandosEmbed
from Messages import GoalsComandosEmbed
from Messages import EcotipD

from Back import ComandoAyuda
from Back import ComandoEcotip
from Back import ComandoGoals


intents = discord.Intents.default( )
intents.message_content = True  
bot = commands.Bot(command_prefix="9", intents=intents, case_insensitive=True)


ComandoAyudaEmbed = discord.Embed.from_dict(ComandoAyudaEmbed)
BotonComandosEmbed = discord.Embed.from_dict(BotonComandosEmbed)
OrigenComandosEmbed = discord.Embed.from_dict(OrigenComandosEmbed)
GoalsComandosEmbed = discord.Embed.from_dict(GoalsComandosEmbed)
@bot.command()
async def Ayuda(ctx):
    await ctx.send(embed=ComandoAyudaEmbed, view=ComandoAyuda())


from Messages import Oembeds
@bot.command()
async def Origen(ctx):
    await Paginator.Simple(
    PreviousButton=PreviousButton,
    NextButton=NextButton,
    PageCounterStyle=PageCounterStyle,
    InitialPage=InitialPage,
    timeout=timeout).start(ctx, pages=Oembeds)


from Messages import Gembed
@bot.command()
async def Gravedad(ctx):
    await Paginator.Simple(
    PreviousButton=PreviousButton,
    NextButton=NextButton,
    PageCounterStyle=PageCounterStyle,
    InitialPage=InitialPage,
    timeout=timeout).start(ctx, pages=Gembed)

@bot.command()
async def Ecotip(ctx):
    await ctx.send(random.choice(EcotipD), view=ComandoEcotip())

@bot.command()
async def Goals(ctx):
    await ctx.send(embed=GoalsComandosEmbed, view=ComandoGoals())


bot.run("")
