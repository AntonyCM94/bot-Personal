// core/comandos.js
require('dotenv').config();

const fs = require("fs");
const dbPath = "./db/ahorros.json";

function registrarAhorro(usuario, cantidad) 
{
    let data =  {};
    if (fs.existsSync(dbPath)){
        data = JSON.parse(fs.readFileSync(dbPath))
    }

    if (!data[usuario]) data[usuario] = [];
    data[usuario].push({ cantidad, fecha: new Date().toISOString() });
    
    fs.writeFileSync(dbPath, JSON.stringify(data, null, 2));
    return `Se han registrado ${cantidad} € para ${usuario}`;
}
module.exports = { registrarAhorro };

const config = require("../config");
