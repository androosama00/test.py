import discord

class Client(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

        if message.content.startswith("anyone is here ?"):
            await message.channel.send("only me :cry: {0.author.mention}".format(message))

        if message.content.startswith("hey"):
           await message.channel.send("hey whats up man {0.author.mention}".format(message))
           

client = Client()
client.run('NjAxNzc4ODQxMTA2NTEzOTQw.XTSR5g.pNuVlYrPUs8y80SyjxMWvw8YOpk')

