from unicodedata import name
import discord
from discord.ext import commands
from discord import Embed
import aiohttp
import asyncio
import random
import asyncpraw
import requests 


prefixes = ["gu ","Gu ","GU ","gU "]
client = commands.Bot(command_prefix = prefixes)

reddit = asyncpraw.Reddit(client_id='ylLQZYSpayeFe7nvBHG11w', client_secret='DhdZ16iWVxU9VZXzOIr4QLwtJT2J8Q',user_agent='Dm SKY#4515 if any problems. made this for a personal discord bot.')

@client.event #setup
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='cries from the gulag' , url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
    channel = client.get_channel(997127467867308184)
    await channel.send("I'm up bitches")
    print('Bot is online')

@client.event #no command error
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used')
        
@client.event #deleted message
async def on_message_delete(message):
    channel = client.get_channel(997130575670415501)
    await channel.send(f'{message.author.mention} deleted a message:\n {message.content}')

"""@client.event #on join
async def  """
#--------------------------------
    
@client.event #f in the chat
async def on_message(message):
    if (message.content == 'f' or message.content == 'F') and not message.author.bot:
           await message.channel.send("f")
           await client.process_commands(message)
           return   
    else: 
        await client.process_commands(message)
        return

    

#-------------------------------
@client.command() #add
async def add(ctx, a: float, b: float):
    await ctx.send(a + b)

@client.command() #multiply
async def mul(ctx, a:float, b:float):
    await ctx.send(a * b)

@client.command() #subtract
async def sub(ctx, a:float, b:float):
    await ctx.send(a - b)

@client.command() #division
async def div(ctx, a:float, b:float):
    await ctx.send(a / b)

@client.command() #rem
async def rem(ctx, a:float, b: float):
    await ctx.send(a % b)
   
@client.command() #clear messages
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount : int):
    await ctx.channel.purge(limit=amount+1)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Specify number of messages to be cleared')
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("Perms ni hai tere pe, Gu khale")

@client.command() #kick
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked')
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Mention the user you want to kick')
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("Perms ni hai tere pe, Gu khale")
       
   
@client.command() #ban
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned')
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Mention the user you want to ban')
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("Perms ni hai tere pe, Gu khale")

@client.command() #unban
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banlist = await ctx.guild.bans()
    mem_name, mem_disc = member.split('#')

    for ban_entry in banlist:
        user = ban_entry.user
        if (user.name, user.discriminator) == (mem_name, mem_disc):
            await ctx.guild.unban(user)
            await ctx.send(f'{mem_name}#{mem_disc} has been unbanned')
            return
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Mention the username and tag of the user you want to unban')
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("Perms ni hai tere pe, Gu khale")

@client.command() #poop dm
async def khale(ctx, member: discord.Member):
    channel = await member.create_dm()
    await channel.send("yeh le :poop:")
    await ctx.send(":poop: is on the way")
@khale.error
async def khale_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("User ko mention tera baap karega?")

@client.command() #send image
async def dm(ctx, member: discord.Member):
    channel = await member.create_dm()
    await channel.send('le')
    await channel.send(file=discord.File('hehe.png'))
    await ctx.send('sent')
@dm.error
async def dm_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("User ko mention tera baap karega?")


@client.command() #choose game
async def choose(ctx, *args):
    lst=[]
    for a in args:
        lst.append(a)
    await ctx.send(f'{random.choice(lst)}')    
@choose.error
async def choose_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("")

@client.command()
async def coinflip(ctx):
    variable = ["head","tail"]
    await ctx.send("{}".format(random.choice(variable)))

"""@client.command(pass_context=True)
async def dankmeme(ctx):
    embed=discord.Embed(title='', description='')
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)"""

@client.command(pass_context=True)
async def memes(ctx):
    embed=discord.Embed()
    author=ctx.author
    print(author,type(author))
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            rand=random.randint(0, 25)
            embed.set_author(name=author)
            embed.title=res['data']['children'][rand]['data']['title']
            embed.set_image(url=res['data']['children'] [rand]['data']['url'])
            await ctx.send(embed=embed) 

@client.command(pass_context=True)
async def dank(ctx):
    meme_subreddit = await reddit.subreddit('dankmemes')
    sub_submissions = meme_subreddit.hot()
    post_to_pick = random.randint(1, 20)
    for _ in range(0, post_to_pick):
        submission = next(x for x in sub_submissions if not x.stickied)
    e = discord.Embed(title=f'Requested by {ctx.author}', description=f'{submission.title}', color=0xFFFFF)
    e.set_image(url=submission.url)
    await ctx.send(embed=e)
    
"""@client.command()
async def meme(ctx):
    
    all_subs=[]
    top=reddit.subreddit('memes').top(Limit=50)
    for submission in top:
        all_subs.append(submission)
    random_sub=random.choice(all_subs)

    name=random_sub.title
    url=random_sub.url

    em=discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(embed=em)"""

    
#----------------------------------------------------------

    


     

client.run('#enter token')    
