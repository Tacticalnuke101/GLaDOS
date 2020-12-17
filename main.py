import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = "-")

@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')
  await ctx.send("Cog Loaded")

@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  await ctx.send("Cog Unloaded")

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('Doing Science'))
  print("I'm ready, you monster") 

@client.command()
async def ping(ctx):
  "Gives the bots latency"
  pass
  await ctx.send('My latency is {0}ms!'.format(round(client.latency*1000)))

@client.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
  "Gets pinged users avatar or your own"
  pass 
  try:
    userAvatarUrl = avamember.avatar_url
    useid = avamember
    await ctx.send("Avatar of " + str(useid))
    await ctx.send(userAvatarUrl)
  except:
    useid = ctx.message.author
    avamember = ctx.message.author
    userAvatarUrl = avamember.avatar_url 
    await ctx.send("Avatar of " + str(useid))
    await ctx.send(userAvatarUrl)
  
@client.command()
async def creator(ctx):
  "Shameless self promotion"
  pass
  await ctx.send("I was made by Tacticalnuke101#9502")

@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	
	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user
		
		if (user.name, user.discriminator) == (member_name, member_discriminator):
 			await ctx.guild.unban(user)
 			await ctx.channel.send(f"Unbanned: {user.mention}")

@client.command()
async def newrole(ctx, *, rolename):
  guild = ctx.guild
  await guild.create_role(name=rolename)

@client.command() 
async def unrole(ctx, *, rolename):
    role_object = discord.utils.get(ctx.message.guild.roles, name=rolename)
    await role_object.delete()

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run("NzUwODYxNjM5MTkyMDE4OTY0.X1AsZQ.9gP2juPNpdGVj9-ATizM3Q97Fvc")