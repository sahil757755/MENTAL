from MashaRoBot import pbot as app
from MashaRoBot.pyrogramee.errors import capture_err
from MashaRoBot.pyrogramee.json_prettify import json_prettify
from MashaRoBot.pyrogramee.fetch import fetch
from pyrogram import filters


__mod_menu__ = "Repo"
__help__ = "/repo - To Get My Github Repository Link " "And Support Group Link"


@app.on_message(filters.command("repo") & ~filters.edited)
@capture_err
async def repo(_, message):
    users = await fetch(
        "https://api.github.com/repos/Prince301102/TianaBot/contributers"
    )
    list_of_users = ""
    count = 1
    for user in users:
        list_of_users += (
            f"**{count}.** [{user['login']}]({user['html_url']})\n"
        )
        count += 1

    text = f"""[Github](https://github.com/Prince301102/TianaBot) | [Group](t.me/Princebotsupport)
```----------------
| Contributors |
----------------```
{list_of_users}"""
    await app.send_message(
        message.chat.id, text=text, disable_web_page_preview=True
    )
