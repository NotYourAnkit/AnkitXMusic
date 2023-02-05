import asyncio
import speedtest
from pyrogram import filters
from strings import get_command
from AnonX import app
from AnonX.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**⇆ 𝘙𝘶𝘯𝘯𝘪𝘯𝘨 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘚𝘱𝘦𝘦𝘥𝘵𝘦𝘴𝘵 𝘉𝘢𝘣𝘺 😌...**")
        test.download()
        m = m.edit("**⇆ 𝘙𝘶𝘯𝘯𝘪𝘯𝘨 𝘜𝘱𝘭𝘰𝘢𝘥 𝘚𝘱𝘦𝘦𝘥𝘵𝘦𝘴𝘵 𝘉𝘢𝘣𝘺 😌...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**↻ 𝘚𝘩𝘢𝘳𝘪𝘯𝘨 𝘠𝘰𝘶𝘳 𝘚𝘱𝘦𝘦𝘥𝘵𝘦𝘴𝘵 𝘙𝘦𝘴𝘶𝘭𝘵𝘴 😎...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("💫 𝘛𝘳𝘺𝘪𝘯𝘨 𝘛𝘰 𝘊𝘩𝘦𝘤𝘬 ☑ 𝘜𝘱𝘭𝘰𝘢𝘥 𝘈𝘯𝘥 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘚𝘱𝘦𝘦𝘥𝘵𝘦𝘴𝘵 😎...")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""✯ **𝕊𝕡𝕖𝕖𝕕𝕋𝕖𝕤𝕥 ℝ𝕖𝕤𝕦𝕝𝕥𝕤** ✯
    
<u>**❥͜͡𝗖𝗹𝗶𝗲𝗻𝘁 💀 :**</u>
**» __ιѕρ :__** {result['client']['isp']}
**» __¢συηтяу :__** {result['client']['country']}
  
<u>**❥͜͡𝗦𝗲𝗿𝘃𝗲𝗿 ❤ :**</u>
**» __ηαмє :__** {result['server']['name']}
**» __¢συηтяу :__** {result['server']['country']}, {result['server']['cc']}
**» __ѕρσηѕσя :__** {result['server']['sponsor']}
**» __ℓєтєη¢у :__** {result['server']['latency']}  
**» __ριηg вαву :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
