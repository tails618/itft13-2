from replit import db

from keep_alive import keep_alive

import os
import json
import time

import discord
from discord.ext import commands
from discord.ext import tasks

TOKEN = os.getenv("DISCORD_TOKEN")
RESET = False

if RESET:
    del db["root"]

bot = commands.Bot(command_prefix="m!")

microwaves = []
db["timeLeft"] = "0:00"

keep_alive()


@tasks.loop(seconds=1)
async def microwave(serverID):
    db_root = json.loads(db["root"])
    if len(db_root["servers"][str(serverID)]["queue"]) > 0:
        current_job = db_root["servers"][str(serverID)]["queue"][0]
        channel = bot.get_channel(db_root["servers"][str(serverID)]["channel"])

        await channel.send(
            f"<@{str(current_job[0])}> microwaving your {current_job[2]} now")

        for i in range(0, current_job[1]):
            await channel.send(
                "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
            )

            db_root = json.loads(db["root"])

            try:
                isNotActive = (current_job !=
                               db_root["servers"][str(serverID)]["queue"][0])
            except IndexError:
                isNotActive = True

            if isNotActive:
                break

            remaining = current_job[1] - i
            db["timeLeft"] = f"{int(remaining/60)}:{str(remaining % 60).zfill(2)}"
            time.sleep(1)

        db["timeLeft"] = "00:00"

        try:
            isNotActive = (current_job !=
                           db_root["servers"][str(serverID)]["queue"][0])
        except IndexError:
            isNotActive = True

        if not isNotActive:
            for i in range(0, 5):
                await channel.send(
                    "mmmmmmmmmmmmmmmmmBEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEPmmmmmmmmmmmmmmmmm"
                )
                time.sleep(1)

            if current_job[2].lower().endswith('s'):
                await channel.send(
                    f"<@{str(current_job[0])}> your {current_job[2]} are ready"
                )
            else:
                await channel.send(
                    f"<@{str(current_job[0])}> your {current_job[2]} is ready")

            db_root = json.loads(db["root"])
            try:
                isNotActive = (current_job !=
                               db_root["servers"][str(serverID)]["queue"][0])
            except IndexError:
                isNotActive = True

            if not isNotActive:
                db_root["servers"][str(serverID)]["queue"].pop(0)
            db["root"] = json.dumps(db_root)
        else:
            if current_job[2].lower().endswith('s'):
                await channel.send(
                    f"<@{str(current_job[0])}> your {current_job[2]} are still cold"
                )
            else:
                await channel.send(
                    f"<@{str(current_job[0])}> your {current_job[2]} is still cold"
                )

@tasks.loop(seconds=1)
async def microwave0(serverID):
    db_root = json.loads(db["root"])
    if len(db_root["servers"][str(serverID)]["queue"]) > 0:
        current_job = db_root["servers"][str(serverID)]["queue"][0]
        channel = bot.get_channel(db_root["servers"][str(serverID)]["channel"])

        await channel.send(
            f"<@{str(current_job[0])}> microwaving your {current_job[2]} now")

        for i in range(0, current_job[1]):
            await channel.send(
                "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
            )

            db_root = json.loads(db["root"])

            try:
                isNotActive = (current_job !=
                               db_root["servers"][str(serverID)]["queue"][0])
            except IndexError:
                isNotActive = True

            if isNotActive:
                break

            remaining = current_job[1] - i
            db["timeLeft"] = f"{int(remaining/60)}:{str(remaining % 60).zfill(2)}"
            time.sleep(1)

        db["timeLeft"] = "00:00"

        try:
            isNotActive = (current_job !=
                           db_root["servers"][str(serverID)]["queue"][0])
        except IndexError:
            isNotActive = True

        if not isNotActive:
            for i in range(0, 5):
                await channel.send(
                    "mmmmmmmmmmmmmmmmmBEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEPmmmmmmmmmmmmmmmmm"
                )
                time.sleep(1)

            if current_job[2].lower().endswith('s'):
                await channel.send(
                    f"<@{str(current_job[0])}> your {current_job[2]} are ready"
                )
            else:
                await channel.send(
                    f"<@{str(current_job[0])}> your {current_job[2]} is ready")

            db_root = json.loads(db["root"])
            try:
                isNotActive = (current_job !=
                               db_root["servers"][str(serverID)]["queue"][0])
            except IndexError:
                isNotActive = True

            if not isNotActive:
                db_root["servers"][str(serverID)]["queue"].pop(0)
            db["root"] = json.dumps(db_root)
        else:
            if current_job[2].lower().endswith('s'):
                await channel.send(
                    f"<@{str(current_job[0])}> your {current_job[2]} are still cold"
                )
            else:
                await channel.send(
                    f"<@{str(current_job[0])}> your {current_job[2]} is still cold"
                )


