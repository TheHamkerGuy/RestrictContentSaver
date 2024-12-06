"""
This bot saves restricted content and makes it accessible to users via commands. 
Includes commands for start, help, and ToS.

Author:
    - @TheHamkerGuy on Telegram
    - @TheHamkerGuy on GitHub

Project:
    - Developed for the @ToolsTheHamkerGuy channel on Telegram.

License:
    This code is open-source and can be reused or modified under the following conditions:
    1. Proper credits must be given to the original authors.
    2. A link to the original source must be included in derivative works.

Disclaimer:
    This project was coded solely for learning purposes. The owner will not be held responsible
    for any misuse, illegal activities, or violations of Terms of Service (ToS) of any platform 
    arising from the use or modification of this code. Users are strongly advised to comply with 
    the applicable rules and regulations of the services they interact with.

Dependencies:
    - Pyrogram
"""

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


@Client.on_message(filters.command("start"))
async def start(bot: Client, m: Message):
    """
    Handle the /start command. Sends a welcoming message to the user with buttons for navigation.

    Args:
        bot (Client): The bot client instance.
        m (Message): Incoming message object.
    """
    photo = "https://imgur.com/a/oukNSXa"  # Replace with a valid image URL
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🌟 ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ 🌟", url="https://t.me/ToolsTheHamkerGuy"),
                InlineKeyboardButton("🍀 sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ 🍀", url="https://t.me/ToolsTheHamkerGuySupport")
            ],
            [
                InlineKeyboardButton("🧑‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🧑‍💻", callback_data="developer"),
                InlineKeyboardButton("📜 TᴏS 📜", callback_data="tos")
            ]
        ]
    )
    start_text = (
        "🌟 **ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴄᴏɴᴛᴇɴᴛ sᴀᴠᴇʀ ʙᴏᴛ!** 🌟\n\n"
        "✨ **ғᴇᴀᴛᴜʀᴇs:**\n"
        "🔹 sᴀᴠᴇ ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ ᴇᴀsɪʟʏ.\n"
        "🔹 ʀᴇᴛʀɪᴇᴠᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜ sɪᴍᴘʟᴇ ᴄᴏᴍᴍᴀɴᴅs.\n"
        "📝 **ᴜsᴀɢᴇ:**\n"
        "1️⃣ sᴇɴᴅ ᴛʜᴇ ʟɪɴᴋ ᴏғ ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ ᴛᴏ sᴀᴠᴇ.\n"
        "2️⃣ ᴜsᴇ ᴄᴏᴍᴍᴀɴᴅs ʟɪᴋᴇ `/save` ᴛᴏ ʀᴇᴛʀɪᴇᴠᴇ ᴄᴏɴᴛᴇɴᴛ.\n\n"
        "ғᴏʀ ʜᴇʟᴘ, ᴄʟɪᴄᴋ on **ʜᴇʟᴘ** ᴏʀ ᴛʏᴘᴇ `/help`."
    )
    await m.reply_photo(photo=photo, caption=start_text, reply_markup=btn)


@Client.on_message(filters.command("help"))
async def help(bot: Client, m: Message):
    """
    Handle the /help command. Provides details about bot features and usage.

    Args:
        bot (Client): The bot client instance.
        m (Message): Incoming message object.
    """
    help_text = (
        "**🆘 ʜᴇʟᴘ - ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ sᴀᴠᴇʀ ʙᴏᴛ**\n\n"
        "🔹 **ᴄᴏᴍᴍᴀɴᴅs:**\n"
        "• `/start`: sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ᴠɪᴇᴡ ᴛʜᴇ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ.\n"
        "• `/help`: ᴅɪsᴘʟᴀʏ ᴛʜɪs ʜᴇʟᴘ ᴍᴇssᴀɢᴇ.\n"
        "• `/repo`: ᴠɪᴇᴡ ᴛʜᴇ ʙᴏᴛ's sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.\n"
        "• `/tos`: ʀᴇᴀᴅ ᴛʜᴇ ʙᴏᴛ's ᴛᴇʀᴍs ᴏғ sᴇʀᴠɪᴄᴇ.\n\n"
        "🔹 **ʜᴏᴡ ᴛᴏ ᴜsᴇ:**\n"
        "1️⃣ sᴇɴᴅ ᴀ ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ ʟɪɴᴋ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.\n"
        "2️⃣ ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ sᴀᴠᴇ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ғᴏʀ ʏᴏᴜ ʏᴏᴜ.\n\n"
        "ғᴏʀ ғᴜʀᴛʜᴇʀ ᴀssɪsᴛᴀɴᴄᴇ, ᴊᴏɪɴ ᴏᴜʀ **sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ**."
    )
    await m.reply_text(help_text)


