import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

client.run('NzA0MzkwNDAxNDQ0MDIwMzE1.XqcdCA.SsBeWPI6WUKvbSGT4hUAquTOZbE')
