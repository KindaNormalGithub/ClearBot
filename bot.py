import discord
from discord.ext import commands

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'MTEzMDcxNTAyMDI4ODg2ODU1Mw.GSz8JK.q3Do1MEUo3thABQLv_mHMk-h5jcKLZ472rdSRM'

intents = discord.Intents.default()
intents.messages = True  # Enable message-related events
intents.message_content = True  # Enable privileged message content intent

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def clear(ctx, amount: int):
    # Check if the user has the necessary permissions (manage_messages)
    if ctx.author.guild_permissions.manage_messages:
        # Delete the requested number of messages (up to 100 at a time)
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Successfully cleared {amount} messages.')
    else:
        await ctx.send("You don't have permission to use this command.")


bot.run(TOKEN)