@Client.on_message(filters.command("tos"))
async def tos(bot: Client, m: Message):
    """
    Handle the /tos command. Displays the bot's Terms of Service.

    Args:
        bot (Client): The bot client instance.
        m (Message): Incoming message object.
    """
    tos_text = (
        "**📜 ᴛᴇʀᴍs ᴏғ sᴇʀᴠɪᴄᴇ - ʀᴇsᴛʀɪᴄᴛ ᴄᴏɴᴛᴇɴᴛ sᴀᴠᴇʀ ʙᴏᴛ**\n\n"
        "1️⃣ ᴛʜɪs ʙᴏᴛ ɪs ғᴏʀ ᴇᴅᴜᴄᴀᴛɪᴏɴᴀʟ ᴘᴜʀᴘᴏsᴇs ᴏɴʟʏ.\n"
        "2️⃣ ᴛʜᴇ ᴏᴡɴᴇʀ ɪs ɴᴏᴛ ʀᴇsᴘᴏɴsɪʙʟᴇ ғᴏʀ ᴀɴʏ ᴍɪsᴜsᴇ ᴏʀ ᴠɪᴏʟᴀᴛɪᴏɴ ᴏғ ᴘʟᴀᴛғᴏʀᴍ TᴏS.\n"
        "3️⃣ ᴜsᴇʀs ᴍᴜsᴛ ᴄᴏᴍᴘʟʏ ᴡɪᴛʜ ᴀʟʟ ᴀᴘᴘʟɪᴄᴀʙʟᴇ ʟᴀᴡs ᴀɴᴅ ᴘʟᴀᴛғᴏʀᴍ ᴘᴏʟɪᴄɪᴇs.\n"
        "4️⃣ ᴛʜᴇ ʙᴏᴛ ʀᴇsᴇʀᴠᴇs ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ʙᴀɴ ᴜsᴇʀs ғᴏʀ ᴀʙᴜsᴇ ᴏʀ ᴍɪsᴜsᴇ.\n\n"
        "ʙʏ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴀɢʀᴇᴇ ᴛᴏ ᴛʜᴇsᴇ ᴛᴇʀᴍs."
    )
    await m.reply_text(tos_text)



@Client.on_callback_query(filters.regex("tos"))
async def tos_callback(bot: Client, q: CallbackQuery):
    """
    Handle ToS button callback. Displays the bot's Terms of Service.

    Args:
        bot (Client): The bot client instance.
        q (CallbackQuery): Incoming callback query object.
    """
    btn = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("ʙᴀᴄᴋ 🔙", callback_data="back")]
        ]
    )
    tos_text = (
        "**📜 ᴛᴇʀᴍs ᴏғ sᴇʀᴠɪᴄᴇ - ʀᴇsᴛʀɪᴄᴛ ᴄᴏɴᴛᴇɴᴛ sᴀᴠᴇʀ ʙᴏᴛ**\n\n"
        "1️⃣ ᴛʜɪs ʙᴏᴛ ɪs ғᴏʀ ᴇᴅᴜᴄᴀᴛɪᴏɴᴀʟ ᴘᴜʀᴘᴏsᴇs ᴏɴʟʏ.\n"
        "2️⃣ ᴛʜᴇ ᴏᴡɴᴇʀ ɪs ɴᴏᴛ ʀᴇsᴘᴏɴsɪʙʟᴇ ғᴏʀ ᴀɴʏ ᴍɪsᴜsᴇ ᴏʀ ᴠɪᴏʟᴀᴛɪᴏɴ ᴏғ ᴘʟᴀᴛғᴏʀᴍ TᴏS.\n"
        "3️⃣ ᴜsᴇʀs ᴍᴜsᴛ ᴄᴏᴍᴘʟʏ ᴡɪᴛʜ ᴀʟʟ ᴀᴘᴘʟɪᴄᴀʙʟᴇ ʟᴀᴡs ᴀɴᴅ ᴘʟᴀᴛғᴏʀᴍ ᴘᴏʟɪᴄɪᴇs.\n"
        "4️⃣ ᴛʜᴇ ʙᴏᴛ ʀᴇsᴇʀᴠᴇs ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ʙᴀɴ ᴜsᴇʀs ғᴏʀ ᴀʙᴜsᴇ ᴏʀ ᴍɪsᴜsᴇ.\n\n"
        "ʙʏ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴀɢʀᴇᴇ ᴛᴏ ᴛʜᴇsᴇ ᴛᴇʀᴍs."
    )
    await q.message.edit_text(tos_text, reply_markup=btn)


@Client.on_callback_query(filters.regex("back"))
async def back_to_home(bot: Client, q: CallbackQuery):
    """
    Handle back button callback. Returns to the start message.

    Args:
        bot (Client): The bot client instance.
        q (CallbackQuery): Incoming callback query object.
    """
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🌟 ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ 🌟", url="https://t.me/ToolsTheHamkerGuy"),
                InlineKeyboardButton("🍀 sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ 🍀", url="https://t.me/ToolsTheHamkerGuySupport")
            ],
            [
                InlineKeyboardButton("🧑‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🧑‍💻", callback_data="developer"),
                InlineKeyboardButton("📜 TᴏS 📜", callback_data="tos")
            ]
        ]
    )
    back_text = (
        "🌟 **ᴡᴇʟᴄᴏᴍᴇ ʙᴀᴄᴋ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴄᴏɴᴛᴇɴᴛ sᴀᴠᴇʀ ʙᴏᴛ!** 🌟\n\n"
        "✨ **ғᴇᴀᴛᴜʀᴇs:**\n"
        "🔹 sᴀᴠᴇ ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ ᴇᴀsɪʟʏ.\n"
        "🔹 ʀᴇᴛʀɪᴇᴠᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜ sɪᴍᴘʟᴇ ᴄᴏᴍᴍᴀɴᴅs.\n\n"
        "ғᴏʀ ʜᴇʟᴘ, ᴄʟɪᴄᴋ ᴏɴ **ʜᴇʟᴘ** ᴏʀ ᴛʏᴘᴇ `/help`."
    )
    await q.edit_message_text(back_text, reply_markup=btn)
