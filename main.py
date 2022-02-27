# Copyright (C) 2021-present notudope <https://github.com/notudope>

from time import sleep
from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

select = " "

help = """
Please go-to "my.telegram.org" (to get API_ID and API_HASH):
~ Login using your Telegram account.
~ Click on API development tools.
~ Create a new application, by entering the required details.

API_ID is "App api_id"
API_HASH is "App api_hash"

Or use:
- @apiscrapperbot
- @UseTGXBot
...
"""

docs = """
Telegram Client:
P -->> Pyrogram [https://docs.pyrogram.org]
T -->> Telethon [https://docs.telethon.dev]
"""

template = """
**This is your {} based UserBots** `STRING_SESSION`
⚠️ **DO NOT SHARE WITH ANYONE** ⚠️

```{}```

Generated by KASTA <3 @kastaid
"""

generated = """
Generated !! Check your Telegram "Saved Messages" to copy STRING_SESSION or copy from above.

~ Follow our channel https://t.me/kastaid
"""

print(help)

try:
    API_ID = int(input("Enter your API_ID here: "))
except ValueError:
    print(">> API_ID must be an integer.\nQuitting...")
    exit()
API_HASH = input("Enter your API_HASH here: ")

print(docs)

while select != ("p", "t"):
    select = input("Enter your required Client < P / T > : ").lower()
    if select == "t":
        print("\nTelethon selected!\nRunning script...")
        sleep(1)
        with TelegramClient(StringSession(), api_id=API_ID, api_hash=API_HASH) as client:
            print("\nGenerating Telethon STRING_SESSION...")
            string_session = client.session.save()
            saved_messages = template.format("Telethon", string_session)
            print("\n" + string_session + "\n")
            client.send_message("me", saved_messages)
            sleep(1)
            print(generated)
        break
    elif select == "p":
        print("\nPyrogram selected!\nRunning script...")
        sleep(1)
        with Client("UserBot", api_id=API_ID, api_hash=API_HASH) as client:
            print("\nGenerating Pyrogram STRING_SESSION...")
            string_session = client.export_session_string()
            saved_messages = template.format("Pyrogram", string_session)
            print("\n" + string_session + "\n")
            client.send_message("me", saved_messages)
            sleep(1)
            print(generated)
        break
    else:
        print("\nPlease only select P or T\n")
        sleep(1.5)
