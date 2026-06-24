# ⚔️ AFFCONQUER Welcome Bot

> Official Discord Welcome Bot for **AFFCONQUER** — the Minecraft community of [@OPANKUSHFF007](https://youtube.com/@OPANKUSHFF007)

---

## ✨ Features
- 🎉 Auto welcome embed on member join
- 💜 Purple themed rich embed with user PFP
- 🔢 Member count with ordinal (1st / 2nd / 3rd...)
- 🔘 3 buttons — Say Hi, Get MC IP, YouTube
- 💥 Smart spoiler ping (notifies without spamming)
- 👑 Bot status — "Watching AFFCONQUER grow"
- 🖼️ Optional banner GIF support

---

## 🚀 Setup

### Step 1 — Create Bot
1. Go to [discord.com/developers](https://discord.com/developers/applications)
2. New Application → name it `AFFCONQUER Bot`
3. Bot tab → Add Bot → Copy **TOKEN**
4. Enable Privileged Intents:
   - ✅ Server Members Intent
   - ✅ Message Content Intent

### Step 2 — Invite to Server
1. OAuth2 → URL Generator
2. Scopes: `bot`
3. Permissions:
   - ✅ Send Messages
   - ✅ Embed Links
   - ✅ Attach Files
   - ✅ Read Message History
   - ✅ Mention Everyone
   - ✅ Use External Emojis
4. Open generated URL → invite to AFFCONQUER

### Step 3 — Configure
Open `bot.py` and set:
```python
TOKEN               = "your_token_here"
WELCOME_CHANNEL_ID  = your_channel_id   # #general-chat
SERVER_INFO_CHANNEL = your_channel_id   # #server-info
BANNER_GIF_URL      = "your_gif_url"    # optional
```

### Step 4 — Deploy to Railway (Free 24/7)
1. Push this repo to GitHub
2. Go to [railway.app](https://railway.app) → New Project → GitHub repo
3. Add Environment Variable:
   ```
   DISCORD_TOKEN = your_token_here
   ```
4. Deploy — bot stays online forever for free ✅

---

## 📁 File Structure
```
AFFCONQUER-Bot/
├── bot.py            ← main bot file
├── requirements.txt  ← dependencies
├── Procfile          ← Railway deployment
├── .gitignore        ← keeps token safe
└── README.md         ← this file
```

---

## ⚠️ Important
- **Never** push your token to GitHub
- Use Railway Environment Variables for token
- `.gitignore` already protects `.env`

---

*Built for AFFCONQUER • The grind never stops ⚔️*
