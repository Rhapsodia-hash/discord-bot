import discord

from discord.ext import commands
from discord import Intents

intents = Intents.default()
intents.typing = False
intents.members = True
intents.presences = False
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_guild_join(guild):
    global SERVER
    servidor = guild
    print(servidor.members)
    print(f"se ha unido al servidor {guild.name}")
    SERVER = guild.id


@client.event
async def on_message(message):
    channel = message.channel
    fetch = await channel.fetch_message(message.id)
    if fetch.content == "hola":
        # print(fetch.content)
        print(message.guild.members)
    #   print(id)
    # print(fetch.created_at)
    # print(message.author)


@client.event
async def on_member_remove(member):
    print(f"{member.name} ha sido expulsado del servidor.")
    # Puedes realizar otras acciones aquí, como enviar un mensaje, almacenar información, etc.


@client.event
async def on_member_join(member):
    print(f"{member.name} se ha unido al servidor el {member.joined_at}")
    # Puedes realizar otras acciones aquí, como enviar un mensaje de bienvenida, asignar roles, etc.


@commands.command(name="members")
async def members_command(self, ctx):
    members = await ctx.guild.fetch_members()

    for member in members:
        await ctx.send(member.name)


# help(discord.Message)
client.run("MTIwMDE0OTM2NjIwNDI4MDkxMg.GHEL3Z._7BaqMwqz3AGCOfoNSWzdSWQRTvQCs9gFM10SM")
