import discord
import asyncio, os
from dotenv import load_dotenv
from discord.utils import get
from discord.ext import tasks
import re

load_dotenv()

token = os.getenv("token")


class Command:
    @staticmethod
    async def action(msg):
        pass


class ShailIsLol(Command):
    @staticmethod
    async def action(msg: discord.Message):
        if "shail" in msg.content.lower():
            await msg.reply("Shail is Gay.")


class Spandan(Command):
    async def action(msg: discord.Message):
        if "spandan" in msg.content.lower():
            await msg.reply("Hottest man on earth ever.")


class Pavan(Command):
    async def action(msg: discord.Message):
        if "pavan" in msg.content.lower():
            await msg.reply("The Annoying weird Kinky boy :LMFAOOO:")


class Bhargav(Command):
    async def action(msg: discord.Message):
        if "bhargav" in msg.content.lower():
            await msg.reply("Actual Chad :DDD")


class Riona(Command):
    async def action(msg: discord.Message):
        if "riona" in msg.content.lower():
            await msg.reply("Wanna be murderer lmfao")


class Darshan(Command):
    async def action(msg: discord.Message):
        if "darshan" in msg.content.lower():
            await msg.reply(
                "Gae ass n*gga. atleast he knows a lil bit coding lmfao")


class Ridhima(Command):
    async def action(msg: discord.Message):
        if "ridhima" in msg.content.lower():
            await msg.reply(
                "Nerdy Blind Cow who loves Harry Potter Weirdo lmao.")


class Harsh(Command):
    async def action(msg: discord.Message):
        if "harsh" in msg.content.lower():
            await msg.reply("Dad of the group :D")




class Guild:
    def __init__(self, commands):
        self.commands: list[Command] = commands

    async def action(self, msg):
        for command in self.commands:
            await command.action(msg)


names = {"UnOfficial XII SC1 Discord v69.6.9": 865109924173316136}
mapping = {
    "UnOfficial XII SC1 Discord v69.6.9":
    [ShailIsLol, Spandan, Bhargav, Riona, Ridhima, Harsh, Pavan, Darshan]
}
guilds = {names[i]: Guild(mapping[i]) for i in names.keys()}


class MyClient(discord.Client):
    async def on_ready(self):
        global school
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")
        school = self.get_guild(names['UnOfficial XII SC1 Discord v69.6.9'])

    async def on_member_update(self, before, after):
        bact = list(before.activities)
        aact = list(after.activities)
        if len(bact) == len(aact):
            return

        role = get(school.roles, name="Music")

        waslisten = False
        islisten = False
        for i in bact:
            if isinstance(i, discord.activity.Spotify):
                waslisten = True

        for i in aact:
            if isinstance(i, discord.activity.Spotify):
                islisten = True

        if not waslisten and islisten:
            await before.add_roles(role)
        elif waslisten and not islisten:
            await before.remove_roles(role)
    async def on_message(self, message: discord.Message):
        
        if message.author.id == self.user.id:
            return
        gid = message.guild.id
        await guilds[gid].action(message)


client = MyClient(intents=discord.Intents.all())
try:
    client.run(token)
except discord.errors.HTTPException:
    print("Blocked by rate limits")
    os.system("python restarter.py")
    os.system("kill 1")
