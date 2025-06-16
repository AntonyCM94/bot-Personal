// handlersW.js
const QRCode = require("qrcode-terminal");
require("dotenv").config();
const { default: makeWASocket, useMultiFileAuthState, DisconnectReason } = require("@whiskeysockets/baileys");
const { registrarAhorro } = require("../core/comandos");
const fs = require("fs");

async function startBot() {
  const { state, saveCreds } = await useMultiFileAuthState("auth");
  const sock = makeWASocket({
    auth: state,
    printQRInTerminal: false, // deprecated, lo gestionamos manualmente
  });

  sock.ev.on("creds.update", saveCreds);

  // Mostrar QR si es necesario
  sock.ev.on("connection.update", ({ qr, connection, lastDisconnect }) => {
    if (qr) {
      console.log("Escanea este QR para iniciar sesión:");
      QRCode.generate(qr, { small: true });
    }

    if (connection === "open") {
      console.log(" Conectado a WhatsApp");
    } else if (connection === "close") {
      const shouldReconnect = (lastDisconnect?.error?.output?.statusCode !== DisconnectReason.loggedOut);
      console.log(" Conexión cerrada. Reintentando...", shouldReconnect);
      if (shouldReconnect) {
        setTimeout(() => startBot(), 5000); // 5 segundos para respirar
      } else {
        console.log(" Sesión cerrada. Borra la carpeta 'auth' y vuelve a escanear el QR.");
      }
    }
  });

  // Escuchar mensajes
  sock.ev.on("messages.upsert", async ({ messages }) => {
    const msg = messages[0];
    if (!msg.message || msg.key.fromMe) return;

    const texto = msg.message.conversation || msg.message.extendedTextMessage?.text;
    const sender = msg.key.remoteJid;

    if (texto && texto.toLowerCase().startsWith("ahorro")) {
      try {
        registrarAhorro(sender, texto);
        await sock.sendMessage(sender, { text: " Ahorro registrado correctamente." });
      } catch (err) {
        console.error("Error al registrar ahorro:", err);
        await sock.sendMessage(sender, { text: "Error al guardar el ahorro." });
      }
    }
  });
}

startBot();

