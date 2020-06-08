import discord
import secret
import subprocess
import sys

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Идет подготовка отчета по электрической энергии за май 2020 г. Подождите около 2-3 минут...')
        process = subprocess.Popen(['C:\\Python38-32\\python.exe', 'D:\\PyCharmProject\\Serial\\Electro\\report_electro.py', '05', '06'])
        code = process.wait()
        await message.channel.send(file=discord.File("ЭЭ_Май_2020.xlsx"))

client.run(secret.DISCORD_TOKEN)
