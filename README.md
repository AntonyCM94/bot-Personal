# Bot personal de Whatsapp con Baileys
Este proyecto es un bot personal de WhatsApp desarrollado con [Baileys](https://github.com/WhiskeySockets/Baileys), una librería basada en WebSocket que permite interactuar con la API web de WhatsApp sin depender de WhatsApp Business API.

## Caracteristicas
  - Conexion en tiempo real a Whatsapp web
  - Gestion de comandos como `!ping`, `!ahorro`, etc.
  - Base de datos en archivo JSON (`./db/ahorros.json`)
  - Reconexion automatica ante errores
  - Estructura modular y facil de escalar

## Instalacion
  ```bash
  # 1. Clonar el repos
  git clone https://github.com/tu-usuario/bot-personal.git
  cd bot-personal

  # 2. Instalar dependencias
  npm install
  # 3. Crear carpeta y archivo JSON para la base de datos
  mkdir -p db
  echo "{}" > db/ahorros.json

  # 4.  Iniciar el bot
  node handlersW.js
