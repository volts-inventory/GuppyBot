import discord
import chatgpt

token = ""
client = discord.Client(intents=discord.Intents.all())

#msg_count_buff = 5


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.channel.name == 'guppy':
        if message.author == client.user:
            return
        print(message.content)
        resp = chatgpt.get_response(message.content, f"{message.author.display_name}")
        try:
            await message.channel.send(f"{message.author.display_name},\n {str(resp)}")
        except Exception as e:
            await message.channel.send("ERROR")

client.run(token)
