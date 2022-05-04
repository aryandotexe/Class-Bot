import discord
import asyncio, os
from dotenv import load_dotenv

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

class Guild:
    def __init__(self, commands):
        self.commands: list[Command] = commands

    async def action(self, msg):
        for command in self.commands:
            await command.action(msg)

names = {
    "UnOfficial XII SC1 Discord v69.6.9": 865109924173316136
}
mapping = {
    "UnOfficial XII SC1 Discord v69.6.9": [ShailIsLol, Spandan]
}
guilds = {names[i]: Guild(mapping[i]) for i in names.keys()}

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")
    async def on_message(self, message: discord.Message):
        # region Deal Bot
        if message.author.id == self.user.id:
            return
        gid = message.guild.id
        await guilds[gid].action(message)

client = MyClient()
try:
    client.run(token)
except discord.errors.HTTPException:
    print("Blocked by rate limits")
    os.system("python restarter.py")
    os.system("kill 1")
