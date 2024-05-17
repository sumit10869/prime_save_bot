import os
from .. import bot as gagan
from telethon import events, Button
from telethon.tl.types import InputMediaPhoto

S = "/start"
START_PIC = "https://graph.org/file/5e03ce82519cb95379e68.jpg"
TEXT = "👋 𝗛𝗶, 𝗜 𝗮𝗺 [𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐕𝐢𝐝𝐞𝐨 𝐒𝐚𝐯𝐞 𝐁𝐨𝐭 🖲️](https://t.me/private_Video_Save_Bot)\n\n👉🏻Execute /batch for bulk process upto 1000 files range.\n\n🧑‍💻**𝗢𝘄𝗻𝗲𝗿:** [๛𝐌𝐑๛𝐒𝐀𝐓𝐘𝐀𝐌๛](tg://openmessage?user_id=6090912349) \n☎️**𝗦𝘂𝗽𝗽𝗼𝗿𝘁:** [CLICK HERE](https://t.me/s_r_c_help_bot)"

def is_set_button(data):
    return data == "set"

def is_rem_button(data):
    return data == "rem"

@gagan.on(events.CallbackQuery(pattern=b"set"))
async def sett(event):    
    gagan = event.client
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    async with gagan.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
            return
        mime = x.file.mime_type
        if 'png' not in mime and 'jpg' not in mime and 'jpeg' not in mime:
            return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")

@gagan.on(events.CallbackQuery(pattern=b"rem"))
async def remt(event):  
    gagan = event.client            
    await event.edit('Trying... to save Bamby ... Wait')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        

@gagan.on(events.NewMessage(pattern=f"^{S}"))
async def start_command(event):
    # Creating inline keyboard with buttons
    buttons = [
        [Button.inline("✮ 𝗦𝗘𝗧 𝗧𝗛𝗨𝗠𝗕 ✮", data="set"),
         Button.inline("✮ 𝗥𝗘𝗠 𝗧𝗛𝗨𝗠𝗕 ✮", data="rem")],
        [Button.url("☠ 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗱 𝗕𝘆 ☠", url="tg://openmessage?user_id=6090912349")]
    ]

    # Sending photo with caption and buttons
    await gagan.send_file(
        event.chat_id,
        file=START_PIC,
        caption=TEXT,
        buttons=buttons
    )

