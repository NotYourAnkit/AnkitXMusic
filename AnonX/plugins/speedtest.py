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
        m = m.edit("**β ππΆπ―π―πͺπ―π¨ ππ°πΈπ―π­π°π’π₯ ππ±π¦π¦π₯π΅π¦π΄π΅ ππ’π£πΊ π...**")
        test.download()
        m = m.edit("**β ππΆπ―π―πͺπ―π¨ ππ±π­π°π’π₯ ππ±π¦π¦π₯π΅π¦π΄π΅ ππ’π£πΊ π...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**β» ππ©π’π³πͺπ―π¨ π π°πΆπ³ ππ±π¦π¦π₯π΅π¦π΄π΅ ππ¦π΄πΆπ­π΅π΄ π...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("π« ππ³πΊπͺπ―π¨ ππ° ππ©π¦π€π¬ β ππ±π­π°π’π₯ ππ―π₯ ππ°πΈπ―π­π°π’π₯ ππ±π¦π¦π₯π΅π¦π΄π΅ π...")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""β― **ππ‘ππππππ€π₯ βππ€π¦ππ₯π€** β―
    
<u>**β₯ΝΝ‘ππΉπΆπ²π»π π :**</u>
**Β» __ΞΉΡΟ :__** {result['client']['isp']}
**Β» __Β’ΟΟΞ·ΡΡΡ :__** {result['client']['country']}
  
<u>**β₯ΝΝ‘π¦π²πΏππ²πΏ β€ :**</u>
**Β» __Ξ·Ξ±ΠΌΡ :__** {result['server']['name']}
**Β» __Β’ΟΟΞ·ΡΡΡ :__** {result['server']['country']}, {result['server']['cc']}
**Β» __ΡΟΟΞ·ΡΟΡ :__** {result['server']['sponsor']}
**Β» __βΡΡΡΞ·Β’Ρ :__** {result['server']['latency']}  
**Β» __ΟΞΉΞ·g Π²Ξ±Π²Ρ :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
