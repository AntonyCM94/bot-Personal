from telegram import Bot
from telegram.error import TelegramError
import time

TOKEN = "8092238337:AAE9hmdeP40GzWXAeKv3XYa8SehjhQfKmSs"
CHAT_ID = "7647357239"  # Replace with your chat ID

def enviar_recordatorio():
    mensaje = "¡Hora de ahorrar 10€! Empieza por algo pequeño, de aqui a diciembre me lo agradeceras."
    bot = Bot(token=TOKEN)
    try: 
        bot.send_message(chat_id=CHAT_ID, text=mensaje)
        print("mensaje enviado.")
    except TelegramError as e:
        print(f"Error al enviar el mensaje: {e}")