import discord
from discord.ext import commands
from discord.ui import Button, View, Select

# --- Bot Setup ---
# Replace 'YOUR_BOT_TOKEN' with your actual bot token
YOUR_BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
# Replace 'YOUR_GUILD_ID' with the ID of your Discord server
YOUR_GUILD_ID = YOUR_GUILD_ID_HERE # remove if not using guild-specific sync

GITHUB_PROFILE = "https://github.com/AdityaLF" 
DISCORD_USER = "https://discordapp.com/users/786163564205047839" 
DISCORD_SERVER_INVITE = "https://discord.gg/uDRaNE7M2b" 
SUPPORT_ME_KOFI = "https://ko-fi.com/adityaf" 

intents = discord.Intents.default()
intents.members = True 
intents.presences = True 
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

class MemberInfoView(View):
    """
    A Discord UI View for displaying interactive server member information and help links.
    """
    def __init__(self, guild: discord.Guild):
        super().__init__(timeout=180) 
        self.guild = guild
        self.message = None 

    def get_member_counts(self):
        """Calculates and returns total, online, bot, and human member counts."""
        total_members = self.guild.member_count
        online_members = 0
        bots = 0
        humans = 0

        for member in self.guild.members:
            if member.bot:
                bots += 1
            else:
                humans += 1

            if member.status != discord.Status.offline:
                online_members += 1
        
        return total_members, online_members, bots, humans

    @discord.ui.button(label="📊 Total Members", style=discord.ButtonStyle.primary, custom_id="total_members_button")
    async def total_members_button_callback(self, interaction: discord.Interaction, button: Button):
        """Callback for the 'Total Members' button, sends total member count as an embed."""
        total_members, _, _, _ = self.get_member_counts()

        embed = discord.Embed(
            title="📊 Total Server Members",
            description=f"There are **{total_members}** members in this server.",
            color=discord.Color.blue() 
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="🟢 Online Members", style=discord.ButtonStyle.success, custom_id="online_members_button")
    async def online_members_button_callback(self, interaction: discord.Interaction, button: Button):
        """Callback for the 'Online Members' button, sends online member count as an embed."""
        _, online_members, _, _ = self.get_member_counts()

        embed = discord.Embed(
            title="🟢 Online Members",
            description=f"There are **{online_members}** members currently online (or idle/DND).",
            color=discord.Color.green() 
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="👤 Human Count", style=discord.ButtonStyle.danger, custom_id="human_members_button")
    async def human_members_button_callback(self, interaction: discord.Interaction, button: Button):
        """Callback for the 'Human Members' button, sends human member count as an embed."""
        _, _, _, humans = self.get_member_counts()

        embed = discord.Embed(
            title="👤 Human Member Count",
            description=f"There are **{humans}** human members in this server.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        # --- END ADDITION/MODIFICATION ---

    @discord.ui.button(label="🤖 Bot Count", style=discord.ButtonStyle.secondary, custom_id="bot_count_button")
    async def bot_count_button_callback(self, interaction: discord.Interaction, button: Button):
        """Callback for the 'Bot Count' button, sends bot count as an embed."""
        _, _, bots, _ = self.get_member_counts()

        embed = discord.Embed(
            title="🤖 Bot Count",
            description=f"There are **{bots}** bots in this server.",
            color=discord.Color.light_grey() 
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="📜 Info & Help", style=discord.ButtonStyle.blurple, custom_id="info_help_button")
    async def info_help_button_callback(self, interaction: discord.Interaction, button: Button):
        """
        Callback for the 'Info & Help' button, sends an embed containing
        links to GitHub, Discord user, Discord server, and a support link.
        The embed has a blue color.
        """
        embed = discord.Embed(
            title="✨ Server Information & Help",
            description="Here's some important information and useful links for you:",
            color=discord.Color.blurple()
        )

        embed.add_field(name="🔗 GitHub", value=f"[Visit GitHub Profile]({GITHUB_PROFILE})", inline=False)
        embed.add_field(name="🎮 Discord", value=f"[@05.07am]({DISCORD_USER})", inline=False)
        embed.add_field(name="💬 Discord Server", value=f"[Join Our Server]({DISCORD_SERVER_INVITE})", inline=False)
        embed.add_field(name="❤️ Support Me", value=f"[Buy Me a Coffee]({SUPPORT_ME_KOFI})", inline=False)
        
        embed.set_thumbnail(url=self.guild.icon.url if self.guild.icon else None)

        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.select(
        placeholder="View Member List (by status)...",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label="All Members", value="all", description="Show a list of all members."),
            discord.SelectOption(label="Online Members Only", value="online", description="Show only members who are online."),
            discord.SelectOption(label="Offline Members Only", value="offline", description="Show only members who are offline."),
            discord.SelectOption(label="Humans Only", value="humans", description="Show only human members."),
            discord.SelectOption(label="Bots Only", value="bots", description="Show only bots.")
        ],
        custom_id="member_list_select"
    )
    async def member_list_select_callback(self, interaction: discord.Interaction, select: Select):
        """
        Callback for the member list filter select menu.
        Sends an embed with a filtered list of members.
        """
        selected_filter = select.values[0]
        member_list_details = [] 
        count = 0
        embed_color = discord.Color.default() 

        response_title_map = {
            "all": "All Members List",
            "online": "Online Members List",
            "offline": "Offline Members List",
            "humans": "Human Members List",
            "bots": "Bot Members List"
        }
        response_title = response_title_map.get(selected_filter, "Member List")

        for member in self.guild.members:
            include_member = False
            if selected_filter == "all":
                include_member = True
                embed_color = discord.Color.blue()
            elif selected_filter == "online" and member.status != discord.Status.offline:
                include_member = True
                embed_color = discord.Color.green()
            elif selected_filter == "offline" and member.status == discord.Status.offline:
                include_member = True
                embed_color = discord.Color.red()
            elif selected_filter == "bots" and member.bot:
                include_member = True
                embed_color = discord.Color.light_grey()
            elif selected_filter == "humans" and not member.bot:
                include_member = True
                embed_color = discord.Color.gold() 
            
            if include_member:
                # Add status emoji to member details
                status_emoji = {
                    discord.Status.online: "🟢",
                    discord.Status.idle: "🟡",
                    discord.Status.dnd: "�",
                    discord.Status.offline: "⚫"
                }.get(member.status, "⚪") 
                
                member_list_details.append(f"{status_emoji} {member.display_name} (`{member.name}#{member.discriminator}`)")
                count += 1
        
        response_description = ""
        if not member_list_details: 
            response_description = f"No members found matching this filter."
        else:
            response_description = f"**{count}** members found:\n"
            if len(member_list_details) > 20: 
                response_description += "\n".join(member_list_details[:20]) + "\n... (showing first 20 members)"
            else:
                response_description += "\n".join(member_list_details)

        embed = discord.Embed(
            title=response_title,
            description=response_description,
            color=embed_color
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    async def on_timeout(self):
        """Disables view components and edits the message after the timeout period."""

        for item in self.children:
            if hasattr(item, 'disabled'):
                item.disabled = True

        if self.message:
            try:

                await self.message.edit(view=self)
            except discord.NotFound:

                pass
            except discord.Forbidden:

                pass
            except Exception as e:

                print(f"Error editing message on timeout: {e}")

# --- Bot Events ---
@bot.event
async def on_ready():
    """Event that fires when the bot is ready and logged in."""
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    try:
        if YOUR_GUILD_ID:

            guild_obj = discord.Object(id=YOUR_GUILD_ID)
            if hasattr(bot.tree, 'copy_global_to_guild'):
                bot.tree.copy_global_to_guild(guild=guild_obj)
                await bot.tree.sync(guild=guild_obj)
                print(f"Slash commands synced to guild {YOUR_GUILD_ID}!")
            else:

                print("Warning: bot.tree.copy_global_to_guild not found. Syncing globally (might take longer).")
                await bot.tree.sync()
        else:

            print("No Guild ID specified. Syncing slash commands globally (can take up to an hour).")
            await bot.tree.sync()
        print("Slash commands sync process initiated.")
    except Exception as e:
        print(f"Error syncing slash commands: {e}")

# --- Slash Commands ---
@bot.tree.command(name="members", description="Displays interactive member information.")
async def members_command(interaction: discord.Interaction):
    """Opens the interactive member information and help menu."""
    if interaction.guild is None:
        await interaction.response.send_message("This command can only be used in a server.", ephemeral=True)
        return

    view = MemberInfoView(interaction.guild)

    message = await interaction.response.send_message(
        "Here's your server's member information. Click a button or select an option:", 
        view=view, 
        ephemeral=False
    )
    view.message = message

if __name__ == "__main__":
    bot.run(YOUR_BOT_TOKEN)
