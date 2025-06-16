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
  node handlersW.js`
```
Cuando lo inicies por primera vez, te aparecerá un código QR en consola. Escanéalo desde WhatsApp Web con tu móvil y listo.
## Estructura
```
bot-personal-whatsapp/
├── core/
│   └── comandos.js       # Lógica de los comandos personalizados
├── db/
│   └── ahorros.json      # Base de datos local en formato JSON
├── whatsappBot/
│   └── handlersW.js      # Entrada principal del bot
├── config.js             # Configuración del bot
├── package.json
└── README.md
```
Notas de seguridad
  - No compartas tu archivo de sesión de WhatsApp en público.
  - Considera agregar autenticación si despliegas el bot online.
  - Puedes usar .env para ocultar claves o ajustes sensibles.

Futuras mejoras
  - Soporte para comandos dinámicos desde JSON o base de datos
  - Dashboard web para ver el estado del bot
  - Persistencia de sesión en la nube

Autor 
  Desarrollador por AntonyCM94
