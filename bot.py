import psutil
import time
import asyncio
from telegram import Bot

# Configura le tue credenziali di Telegram
TELEGRAM_API_KEY = 'APIKEY'
CHAT_ID = ID  # Sostituisci con il tuo ID chat

# Inizializza il bot
bot = Bot(token=TELEGRAM_API_KEY)

async def send_telegram_message(chat_id, message):
    await bot.send_message(chat_id=chat_id, text=message)

# Monitoraggio della batteria
async def monitor_battery():
    while True:
        battery = psutil.sensors_battery()
        if battery is None:
            print("Impossibile ottenere le informazioni sulla batteria. Uscita dal programma.")
            break

        percent = battery.percent
        plugged = battery.power_plugged

        if percent == 100 and plugged:
            await send_telegram_message(CHAT_ID, "Batteria carica")
        elif percent <= 20 and not plugged:
            await send_telegram_message(CHAT_ID, "Ricarica la batteria")

        await asyncio.sleep(60)  # Controlla ogni 60 secondi

if __name__ == "__main__":
    asyncio.run(monitor_battery())