@tasks.loop(seconds=1)
async def microwave1(serverID):  # ITFT13
    db_root = json.loads(db["root"])
    if len(db_root["servers"][str(serverID)]["queue"]) > 0:
        current_job = db_root["servers"][str(serverID)]["queue"][0]
        channel = bot.get_channel(db_root["servers"][str(serverID)]["channel"])

        await channel.send(
            f"<@{str(current_job[0])}> microwaving your {current_job[2]} now")

        for i in range(0, current_job[1]):
            await channel.send(
                "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
            )

            db_root = json.loads(db["root"])

            try:
                isNotActive = (current_job !=
                               db_root["servers"][str(serverID)]["queue"][0])
            except IndexError:
                isNotActive = True

            if isNotActive:
                break

            remaining = current_job[1] - i
            db["timeLeft"] = f"{int(remaining/60)}:{str(remaining % 60).zfill(2)}"
            time.sleep(1)

        db["timeLeft"] = "00:00"

        try:
            isNotActive = (current_job !=
                           db_root["servers"][str(serverID)]["queue"][0])
        except IndexError:
            isNotActive = True

        if not isNotActive:
            for i in range(0, 5):
                await channel.send(
                    "mmmmmmmmmmmmmmmmmBEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEPmmmmmmmmmmmmmmmmm"
                )
                time.sleep(1)

            if current_job[2].lower().endswith('s'):
                await channel.send(
                    f"<@{str(current_job[0])}> your {current_job[2]} are ready"
                )
            else:
                await channel.send(
                    f"<@{str(current_job[0])}> your {current_job[2]} is ready")

            db_root = json.loads(db["root"])
            try:
                isNotActive = (current_job !=
                               db_root["servers"][str(serverID)]["queue"][0])
            except IndexError:
                isNotActive = True

            if not isNotActive:
                db_root["servers"][str(serverID)]["queue"].pop(0)
            db["root"] = json.dumps(db_root)
        else:
            if current_job[2].lower().endswith('s'):
                await channel.send(
                    f"<@{str(current_job[0])}> your {current_job[2]} are still cold"
                )
            else:
                await channel.send(
                    f"<@{str(current_job[0])}> your {current_job[2]} is still cold"
                )


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='m!help'))
    if "root" not in db.keys():
        db["root"] = '{"sanctioned" : [],"servers" : {}}'

    db_root = json.loads(db["root"])

    print(f'{bot.user} has connected to Discord!')

    for guild in bot.guilds:
        if str(guild.id) not in db_root["servers"]:
            db_root["servers"][str(guild.id)] = {"queue": [], "channel": None}

        microwaves.append(guild.id)

    db["root"] = json.dumps(db_root)

    for x in microwaves:
        if x == 781856224269434885: # H
          microwave0.start(x)
          print("hungus")
        elif x == 757729011592855633: # UCC
          microwave.start(x)
          print("bungus")
        elif x == 717046745149866046:  # ITFT13
          microwave1.start(x)
          print("Fungus")

    # await bot.change_presence(activity=discord.Game('m!help'))


@bot.event
async def on_guild_join(guild):
    db_root = json.loads(db["root"])
    db_root["servers"][str(guild.id)] = {"queue": [], "channel": None}
    db["root"] = json.dumps(db_root)

    microwaves.append(guild.id)
    if guild.id == 781856224269434885: # H
      microwave0.start(microwaves[-1])
      print("bungus")
    elif guild.id == 717046745149866046:
      microwave1.start(microwaves[-1])  # ITFT13
      print("fungus")


@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send(
            "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm no"
        )


@bot.command()
@commands.is_owner()
async def sanction(ctx, user: discord.User):
    "Sanctions people\nRequires: Bot Owner\nUsage: m!sanction <@user>"
    db_root = json.loads(db["root"])
    if user.id in db_root["sanctioned"]:
        await ctx.send(f"<@{str(user.id)}> is already sanctioned")
    else:
        db_root["sanctioned"].append(user.id)
        db["root"] = json.dumps(db_root)
        await ctx.send(f"Sanctioned <@{str(user.id)}>")


