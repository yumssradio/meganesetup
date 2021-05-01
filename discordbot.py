from discord.ext import commands
import random
import os
import traceback

bot = commands.Bot(command_prefix='^')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def i(ctx):
    ilist = ('クラシックで穏やかな朝を。','ロックで社会にドロップキック！','ジャズとともにコーヒータイム','ラテンで朝から上げていこう！','J-POPで最新流行をチェック')
    result = random.choice(ilist)
    await ctx.send(result)

bot.run(token)
