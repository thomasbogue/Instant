import random
import discord
from discord_token import token

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f"we've logged on as {client.user}")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
      await greeting(message)
  if message.content.startswith('$help'):
      await help(message)
  if message.content.startswith('$r') or message.content.startswith('$roll'):
      await roll(message)
  if message.content.startswith('$h') or message.content.startswith('$heal'):
      await heal(message)
  if message.content.startswith('$d'):
      await rollD(message)

def greeting(message):
  return message.channel.send(f"Hello {message.author}, I'm Instant Servant, a Cypher RPG die rolling bot.  Type $help for more details on how I can help")

def help(message):
  return message.channel.send("Instant Servant:\n  $help\n    show this help\n  $r 3\n    make a level 3 roll\n  $d10 + 3\n    rolls a d10 and adds 3\n  $h +3\n    make a healing roll and add 3\n  $hello\n    Say hi.  Everybody appreciates politeness")

def roll(message):
  params = message.content.split()
  if (len(params) > 2):
      return message.channel.send(f"I'm not sure how to make that roll.  The syntax I'm expecting is $r 3, but you put more than one thing after the $r")
  if (len(params) < 2):
    level = 0
  else:
    try:
      level = int(params[1])
    except:
      return message.channel.send(f"I was expecting a number after the $r, but did you say '{params[1]}'?")
  roll = random.randint(1,20)
  target = 3 * level
  success = (roll >= target)
  success_message = ""
  if success:
      success_message = "Success!"
  else:
      success_message = "Failed."
  return message.channel.send(f"{success_message}  You rolled a {roll}, and the target was {target}")

def parseBonus(params):
  bonus = 0
  for param in params[1:]:
    try:
      b = int(param)
      bonus = bonus + b
    except ValueError:
      b = 0
  return bonus

def heal(message):
  params = message.content.split()
  bonus = 0
  if (len(params) > 1):
    bonus = parseBonus(params[1:])
  roll = random.randint(1,6)
  if (bonus == 0):
    reply = f"You rolled {roll} on your heal roll"
  else:
    reply = f"You rolled {roll} + {bonus} = {roll + bonus} on your heal roll"
  return message.channel.send(reply)

def rollD(message):
  params = message.content.split()
  try:
    d = int(params[0][2:])
  except:
    return message.channel.send(f"I was expecting $d6 or $d8, not '{params[0]}'")
  bonus = 0
  if (len(params) > 1):
    bonus = parseBonus(params[1:])
  roll = random.randint(1, d)
  if bonus == 0:
    reply = f"You rolled {roll} on 1d{d}"
  else:
    reply = f"You rolled {roll} + {bonus} = {roll + bonus} on 1d{d} + {bonus}"
  return message.channel.send(reply)

client.run(token)
