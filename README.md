
# 🤖 AI ChatBot Django

> Un chatbot inteligente construido con Django y tecnologías de IA para conversaciones naturales y fluidas.

## ✨ Características

- 🧠 **IA Conversacional**: Respuestas inteligentes y contextuales
- 🌐 **Interfaz Web**: Dashboard moderno y responsive
- ⚡ **Tiempo Real**: Conversaciones en vivo
- 📱 **Mobile Friendly**: Optimizado para dispositivos móviles
- 🔒 **Seguro**: Autenticación y validación de datos

## 🛠️ Tecnologías

- **Backend**: Django, Python
- **Frontend**: HTML5, CSS3, JavaScript
- **Base de Datos**: SQLite/PostgreSQL
- **IA**: ChatterBot/OpenAI API

## ⚙️ Instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/AI-ChatBot-Django.git
   cd AI-ChatBot-Django
   ```

2. **Crea un entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # o
   venv\Scripts\activate     # Windows
   ```

3. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Ejecuta el servidor**
   ```bash
   python manage.py runserver
   ```

6. **Abre tu navegador** en `http://localhost:8000`

## 📝 Uso

1. Accede a la interfaz web
2. Escribe tu mensaje en el chat
3. ¡Disfruta de la conversación con la IA!

```python
# Ejemplo de uso en código
from chat.models import ChatBot

bot = ChatBot()
response = bot.get_response("¡Hola! ¿Cómo estás?")
print(response)
```

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: Amazing Feature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 👤 Autor

**Eleazar Landeta Esteva**
- GitHub: [@EleazarL](https://github.com/EleazarL)
- eleazarlandetae@gmail.com
