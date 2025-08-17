import discord
import requests #type: ignore
import json
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env file

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

def get_joke():
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    json_data = json.loads(response.text)
    joke = json_data['setup'] + "\n||" + json_data['punchline'] + "||"
    return joke

def get_fact():
    response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    json_data = json.loads(response.text)
    return json_data['text']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_member_join(self, member):
        # Customize your welcome message channel ID here
        welcome_channel_id = 12345678910  # Replace with your channel ID
        channel = member.guild.get_channel(welcome_channel_id)
        if channel:
            try:
                await channel.send(f"Welcome to the server, {member.mention}! 🎉")
            except discord.Forbidden:
                print(f"Missing permissions to send welcome message in {channel.name}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        try:
            # Greetings
            if message.content.lower() in ['$hello', '$hi', '$hey']:
                await message.channel.send(f'Hello, {message.author.display_name}!')

            # Help command
            if message.content.startswith('$help'):
                help_text = (
                    "**Bot Commands:**\n"
                    "`$hello`, `$hi`, `$hey` - Greet the bot\n"
                    "`$userinfo` - Display your user info\n"
                    "`$meme` - Get a random meme\n"
                    "`$joke` - Hear a joke\n"
                    "`$fact` - Get a random fact\n"
                    "`$poll <question>` - Create a yes/no poll\n"
                )
                await message.channel.send(help_text)

            # Moderation: banned words
            banned_words = ['Add the words you want to exclude']
            if any(word in message.content.lower() for word in banned_words):
                try:
                    await message.delete()
                    await message.channel.send(f'Watch your language, {message.author.mention}')
                except discord.Forbidden:
                    await message.channel.send('Cannot delete message: missing permissions.')

            # Userinfo command
            if message.content.startswith('$userinfo'):
                if message.guild:
                    user = message.author
                    member = message.guild.get_member(user.id)
                    if member is None:
                        await message.channel.send('User info not found (maybe missing intent or not cached).')
                    else:
                        roles = [role.name for role in member.roles if role.name != "@everyone"]
                        await message.channel.send(
                            f'**Username:** {user}\n'
                            f'**ID:** {user.id}\n'
                            f'**Joined:** {member.joined_at}\n'
                            f'**Roles:** {", ".join(roles) if roles else "None"}'
                        )
                else:
                    await message.channel.send('This command can only be used in servers, not in direct messages.')

            # Meme
            if message.content.startswith('$meme'):
                await message.channel.send(get_meme())

            # Joke
            if message.content.startswith('$joke'):
                joke_text = get_joke()
                await message.channel.send(joke_text)

            # Fact
            if message.content.startswith('$fact'):
                fact_text = get_fact()
                await message.channel.send(fact_text)

            # Poll
            if message.content.startswith('$poll '):
                question = message.content[len('$poll '):]
                poll_msg = await message.channel.send(f'📊 **Poll:** {question}')
                await poll_msg.add_reaction('👍')
                await poll_msg.add_reaction('👎')

        except Exception as e:
            # Basic error message for unexpected issues
            await message.channel.send(f"An error occurred: {str(e)}")
            # Optionally log the error to console for debugging
            print(f"Error handling message: {e}")

# Set up intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents=intents)
client.run(TOKEN) 