from telegram.ext import Application, CommandHandler, MessageHandler, filters
import logging

import main

TOKEN = "8092238337:AAE9hmdeP40GzWXAeKv3XYa8SehjhQfKmSs"
ADMIN_CHAT_ID = "7647357239"

USUARIOS_FILE = "usuarios.txt"
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def guardar_usuario(chat_id):
    try:
        with open(USUARIOS_FILE, "r") as f:
            usuarios = f.read().splitlines()
    except FileNotFoundError:
        usuarios = []

    if str(chat_id) not in usuarios:
        usuarios.append(str(chat_id))
        with open(USUARIOS_FILE, "w") as f:
            f.write("\n".join(usuarios))
        logging.info(f"usuario guardado: {chat_id}")

async def start(update, context):
    chat_id = update.effective_chat.id
    guardar_usuario(chat_id)
    usuario = update.effective_user.first_name or "usuario"
    logging.info(f"Usuario {usuario} con ID {chat_id} ha iniciado el bot.")
    await context.bot.send_message(chat_id=chat_id, text="¡Hola! Soy tu bot de recordatorios. Usa /recordatorio para recibir un recordatorio diario.")
    await update.message.reply_text(f"Hola {usuario}! Ya estas registrado para recibir recordatorios.")

async def avisar(update, context):
    chat_id = update.effective_chat.id
    if str(chat_id) != ADMIN_CHAT_ID:
        await update.message.reply_text("No tienes permiso para usar este comando.")
        return

    mensaje = " ".join(context.args)
    if not mensaje:
        await update.message.reply_text("Usa /avisar <mensaje> para enviar un aviso a todos")
        return

    try:
        with open(USUARIOS_FILE, "r") as f:
            usuarios = f.read().splitlines()
    except FileNotFoundError:
        await update.message.reply_text("No hay usuarios registrados.")
        return

    for usuario_id in usuarios:
        try:
            await context.bot.send_message(chat_id=int(usuario_id), text=mensaje)
        except Exception as e:
            logging.warning(f"No se pudo enviar mensaje a {usuario_id}: {e}")
    await update.message.reply_text("Mensaje enviado a todos los usuarios registrados.")

async def mensaje_texto(update, context):
    await update.message.reply_text("Usa /start para comenzar.")

async def recordatorio(update, context):
    await update.message.reply_text("¡Este es tu recordatorio diario de ahorro! 💰")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("avisar", avisar))
    app.add_handler(CommandHandler("recordatorio", recordatorio))  # <-- Agrega este handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensaje_texto))
    logging.info("Bot iniciado.")
    app.run_polling()

if __name__ == "__main__":
    main()

# Asegúrate de tener instalada la última versión de python-telegram-bot
# pip install --upgrade python-telegram-bot
