import subprocess
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/start'):
        result = subprocess.run(["bash", "/home/user/pc_wake.sh"], capture_output=True, text=True)

        if result.returncode == 0:
            await message.channel.send('Minecraft server starting...')
            result = subprocess.run(["bash", "/home/user/check_online.sh"], capture_output=True, text=True)
            await message.channel.send('Minecraft server is up now !')
        else:
            await message.channel.send(f'Error starting server: {result.stderr}')

    if message.content.startswith('/stop'):
        await message.channel.send('Stoping minecraft server...')
        result = subprocess.run(["bash", "/home/user/shutdown_server.sh"], capture_output=True, text=True)
        if result.returncode == 0:
            await message.channel.send('Minecraft server stopping...')
            result = subprocess.run(["bash", "/home/user/check_offline.sh"], capture_output=True, text=True)
            await message.channel.send('Minecraft server stopped !')
        else:
            await message.channel.send(f'Error stoping server: {result.stderr}')

    if message.content.startswith('/check'):
        result = subprocess.run(["bash", "/home/user/check_status.sh"], capture_output=True, text=True)
        if result.returncode == 0:
            status = result.stdout.strip()  # Get the output from the script and remove any extra spaces/newlines
            if status == "Online":
                await message.channel.send('Minecraft server is up now!')
            elif status == "Offline":
                await message.channel.send('Minecraft server is down.')
            else:
                await message.channel.send('Unexpected status received.')
        else:
            await message.channel.send(f'Error checking server status: {result.stderr}')

client.run('your_discord_bot_KEY')
