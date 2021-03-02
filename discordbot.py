from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

await client.change_presence(activity=discord.Game(name='Healts of Iron Ⅳ'))

# or, for watching:
activity = discord.Activity(name='Healts of Iron Ⅳ', type=discord.ActivityType.watching)
await client.change_presence(activity=activity)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def hello(ctx):
    await ctx.send('よお')

@bot.command()
async def think(ctx):
    await ctx.send(':thinking:')
 

    

bot.run(token)
