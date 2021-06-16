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
    
    
@commands.command(name='del')
async def _purge(self, ctx):
    logs = [log async for log in message.channel.history() if log.author == message.author]
    await message.channel.delete_messages(logs)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def i(ctx):
    ilist = ('ゆうおすすめの曲はhttps://www.youtube.com/watch?v=gjDrEdEzfQc　です。','えてけおすすめの曲はhttps://youtu.be/YnSW8ian29w　です。','さめおすすめの曲はhttps://youtu.be/61xsHlw99II　です。','おにぎりおすすめの曲はhttps://youtu.be/Gs069dndIYk　です。')
    result = random.choice(ilist)
    await ctx.send(result)

bot.run(token)
