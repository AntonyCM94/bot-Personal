require('dotenv').config();

const TelegramBot = require("node-telegram-bot-api");
const { registrarAhorro } = require("../core/comandos");

const token = process.env.TELEGRAM_TOKEN;
const bot = new TelegramBot(token, { polling: true });

bot.on("message", (msg) => {
    const chatId = msg.chat.id;
    const texto = msg.text;

    if (texto.startsWith("/ahorrar")) {
        const partes = texto.split(" ");
        const cantidad = partes[1];
        const respuesta = registrarAhorro(msg.from.username, cantidad);
        bot.sendMessage(chatId, respuesta);
    }
});

const config = require("../config");



