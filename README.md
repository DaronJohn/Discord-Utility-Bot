# Discord Utility Bot

## 📌 Description
A simple Discord bot built in Python using `discord.py` that provides fun and useful features like memes, jokes, random facts, user info, moderation (word filtering), polls, and welcome messages.  
It listens to text commands and interacts with external APIs for content.

---

## ✨ Features

- **Greeting commands:** `$hello`, `$hi`, `$hey`
- **User information:** `$userinfo`
- **Random memes:** `$meme`
- **Random jokes:** `$joke`
- **Random facts:** `$fact`
- **Poll creation:** `$poll`
- **Moderation:** Automatically deletes messages containing banned words and warns users
- **Welcome message:** Greets users joining the server in a specified channel

---

## ⚙️ Setup & Usage

### ✅ Prerequisites
- Python **3.8+**
- Discord **bot token** (from [Discord Developer Portal](https://discord.com/developers/applications))
- Libraries:
  - `discord.py`
  - `python-dotenv`
  - `requests`

---

### 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. **(Optional) Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install discord.py python-dotenv requests
   ```

4. **Create a `.env` file** in the root folder with your bot token:
   ```env
   DISCORD_BOT_TOKEN=your_bot_token_here
   ```

5. **Update the `welcome_channel_id`** in your bot script with your server’s welcome channel ID.

---

### ▶️ Running the Bot
```bash
python bot.py
```
*(Replace `bot.py` with your script’s filename if different.)*

---

## 🔑 Permissions & Intents

Make sure to enable these in your **Discord Developer Portal** and server:

- **Privileged Gateway Intents:**
  - ✅ Server Members Intent  
  - ✅ Message Content Intent  

- **Bot Permissions in your Discord Server:**
  - Send Messages  
  - Manage Messages *(for moderation)*  
  - Read Message History *(recommended)*  
  - Add Reactions *(for polls)*  

---

## 🛡️ Customizing Moderation
Edit the `banned_words` list in the script to add or remove words you want the bot to auto-moderate.

---

## ⚠️ Important Notes
- 🔒 **Keep your bot token private!** Never share it or commit it to public repositories.  
- This bot uses environment variables (`.env` file) to keep secrets safe.  
- You can extend the bot by adding new commands or converting it to `discord.ext.commands.Bot` for more advanced functionality.  

---

## 📜 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.