from aiogram import Bot,Dispatcher,executor, types

TOKEN_API = "5979455758:AAELSJwHzcjROUWRtYBlep6QNJiQjFKP3B0"
HELP_COMMAND="""
i=i

"""
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)

@dp.message_handler(commands=["start"])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)
    await message.delete()
if __name__=="__main__":
    executor.start_polling(dp)

