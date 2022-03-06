import os, json, nextcord, datetime, random
from nextcord.ext import commands


# DropDown View
# SELECT MENUS AND BUTTONS
class DropDown(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(label="Python", description="Python is a user friendly language born from C language."),
            nextcord.SelectOption(label="JavaScript", description="JavaScript is a very popular language can be executed by the browser."),\
            nextcord.SelectOption(label="HTML", description="HTML is mandatory while building websites."),
            nextcord.SelectOption(label="CSS", description="Raw HTML looks bad, so CSS styles and decorates it."),
            nextcord.SelectOption(label="PHP", description="PHP is also a very popular language (used in Wordpress).")
        ]
        super().__init__(placeholder="Select Your Language", min_values=1, max_values=1, options=options)
    async def callback(self, interaction: nextcord.Interaction):
        if self.values[0] == "Python":
             langembed = nextcord.Embed(
               title=f":wave: Hi {interaction.user.name}", description="**You have choosed <:python:935932879714779227> python.**")
           
             langembed.set_author(
        name="OpenSourceGames Utility", icon_url=interaction.client.user.display_avatar, url="https://python.org")   
             langembed.add_field(name="__ABOUT__", value="***Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects***") 
            
             await interaction.response.edit_message(embed=langembed)
                
        if self.values[0] == "JavaScript":
             langembed = nextcord.Embed(
               title=f":wave: Hi {interaction.user.name}", description="**You have choosed <:JS:935933057800757318> javascript.**")
 
             langembed.set_author(
         name="OpenSourceGames Utility", icon_url=interaction.client.user.display_avatar, url="https://javascript.com")   
             langembed.add_field(name="__ABOUT__", value="***JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS. Over 97% of websites use JavaScript on the client side for web page behavior, often incorporating third-party libraries.***") 
             await interaction.response.edit_message(embed=langembed)    
            
        if self.values[0] == "HTML":
             langembed = nextcord.Embed(
               title=f":wave: Hi {interaction.user.name}", description="**You have choosed <:html:935933258439483442> HTML.**")
 
             langembed.set_author(
          name="OpenSourceGames Utility", icon_url=interaction.client.user.display_avatar, url="https://html.com")   
             langembed.add_field(name="__ABOUT__", value="***The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript. ... HTML elements are the building blocks of HTML pages.***") 
             await interaction.response.edit_message(embed=langembed) 
        if self.values[0] == "CSS":
             langembed = nextcord.Embed(
               title=f":wave: Hi {interaction.user.name}", description="**You have choosed <:css:935935867468533830> CSS.**")
 
             langembed.set_author(
          name="OpenSourceGames Utility", icon_url=interaction.client.user.display_avatar, url="https://g.co/kgs/83EKjE")   
             langembed.add_field(name="__ABOUT__", value="***Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML. CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScripts.***") 
             await interaction.response.edit_message(embed=langembed) 
        if self.values[0] == "PHP":
             langembed = nextcord.Embed(
               title=f":wave: Hi {interaction.user.name}", description="**You have choosed <:php:935937346799546408> PHP.**")
 
             langembed.set_author(
        name="OpenSourceGames Utility", icon_url=interaction.client.user.display_avatar, url="https://php.net/")   
             langembed.add_field(name="__ABOUT__", value="***PHP is a general-purpose scripting language geared towards web development. It was originally created by Danish-Canadian programmer Rasmus Lerdorf in 1994. The PHP reference implementation is now produced by The PHP Group.***") 
             await interaction.response.edit_message(embed=langembed) 

class DropDownView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(DropDown())
          
class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")         
        
    # SLASH COMMAND

    # 8ball Slash Command
    @nextcord.slash_command(name="8ball", description="Let the 8 Ball Predict!\nthe future")
    async def eightball(self, interaction: nextcord.Interaction, *, question):
        responses = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            "I'm feeling well",
            'Yes - definitely.',
            'You may rely on it.',
            'As I see it yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',
            'Reply hazy, try again.',
            'Better not tell you now.',
            'Concentrate and ask again.',
            "Don't count on it.",
            'I cannot predict now.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'VEry doubtfull.',
            'I am tired. *proceeds with sleeping*',
            'As I see it, yes.',
            'Yes.',
            'Positive',
            'From my point of view, yes',
            'Convinced.',
            'Most Likley.',
            'Chances High',
            'No.',
            'Negative.',
            'Not Convinced.',
            'Perhaps.',
            'Not Sure',
            'Mayby',
            'Im to lazy to predict.'
        ]
        await interaction.response.send_message(f":8ball: Question: {question}\n:8ball: Answer: {random.choice(responses)}", ephemeral=True)



    # Clear Slash Command
    @nextcord.slash_command(name="clear",description="Clears messages")
    @commands.has_permissions(administrator=True)
    async def clear(self, interaction: nextcord.Interaction, amount: int):
      if amount > 1000 :
          await interaction.response.send_message('Cannot delete more than 1000 messages.', ephemeral=True)
      else:
          new_count = {}
          messages = await interaction.channel.history(limit=amount).flatten()
          for message in messages:
              if str(message.author) in new_count:
                  new_count[str(message.author)] += 1
              else:
                  new_count[str(message.author)] = 1
          messages_deleted = 0          
          for message_deleted in list(new_count.items()):
                messages_deleted += message_deleted
                new_message = f"Successfully cleared `{messages_deleted} messages`"        
          await interaction.channel.purge(limit=amount)
          await interaction.response.send_message(new_message, ephemeral=True)     

    @nextcord.slash_command(name="ping", description="Returns the latency of the bot")
    async def ping(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"Pong! Latency is {self.bot.latency}ms", ephemeral=True)    

    
def setup(bot):
    bot.add_cog(Slash(bot))          