@bot.command()
@commands.is_owner()
async def pardon(ctx, user: discord.User):
    "Unsanctions people\nRequires: Bot Owner\nUsage: m!pardon <@user>"
    db_root = json.loads(db["root"])
    if user.id not in db_root["sanctioned"]:
        await ctx.send(f"<@{str(user.id)}> is not sanctioned")
    else:
        db_root["sanctioned"].remove(user.id)
        db["root"] = json.dumps(db_root)
        await ctx.send(f"Pardoned <@{str(user.id)}>")


@bot.command()
@commands.has_permissions(manage_channels=True)
async def channel(ctx, channel: discord.TextChannel):
    "Set microwave channel\nRequires: Manage Channels\nUsage: m!channel <#channel>"
    db_root = json.loads(db["root"])
    db_root["servers"][str(ctx.guild.id)]["channel"] = channel.id
    db["root"] = json.dumps(db_root)
    await ctx.send(f"Microwave output will appear in <#{str(channel.id)}>")


@bot.command()
async def start(ctx, itemName, duration):
    "Microwave item for set time\nUsage: m!start <item> <mm:ss>"
    print("stuff")
    db_root = json.loads(db["root"])

    if db_root["servers"][str(ctx.guild.id)]["channel"] is None:
        await ctx.send(
            "Microwave output is not configured. Select a channel using `m!channel <#channel>`"
        )
        return

    if ctx.author.id in db_root["sanctioned"]:
        await ctx.send("no")
        return

    for x in db_root["servers"][str(ctx.guild.id)]["queue"]:
        if x[0] == ctx.author.id:
            await ctx.send(
                "You already have an item in the queue. You can use `m!stop` to remove it from the queue."
            )
            return

    if ((len(duration) == 4 or len(duration) == 5) and ':' in duration
            and len(duration.split(':')) == 2):
        print("more stuff")
        times = duration.split(':')
        if len(times[0]) <= 2 and len(times[1]) == 2:
            print("most stuff")
            try:
                minutes = int(times[0])
                seconds = int(times[1])
            except ValueError:
                return

            seconds = seconds + minutes * 60

            if seconds > 1800:
              await ctx.send("Microwave time is too long. Maximum is 30 minutes per job.")
              return
            await ctx.send("ok")

            db_root["servers"][str(ctx.guild.id)]["queue"].append(
                [ctx.author.id, seconds, itemName])
            db["root"] = json.dumps(db_root)


@bot.command()
async def stop(ctx):
    "Remove from microwave queue"
    db_root = json.loads(db["root"])
    for entry in db_root["servers"][str(ctx.guild.id)]["queue"]:
        if entry[0] == ctx.author.id:
            await ctx.send("ok")
            db_root["servers"][str(ctx.guild.id)]["queue"].remove(entry)
            db["root"] = json.dumps(db_root)
            return

    await ctx.send("You don't have anything in the queue smh")


@bot.command()
async def queue(ctx):
    "Shows microwave queue for server"
    db_root = json.loads(db["root"])
    queue = db_root["servers"][str(ctx.guild.id)]["queue"]
    print(f"Chungus {len(queue)}")

    if len(queue) == 0:
        await ctx.send(
            "Nothing in the queue. Microwave something with `m!start <item> <mm:ss>`"
        )
    elif len(queue) == 1:
        await ctx.send(
            f'**Now Microwaving**\n{queue[0][2]} - {db["timeLeft"]} remaining ({str(bot.get_user(queue[0][0]))})'
        )
    elif len(queue) >= 2:
        print("Bungus")
        message = f'**Now Microwaving**\n{queue[0][2]} - {db["timeLeft"]} remaining ({str(bot.get_user(queue[0][0]))})\n\n**Queued**\n'

        queue.pop(0)
        for entry in queue:
            message = message + f'{entry[2]} - {int(entry[1]/60)}:{str(entry[1] % 60).zfill(2)} ({str(bot.get_user(entry[0]))})\n'

        print(message)
        await ctx.send(message)


@bot.command()
@commands.is_owner()
async def stopall(ctx):
  "Clears queue for server\nRequires: Bot Owner"
  await ctx.send("ok")
  db_root = json.loads(db["root"])
  db_root["servers"][str(ctx.guild.id)]["queue"] = []
  db["root"] = json.dumps(db_root)

bot.run(TOKEN)
