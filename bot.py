import os, nextcord
from pathlib import Path
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()

activity = nextcord.Activity(type=nextcord.ActivityType.watching,name="Danker Sale Items")
client = commands.Bot(command_prefix="!m", activity=activity,status=nextcord.Status.idle)
client.config_token = os.getenv("BOT_TOKEN")
cwd = Path(__file__).parents[0]
cwd = str(cwd)
@client.event
async def on_ready():
    
    # On ready, print some details to standard out
    print(
        f"-----\nLogged in as: {client.user.name} : {client.user.id}\n-----\nMy current prefix is: t!\n-----"
    )    
    
# A new nextcord view
class DelBtn(nextcord.ui.View):
    def __init__(self):
        super().__init__()

    @nextcord.ui.button(label="Delete", style=nextcord.ButtonStyle.secondary, emoji="<:dustbin:949602736633167882>")  
    async def stop(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.message.delete()   

# Error Handling
@client.event
async def on_command_error(ctx, error):
    view = DelBtn()
    if isinstance(error, commands.CommandNotFound):
        notfounderror = nextcord.Embed(
            title="❌ Error in the Bot", description="😞 Sorry we are facing an error while running this command.", color=0xFF5733)
        notfounderror.set_author(
            name="OpenSourceGames Utility", icon_url=client.user.display_avatar)
        notfounderror.add_field(
            name="Error is described below.", value=f"```py\n {error}\n```")
        notfounderror.add_field(
            name="__**What To do?**__", value="Don't worry we will forward this message to the devs.", inline=False)
        notfounderror.set_footer(
            text=f"Command requested by {ctx.author.name}")
        await ctx.send(embed=notfounderror, view=view)
    if isinstance(error, commands.MissingRequiredArgument):
        notfounderror = nextcord.Embed(
            title="❌ Error in the Bot", description="😞 Sorry we are facing an error while running this command.", color=0xFF5733)
        notfounderror.set_author(
            name="OpenSourceGames Utility", icon_url=client.user.display_avatar)
        notfounderror.add_field(
            name="Error is described below.", value=f"```py\n {error}\n```")
        notfounderror.add_field(
            name="__**What To do?**__", value="Don't worry we will forward this message to the devs.", inline=False)
        notfounderror.set_footer(
            text=f"Command requested by {ctx.author.name}")
        await ctx.send(embed=notfounderror, view=view)
    if isinstance(error, commands.MissingRole):
        notfounderror = nextcord.Embed(
            title="❌ Error in the Bot", description="😞 Sorry we are facing an error while running this command.", color=0xFF5733)
        notfounderror.set_author(
            name="OpenSourceGames Utility", icon_url=client.user.display_avatar)
        notfounderror.add_field(
            name="Error is described below.", value=f"```py\n {error}\n```")
        notfounderror.add_field(
            name="__**What To do?**__", value="Don't worry we will forward this message to the devs.", inline=False)
        notfounderror.set_footer(
            text=f"Command requested by {ctx.author.name}")
        await ctx.send(embed=notfounderror, view=viewr)
    if isinstance(error, commands.MissingPermissions):
        notfounderror = nextcord.Embed(
            title="❌ Error in the Bot", description="😞 Sorry we are facing an error while running this command.", color=0xFF5733)
        notfounderror.set_author(
            name="OpenSourceGames Utility", icon_url=client.user.display_avatar)
        notfounderror.add_field(
            name="Error is described below.", value=f"```py\n {error}\n```")
        notfounderror.add_field(
            name="__**What To do?**__", value="Don't worry we will forward this message to the devs.", inline=False)
        notfounderror.set_footer(
            text=f"Command requested by {ctx.author.name}")
        await ctx.send(embed=notfounderror, view=view)
    if isinstance(error, commands.CommandInvokeError):
        notfounderror = nextcord.Embed(
            title="❌ Error in the Bot", description="😞 Sorry we are facing an error while running this command.", color=0xFF5733)
        notfounderror.set_author(
            name="OpenSourceGames Utility", icon_url=client.user.display_avatar)
        notfounderror.add_field(
            name="Error is described below.", value=f"```py\n {error}\n```")
        notfounderror.add_field(
            name="__**What To do?**__", value="Don't worry we will forward this message to the devs.", inline=False)
        notfounderror.set_footer(
            text=f"Command requested by {ctx.author.name}")
        await ctx.send(embed=notfounderror, view=view)
    if isinstance(error, commands.CommandOnCooldown):
        notfounderror = nextcord.Embed(
            title="❌ Error in the Bot", description="😞 Sorry we are facing an error while running this command.", color=0xFF5733)
        notfounderror.set_author(
            name="OpenSourceGames Utility", icon_url=client.user.display_avatar)
        notfounderror.add_field(
            name="Error is described below.", value=f"```py\n {error}\n```")
        notfounderror.add_field(
            name="__**What To do?**__", value="Don't worry we will forward this message to the devs.", inline=False)
        notfounderror.set_footer(
            text=f"Command requested by {ctx.author.name}")
        await ctx.send(embed=notfounderror, view=view)
    if isinstance(error, commands.ConversionError):
        notfounderror = nextcord.Embed(
            title="❌ Error in the Bot", description="😞 Sorry we are facing an error while running this command.", color=0xFF5733)
        notfounderror.set_author(
            name="OpenSourceGames Utility", icon_url=client.user.display_avatar)
        notfounderror.add_field(
            name="Error is described below.", value=f"```py\n {error}\n```")
        notfounderror.add_field(
            name="__**What To do?**__", value="Don't worry we will forward this message to the devs.", inline=False)
        notfounderror.set_footer(
            text=f"Command requested by {ctx.author.name}")
        await ctx.send(embed=notfounderror, view=view)
    if isinstance(error, commands.UserInputError):
        notfounderror = nextcord.Embed(
            title="❌ Error in the Bot", description="😞 Sorry we are facing an error while running this command.", color=0xFF5733)
        notfounderror.set_author(
            name="OpenSourceGames Utility", icon_url=client.user.display_avatar)
        notfounderror.add_field(
            name="Error is described below.", value=f"```py\n {error}```")
        notfounderror.add_field(
            name="__**What To do?**__", value="Don't worry we will forward this message to the devs.", inline=False)
        notfounderror.set_footer(
            text=f"Command requested by {ctx.author.name}")
        await ctx.send(embed=notfounderror, view=view)
    if isinstance(error, commands.DisabledCommand):
        notfounderror = nextcord.Embed(
            title="❌ Error in the Bot", description="😞 Sorry we are facing an error while running this command.", color=0xFF5733)
        notfounderror.set_author(
            name="OpenSourceGames Utility", icon_url=client.user.display_avatar)
        notfounderror.add_field(
            name="Error is described below.", value=f"```py\n {error}```")
        notfounderror.add_field(
            name="__**What To do?**__", value="Don't worry we will forward this message to the devs.", inline=False)
        notfounderror.set_footer(
            text=f"Command requested by {ctx.author.name}")
        await ctx.send(embed=notfounderror, view=view)


# RUNNING OUR CLIENT
if __name__ == "__main__":
    # When running this file, if it is the 'main' file
    # I.E its not being imported from another python file run this
    for file in os.listdir(cwd + "/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            client.load_extension(f"cogs.{file[:-3]}")

    client.run(client.config_token)
