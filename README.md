# 🎵 DownYT - Bot de Telegram para Descargar Videos de YouTube 🎥

DownYT es un bot de Telegram desarrollado en Python que permite descargar videos de YouTube en formato MP3 y MP4. Utiliza la librería [`telebot`](https://pypi.org/project/telebot/) para la integración con Telegram y [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) para la descarga de videos.

## 📌 Características

- 📥 Descarga videos de YouTube en formato **MP3** o **MP4**.
- 📂 Guarda temporalmente los archivos en la carpeta `downloads/`.
- 🚀 Interfaz intuitiva con botones de selección de formato.
- 🔗 Solo necesitas enviar el enlace del video para descargarlo.

## 🚀 Instalación

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/downyt-bot.git
cd downyt-bot
```

### 2️⃣ Instalar dependencias
Ejecuta el siguiente comando para instalar las librerías necesarias:
```bash
pip install telebot yt-dlp
```

### 3️⃣ Configurar el bot
Edita el archivo `my_bot.py` y reemplaza `"MI-API-KEY"` con el **token de tu bot** de Telegram.

### 4️⃣ Ejecutar el bot
```bash
python my_bot.py
```

## 📂 Estructura del Proyecto

```
BOTS/
│── __pycache__/        # Archivos compilados de Python (generados automáticamente)
│── downloads/          # Carpeta donde se guardan los videos y audios descargados
│── download.py         # Script que maneja la descarga de videos y audios
└── my_bot.py           # Script principal que ejecuta el bot de Telegram
```

## 📜 Uso

1️⃣ Inicia el bot con `/start`.  
2️⃣ Usa `/Choose` para seleccionar el formato (**MP3** o **MP4**).  
3️⃣ Envía el enlace del video de YouTube.  
4️⃣ El bot descargará y enviará el archivo correspondiente.  

## 🛠 Tecnologías Usadas

- **Python** 🐍  
- **[telebot](https://pypi.org/project/telebot/)** (para la integración con Telegram)  
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** (para la descarga de videos)

## 📌 Autor
👤 **@Nigth_pg (Cesar Alb.)**  

¡Disfruta del bot! 🎶📹  
