import discord
from discord.ext import commands
import random
from Messages import EcotipD
intents = discord.Intents.default( )
intents.message_content = True  
bot = commands.Bot(command_prefix="9", intents=intents, case_insensitive=True)

from Messages import BotonComandosEmbed
BotonComandosEmbed = discord.Embed.from_dict(BotonComandosEmbed)

class ComandoAyuda(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(discord.ui.Button(label="Github", url="https://github.com/metastaticsarcoma/M10L1", style=discord.ButtonStyle.link))

    @discord.ui.button(label="Comandos", style=discord.ButtonStyle.red)
    async def info_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(embed=BotonComandosEmbed, ephemeral=True)

class ComandoEstadistica(discord.ui.View):
    @discord.ui.button(label="Comandos", style=discord.ButtonStyle.red)
    async def info_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(embed=BotonComandosEmbed, ephemeral=True)

class ComandoEcotip(discord.ui.View):
   def __init__(self):
        super().__init__()
        self.add_item(discord.ui.Button(label="Leer mas Ecotips online", url="https://www.greenpeace.org/mexico/participa/tips-y-guias/", style=discord.ButtonStyle.link))

   @discord.ui.button(label="Ecotip random", style=discord.ButtonStyle.red)
   async def info_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(random.choice(EcotipD), view=ComandoEcotip())

def paginatorFunction():
    PreviousButton = discord.ui.Button(label="◀", style=discord.ButtonStyle.danger)
    NextButton =  discord.ui.Button(label="▶", style=discord.ButtonStyle.danger)
    PageCounterStyle = discord.ButtonStyle.grey
    InitialPage = 0 
    timeout = 60 

class ComandoGoals(discord.ui.View):
       def __init__(self):
        super().__init__()
        self.add_item(discord.ui.Button(label="Leer 'accion climatica'", url="https://www.un.org/sustainabledevelopment/climate-change/", style=discord.ButtonStyle.link))
