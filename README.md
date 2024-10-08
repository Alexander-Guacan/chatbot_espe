# Chatbot de la Universidad de las Fuerzas Armadas ESPE

Este proyecto es un chatbot especializado para responder preguntas frecuentes sobre la Universidad de las Fuerzas Armadas ESPE. El sistema está dividido en dos componentes: un backend desarrollado con Flask y un frontend desarrollado con React.

## Estructura del Proyecto

```plaintext
/backend
├── assets/
│   ├── bert/
│   ├── flan/
│   └── preguntas_respuestas.csv
├── requirements.txt
├── server.py
└── .env

/frontend
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── assets/
│   ├── components/
│   ├── pages/
│   ├── App.jsx
│   └── index.jsx
├── .env
├── package.json
└── README.md
```

## Requisitos Previos

- Python 3.x
- Node.js y npm
- Un entorno virtual para Python (`venv`)
- Claves API de DeepL para la traducción de texto

## Instalación

### Backend

1. Clona este repositorio:

    ```bash
    git clone https://github.com/Alexander-Guacan/chatbot_espe.git
    cd chatbot_espe/backend
    ```

2. Crea y activa un entorno virtual llamado chatbot_env:

    ```bash
    python -m venv chatbot_env
    chatbot_env/Scripts/activate
    ```

3. Instala torch manualmente

    ```bash
    pip install torch==2.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
    ```

4. Instala las dependencias faltantes:

    ```bash
    pip install -r requirements.txt
    ```

5. [Descarga](https://drive.google.com/file/d/1-9KvZ7fpScM63DiKiQcGAv-dWsV6voxl/view?usp=drive_link) el modelo fine-tuning y extraelo en la siguiente ruta

    ```bash
    /chatbot_espe/backend/assets/flan/
    ```

6. Descarga el modelo spaCy

    ```bash
    python -m spacy download es_core_news_sm
    ```

7. Crea un archivo .env en la carpeta backend con la API Key de DeepL:

    ```plaintext
    DEEPL_API_KEY=tu_api_key_deepl
    ```

8. Ejecuta el servidor Flask:

    ```bash
    python server.py
    ```

### Frontend

1. Navega a la carpeta frontend:

    ```bash
    cd ../frontend
    ```

2. Instala las dependencias del frontend:

    ```bash
    npm install
    ```

3. Crea un archivo .env en la carpeta frontend con la dirección del backend:

    ```plaintext
    VITE_API_ADDRESS=http://localhost:8000  # Ajusta la URL si tu backend está en otra dirección
    ```

4. Inicia la aplicación React:

    ```bash
    npm run dev
    ```

## Uso
Con ambos servidores (backend y frontend) corriendo, puedes acceder al chatbot a través de tu navegador en http://localhost:5173 (o el puerto que esté usando React).
