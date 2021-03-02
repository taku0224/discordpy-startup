from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


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
    
@bot.command()
async def a(ctx):
    def main():
  loop = asyncio.get_event_loop()
  v = loop.run_until_complete(f(1))  # ループにコルーチンを渡す

bot.run(token)
