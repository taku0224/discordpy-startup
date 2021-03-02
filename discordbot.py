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
    
@bot.event
async def get_content(n):
  print(f'start {n}')
  await asyncio.sleep(random.randint(1, 5))  # レスポンスタイムが違うことをシミュレート
  print(f'end {n}')
  return n

async def f(n):
  tasks = (
    asyncio.ensure_future(get_content('a')),
    asyncio.ensure_future(get_content('b')),
    asyncio.ensure_future(get_content('c')),
  )
  return n, await asyncio.gather(*tasks)

bot.run(token)
