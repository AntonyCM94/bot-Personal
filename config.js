require('dotenv').config();

module.exports = {
    TELEGRAM_TOKEN: process.env.TELEGRAM_TOKEN,
    WHATSAPP_GROUP_ID: process.env.WHATSAPP_GROUP_ID,
    ADMIN_USERS: ['Antony'],
    DB_PATH: process.env.DB_PATH || './usuarios.txt'
};