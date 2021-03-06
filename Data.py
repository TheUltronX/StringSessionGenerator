from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

β **I'm A String Session Generator Bot**π₯
β **I'm  Very Fast And Smooth**π₯
ββββββββββββββββββββββββ
β **If you don't trust this bot**, 
~ **stop reading this message**.
~ **delete this chat**.

**Still reading?**
**You can use me to generate pyrogram and telethon string session. Use below buttons to learn more** !
ββββββββββββββββββββββββ
β **Powered π By**:~ **@TeamUltronX**
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("π₯ Start Generating Session π₯", callback_data="generate")],
        [InlineKeyboardButton(text="Backπ", callback_data="back")]
    ]

    generate_button = [
        [InlineKeyboardButton("π₯ Start Generating Session π₯", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("π₯ Start Generating Session π₯", callback_data="generate")],
        [InlineKeyboardButton("πTeamUltronXπ", url="https://t.me/TeamUltronX")],
        [
            InlineKeyboardButton("How to Use β", callback_data="help"),
            InlineKeyboardButton("π°Aboutπ°", callback_data="about")
        ],
        [InlineKeyboardButton("πTeamUltronXπ", url="https://t.me/teamUltronX")],
    ]

    # Help Message
    HELP = """
π₯ **Available Commands** π₯

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

π₯Source Code : [Click Here](https://github.com/TheUltronX/StringSessionGenerator)

π₯Framework : [Pyrogram](docs.pyrogram.org)

π₯Language : [Python](www.python.org)

π₯Developer : [TheUltronX](https://t.me/itz_me_ultronX)
    """
