import os, nextcord, datetime
from nextcord.ext import commands


class TicketController(nextcord.ui.View):
    def __init__(self):
        super().__init__()

    @nextcord.ui.button(style=nextcord.ButtonStyle.green, emoji="⛏️")
    async def button_callback_a(self, button: nextcord.Button, interaction: nextcord.Interaction):
        embed = nextcord.Embed(color=nextcord.Color.orange())
        embed.set_author(name="Danker Instant Help", icon_url=f"{interaction.client.user.display_avatar}")
        embed.add_field(name="⛏️ - Server Updation Support", value="Please keep noticing <#852069972171161651> channel")
        embed.set_footer(text=f"Danker Sale Items Support ➤ Command ran by: {interaction.user.name}", icon_url =f"{interaction.client.user.display_avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.channel.set_permissions(interaction.user,send_messages=False,read_messages=True)

    @nextcord.ui.button(style=nextcord.ButtonStyle.green, emoji="⚔️")
    async def button_callback_b(self, button: nextcord.Button, interaction: nextcord.Interaction):
        embed = nextcord.Embed(color=nextcord.Color.orange())
        embed.set_author(name="Danker Instant Help", icon_url=f"{interaction.client.user.display_avatar}")
        embed.add_field(name="⚔️ - Confliction Support", value="Please write the name or id of the member who is annoying you with proof in this channel.")
        embed.set_footer(text=f"Danker Sale Items Support ➤ Command ran by: {interaction.user.name}", icon_url =f"{interaction.client.user.display_avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.channel.set_permissions(interaction.user,send_messages=True,read_messages=True)

    @nextcord.ui.button(style=nextcord.ButtonStyle.green, emoji="🎯")
    async def button_callback_c(self, button: nextcord.Button, interaction: nextcord.Interaction):
        embed = nextcord.Embed(color=nextcord.Color.orange())
        embed.set_author(name="Danker Instant Help", icon_url=f"{interaction.client.user.display_avatar}")
        embed.add_field(name="🎯 - BOTS Support", value="For bot support you have to write the prefix of the bot and then you have to write help after that(`<bot prefix>help`).All the prefixes can be found in <#843774911206260736> channel.")
        embed.set_footer(text=f"Danker Sale Items Support ➤ Command ran by: {interaction.user.name}", icon_url =f"{interaction.client.user.display_avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.channel.set_permissions(interaction.user,send_messages=False,read_messages=True)

    @nextcord.ui.button(style=nextcord.ButtonStyle.green, emoji="🎁")
    async def button_callback_d(self, button: nextcord.Button, interaction: nextcord.Interaction):
        embed = nextcord.Embed(color=nextcord.Color.orange())
        embed.set_author(name="Danker Instant Help", icon_url=f"{interaction.client.user.display_avatar}")
        embed.add_field(name="🎁 - Rank Support", value="Please type `!rank` or use slash command `/rank (MEE6 BOT)` in the <#843774911206260736> channel to know your rank.")
        embed.set_footer(text=f"Danker Sale Items Support ➤ Command ran by: {interaction.user.name}", icon_url =f"{interaction.client.user.display_avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.channel.set_permissions(interaction.user,send_messages=False,read_messages=True)

    @nextcord.ui.button(style=nextcord.ButtonStyle.green, emoji="📋")
    async def button_callback_f(self, button: nextcord.Button, interaction: nextcord.Interaction):
        embed = nextcord.Embed(color=nextcord.Color.orange())
        embed.set_author(name="Danker Instant Help", icon_url=f"{interaction.client.user.display_avatar}")
        embed.add_field(name="📋 - Punishment Appeal", value="Please write the name or id of the member in this channel whom did you want to punish. Also share a valid reason with proof.")
        embed.set_footer(text=f"Danker Sale Items Support ➤ Command ran by: {interaction.user.name}", icon_url =f"{interaction.client.user.display_avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.channel.set_permissions(interaction.user,send_messages=True,read_messages=True)       

    @nextcord.ui.button(style=nextcord.ButtonStyle.green, emoji="🎫")
    async def button_callback_g(self, button: nextcord.Button, interaction: nextcord.Interaction):
        embed = nextcord.Embed(color=nextcord.Color.orange())
        embed.set_author(name="Danker Instant Help", icon_url=f"{interaction.client.user.display_avatar}")
        embed.add_field(name="🎫 - Discord Support", value="If you don't know how to use this app then go to <#844996204844810240> channel and watch the videos provied on that channel.")
        embed.set_footer(text=f"Danker Sale Items Support ➤ Command ran by: {interaction.user.name}", icon_url =f"{interaction.client.user.display_avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.channel.set_permissions(interaction.user,send_messages=False,read_messages=True) 

    @nextcord.ui.button(style=nextcord.ButtonStyle.green, emoji="⚙️")
    async def button_callback_h(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"{interaction.user.mention} What is the problem? Tell Us in this channel.", ephemeral=True)
        await interaction.channel.set_permissions(interaction.user,send_messages=True,read_messages=True)    

    @nextcord.ui.button(style=nextcord.ButtonStyle.green, emoji="🔒")
    async def button_callback_i(self, button: nextcord.Button, interaction: nextcord.Interaction):
        lock = nextcord.Embed(color=nextcord.Color.orange())
        lock.set_author(name="Danker Ticket Claimed", icon_url=f"{interaction.client.user.display_avatar}")
        lock.add_field(name="Ticket has been Locked",value=":lock: Ticket has been locked. Do you want to delete then react with ✔ ")
        lock.set_footer(text=f"Danker Sale Items Support ➤ Command ran by: {interaction.user.name}", icon_url =f"{interaction.client.user.display_avatar}")
        await interaction.response.send_message(embed=lock, ephemeral=True) 
        await interaction.channel.set_permissions(interaction.user,send_messages=False,read_messages=True)
        await interaction.channel.edit(name=f"📥・ticket-{interaction.user.names}-claimed" )

    @nextcord.ui.button(style=nextcord.ButtonStyle.green, emoji="⛔")
    async def channel_delete_and_user_send_callback(self, button: nextcord.Button, interaction: nextcord.Interaction):
        dt_obj= datetime.datetime.utcnow().date()
        await interaction.channel.delete(reason="As per user's request we have deleted.")
        embed = nextcord.Embed(color=nextcord.Color.orange())
        embed.set_author(name="DANKER SALE ITEMS SUPPORT", url="https://dankersaleitems.herokuapp.com",icon_url=f"{interaction.client.user.display_avatar}")
        embed.add_field(name=":notepad_spiral: DANKER SALE ITEMS Ticket Closed", value="Thanks for reaching out to our support team, we hope your issue was solved.")
        embed.add_field(name="‏‏‎ ‎", value="Feel free to create a new ticket using `!mticket` command or `/ticket` slash command.", inline=False)
        embed.set_footer(text = f"Deleted on: {dt_obj}" , )
        await interaction.user.send(f"{interaction.user.mention} Ticket successfully deleted.")
        await interaction.user.send(embed=embed)





class TicketCreator(nextcord.ui.View):
    def __init__(self):
        super().__init__()

    @nextcord.ui.button(label="Create Ticket", style=nextcord.ButtonStyle.green, emoji="📩")
    async def create_ticket(self, button: nextcord.Button, interaction: nextcord.Interaction):
        category= nextcord.utils.get(interaction.guild.categories,  name="Help / Support ▶")
        channel = await interaction.guild.create_text_channel(name=f"📥・ticket {interaction.user.name}", category=category)
        embed = nextcord.Embed(color=nextcord.Color.orange())
        embed.set_author(name="DANK TICKET", icon_url=f"{interaction.client.user.display_avatar}")
        embed.add_field(name="WELCOME TO 🎫 TICKET", value="Hey, welcome to <a:pepe_crymusic:877458357655568384> 💡Danker Sale Items! The easiest way to get updated about Dank Memer if you got banned from there server.Here you can enjoy the server by 🎮 playing games, playing with dank memer, <:triviabot:738337421141475388> joining trivias and much more.")
        embed.add_field(name=" ‎", value="1) ⛏️ - Server Updation Support", inline=False)
        embed.add_field(name="‏‏‎ ‎", value="2) ⚔️ - Confliction Support", inline=False)
        embed.add_field(name="‏‏‎ ‎", value="3) 🎯 - Games and BOTS Support",inline=False)
        embed.add_field(name="‏‏‎ ‎", value="4) 🎁 - Rank Support",inline=False)
        embed.add_field(name="‏‏‎ ‎", value="5) 📋 - Punishment Appeal",inline=False)
        embed.add_field(name="‏‏‎ ‎", value="6) 🎫 - Discord Support",inline=False)
        embed.add_field(name="‏‏‎ ‎", value="7) ⚙️ - Other Support",inline=False)
        embed.add_field(name="‏‏‎ ‎", value="<:pepetension:877458283005358080> Dank Memer.React with ⛔ emoji to close the ticket.",inline=False)
        embed.add_field(name="‏‏‎ ‎", value="<:pepetension:877458283005358080> Dank Memer.React with 🔒 emoji to claim or lock the ticket.",inline=False)
        embed.set_footer(text=f"Danker Sale Items Support ➤ Command ran by: {interaction.user.name}", icon_url =f"{interaction.client.user.display_avatar}")
        await channel.send(f"{interaction.user.mention} Thanks for creating a ticket 📩", embed=embed, view=TicketController())
        await channel.set_permissions(interaction.user,send_messages=True,read_messages=True) 
        await interaction.message.delete()

    @nextcord.ui.button(style=nextcord.ButtonStyle.secondary,emoji="<:dustbin:949602736633167882>")
    async def on_stop(self, button, interaction: nextcord.Interaction):
        await interaction.message.delete()

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
 

    @commands.command(name="ticket", description="Creates a ticket for you.")
    async def ticket(self, ctx):
        view = TicketCreator()        
        embed= nextcord.Embed(color=nextcord.Color.red())
        embed.set_author(name="DANK TICKET", icon_url=f"{self.bot.user.display_avatar}")
        embed.add_field(name=":safety_vest: WELCOME TO HELP CENTER", value="Hello @everyone Welcome to ticket center. Do you need help?",inline=False)
        embed.add_field(name="Help", value="Just create a ticket by reacting with 📩 this emoji")
        embed.set_thumbnail(url=f"{self.bot.user.display_avatar}")
        embed.set_footer(text="Danker Sale Items Support ➤ Command ran by: {}".format(ctx.author.display_name), icon_url =f"{self.bot.user.display_avatar}")
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed, view=view)

    @nextcord.slash_command(name="ticket", description="Creates a ticket for you.")
    async def ticket(self, interaction: nextcord.Interaction):
        view = TicketCreator()        
        embed= nextcord.Embed(color=nextcord.Color.red())
        embed.set_author(name="DANK TICKET", icon_url=f"{self.bot.user.display_avatar}")
        embed.add_field(name=":safety_vest: WELCOME TO HELP CENTER", value="Hello @everyone Welcome to ticket center. Do you need help?",inline=False)
        embed.add_field(name="Help", value="Just create a ticket by reacting with 📩 this emoji")
        embed.set_thumbnail(url=f"{self.bot.user.display_avatar}")
        embed.set_footer(text="Danker Sale Items Support ➤ Command ran by: {}".format(interaction.user.display_name), icon_url =f"{self.bot.user.display_avatar}")
        await interaction.response.send_message(embed=embed, view=view)

def setup(bot):
    bot.add_cog(Ticket(bot))
