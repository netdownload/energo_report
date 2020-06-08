import discord
import secret

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
        await message.channel.send(file=discord.File('D:\PyCharmProject\Serial\Electro\demo.xlsx'))


client.run(secret.DISCORD_TOKEN)
