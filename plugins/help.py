from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Bot Can Download Mp3/Mp4 from yotubebe Powered by @BeastX_Bots"
    await message.reply_text(helptxt)
