from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

✗ **I'm A String Session Generator Bot**🔥
✗ **I'm  Very Fast And Smooth**🔥
────────────────────────
✗ **If you don't trust this bot**, 
~ **stop reading this message**.
~ **delete this chat**.

**Still reading?**
**You can use me to generate pyrogram and telethon string session. Use below buttons to learn more** !
────────────────────────
✗ **Powered 💕 By**:~ **@TeamUltronX**
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="Back🔙", callback_data="back")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton("🌟TeamUltronX🌟", url="https://t.me/TeamUltronX")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🔰About🔰", callback_data="about")
        ],
        [InlineKeyboardButton("🌟TeamUltronX🌟", url="https://t.me/teamUltronX")],
    ]

    # Help Message
    HELP = """
🔥 **Available Commands** 🔥

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to generate pyrogram and telethon string session Made by [TeamUltronX](https://t.me/TeamUltronX)

🔥Source Code : [Click Here](https://github.com/TheUltronX/StringSessionGenerator)

🔥Framework : [Pyrogram](docs.pyrogram.org)

🔥Language : [Python](www.python.org)

🔥Developer : [TheUltronX](https://t.me/itz_me_ultronX)
    """
