# Discord Stats Bot

A simple yet functional Discord bot built with Python using the `discord.py` library. It provides live server member statistics and a clean interface via slash commands.

<img src="https://i.postimg.cc/0NZSybs6/image.png" width="400" />

---

## ✨ Features

* **📊 Member Statistics** — Real-time display of total, online, bot, and human members.
* **🌐 Slash Commands** — Easy-to-use Discord native commands.

---

## 🚀 Setup & Installation

Follow the steps below to run this bot on your own server.

### 1. Prerequisites

* **Python 3.8+** — [Download here](https://www.python.org/downloads/)
* **pip** — Python's package installer, usually comes bundled with Python.
* **Git** — [Download here](https://git-scm.com/downloads)

### 2. Create Bot & Get Required Info

#### Create a Discord Bot Application

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"**, give it a name
3. Navigate to the **"Bot"** tab, click **"Add Bot"**, then confirm

#### Obtain Bot Token

1. Still under the **"Bot"** tab, click **"Reset Token"** to get your bot token
2. **Store it securely** — Never share it publicly

#### Enable Privileged Intents

* Under the **"Bot"** tab, scroll to **"Privileged Gateway Intents"**
* Enable both:

  * **PRESENCE INTENT**
  * **SERVER MEMBERS INTENT**

### 3. Clone the Repository

Open your terminal or command prompt:

```bash
git clone https://github.com/AdityaLF/discord-stats-bot.git
cd discord-stats-bot
```

### 4.

Replace 'YOUR_BOT_TOKEN' with your actual bot token
```bash
YOUR_BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
```

### 5. Run the Bot

After configuring your environment variables and installing dependencies, you can start the bot with:

```bash
python bot.py
```

---

## 👤 Author

* **GitHub** → [@AdityaLF](https://github.com/AdityaLF)
* **Discord** → [@05.07am](https://discordapp.com/users/786163564205047839)
* **Support Me (Ko-fi)** → [ko-fi.com/adityaf](https://ko-fi.com/adityaf)

---

## 📄 License

This project is licensed under the **MIT License**
You are free to use, modify, and share this project.
