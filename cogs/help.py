from typing import List, Tuple

import nextcord
from nextcord.ext import commands, menus


class HelpPageSource(menus.ListPageSource):
    """Page source for dividing the list of tuples into pages and displaying them in embeds"""

    def __init__(self, help_command: "NewHelpCommand", data: List[Tuple[str, str]]):
        self._help_command = help_command
        # you can set here how many items to display per page
        super().__init__(data, per_page=2)

    async def format_page(self, menu: menus.ButtonMenuPages, entries: List[Tuple[str, str]]):
        """
        Returns an embed containing the entries for the current page
        """
        prefix = self._help_command.context.clean_prefix
        invoked_with = self._help_command.invoked_with
        # create embed
        embed = nextcord.Embed(title="OpenSourceGames Utility Bot Commands", colour=self._help_command.COLOUR)
        embed.set_author(
            name="Utility Bot", icon_url="https://cdn.discordapp.com/avatars/932265924541681727/b5b498a84d5f8783d732b7b63aa4fe69.png?size=128")
        embed.description = (
            f'Use `{prefix}{invoked_with} command` for more info on a command.\n'
            f'Use `{prefix}{invoked_with} category` for more info on a category.'
        )
        # add the entries to the embed
        for entry in entries:
            embed.add_field(name=entry[0], value=entry[1], inline=False)
        # set the footer to display the page number
        embed.set_footer(text=f'Page {menu.current_page + 1}/{self.get_max_pages()}')
        return embed


class HelpButtonMenuPages(menus.ButtonMenuPages):
    """Subclass of ButtonMenuPages to add an interaction_check"""

    def __init__(self, ctx: commands.Context, **kwargs):
        super().__init__(**kwargs)
        self._ctx = ctx

    async def interaction_check(self, interaction: nextcord.Interaction) -> bool:
        """Ensure that the user of the button is the one who called the help command"""
        return self._ctx.author == interaction.user


class NewHelpCommand(commands.MinimalHelpCommand):
    """Custom help command override using embeds and button pagination"""

    # embed colour
    COLOUR = nextcord.Colour.blurple()

    def get_command_signature(self, command: commands.core.Command):
        """Retrieves the signature portion of the help page."""
        return f"{self.context.clean_prefix}{command.qualified_name} {command.signature}"

    async def send_bot_help(self, mapping: dict):
        """implements bot command help page"""
        prefix = self.context.clean_prefix
        invoked_with = self.invoked_with
        embed = nextcord.Embed(title="OpenSourceGames Utility Bot Commands", colour=self.COLOUR)
        embed.set_author(
            name="OpenSourceGames Utility", icon_url="https://cdn.discordapp.com/avatars/932265924541681727/b5b498a84d5f8783d732b7b63aa4fe69.png?size=128")
        embed.description = (
            f'Use `{prefix}{invoked_with} command`  for more info on a command.\n'
            f'Use `{prefix}{invoked_with} category`  for more info on a category.'
        )

        # create a list of tuples for the page source
        embed_fields = []
        for cog, commands in mapping.items():
            name = "No Category" if cog is None else cog.qualified_name
            filtered = await self.filter_commands(commands, sort=True)
            if filtered:
                # \u2002 = en space
                value = "\u2002".join(f"`{prefix}{c.name}`" for c in filtered)
                if cog and cog.description:
                    value = f"{cog.description}\n{value}"
                # add (name, value) pair to the list of fields
                embed_fields.append((name, value))

        # create a pagination menu that paginates the fields
        pages = HelpButtonMenuPages(
            ctx=self.context,
            source=HelpPageSource(self, embed_fields),
            delete_message_after=True
        )
        await pages.start(self.context)

    async def send_cog_help(self, cog: commands.Cog):
        """implements cog help page"""
        embed = nextcord.Embed(
            title=f"{cog.qualified_name} Commands",
            colour=self.COLOUR,
        )
        embed.set_author(
            name="OpenSourceGames Utility", icon_url="https://cdn.discordapp.com/avatars/932265924541681727/b5b498a84d5f8783d732b7b63aa4fe69.png?size=128")
        if cog.description:
            embed.description = cog.description

        filtered = await self.filter_commands(cog.get_commands(), sort=True)
        for command in filtered:
            embed.add_field(
                name=self.get_command_signature(command),
                value=command.description or "...",
                inline=False,
            )
        embed.set_footer(
            text=f"Use {self.context.clean_prefix}help [command] for more info on a command."
        )
        await self.get_destination().send(embed=embed)

    async def send_group_help(self, group: commands.Group):
        """implements group help help page"""
        embed = nextcord.Embed(title=group.qualified_name, colour=self.COLOUR)
        embed.set_author(
            name="OpenSourceGames Utility", icon_url="https://cdn.discordapp.com/avatars/932265924541681727/b5b498a84d5f8783d732b7b63aa4fe69.png?size=128")
        if group.help:
            embed.description = group.help

        if isinstance(group, commands.Group):
            filtered = await self.filter_commands(group.commands, sort=True)
            for command in filtered:
                embed.add_field(
                    name=self.get_command_signature(command),
                    value=command.description or "...",
                    inline=False,
                )

        await self.get_destination().send(embed=embed)

    # Use the same function as group help for command help
    async def send_command_help(self, command: commands.command):
        """implements group help page and command help page"""
        embed = nextcord.Embed(title=f"{command.qualified_name}", description=f"{command.description}", colour=self.COLOUR)
        embed.set_author(name="OpenSourceGames Utility", icon_url="https://cdn.discordapp.com/avatars/932265924541681727/b5b498a84d5f8783d732b7b63aa4fe69.png?size=128")
        embed.add_field(name="Format of the command", value=f"`{self.context.clean_prefix}{command.qualified_name} {command.signature}`")
        embed.set_footer(text=f"OpenSourceGames Utility ▶️ {command.qualified_name}", icon_url="https://cdn.discordapp.com/avatars/932265924541681727/b5b498a84d5f8783d732b7b63aa4fe69.png?size=128") 

        await self.get_destination().send(embed=embed)    




class Help(commands.Cog, name="Help"):
    """Displays help information for commands and cogs"""

    def __init__(self, bot: commands.Bot):
        self.__bot = bot
        self.__original_help_command = bot.help_command
        bot.help_command = NewHelpCommand()
        bot.help_command.cog = self

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----") 

    def cog_unload(self):
        self.__bot.help_command = self.__original_help_command





def setup(bot):
    bot.add_cog(Help(bot))