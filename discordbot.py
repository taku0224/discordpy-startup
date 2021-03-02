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
    
 @client.event
async def on_ready():
    print('Ready')

@client.command(pass_context=True)
async def join(ctx, *, question):
    question_message = await ctx.send(f'アンケート： {question}\nhoi4参加できる？')
    await question_message.add_reaction('✅')


@bot.command()
async def hello(ctx):
    await ctx.send('よお')

@bot.command()
async def think(ctx):
    await ctx.send(':thinking:')
 

    

bot.run(token)
