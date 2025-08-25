# 🛒 Carrito de Compras con Laravel y Vue.js

> Una aplicación web full-stack que implementa un sistema de carrito de compras. El backend está construido con Laravel y expone una API REST, mientras que el frontend es una Single Page Application (SPA) dinámica desarrollada con Vue.js.

![Laravel](https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white)
![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D)
![PHP](https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white)

![Captura de pantalla del carrito de compras en acción](./ruta/a/tu/imagen.png)

## 📝 Descripción

Este proyecto es una demostración de cómo integrar un backend robusto de Laravel con un frontend reactivo de Vue.js para crear una experiencia de usuario fluida y moderna. Los usuarios pueden navegar por un catálogo de productos, agregarlos a su carrito y gestionar su contenido en tiempo real sin necesidad de recargar la página.

## ✨ Características Principales

* **Catálogo de Productos:** Muestra una lista de productos obtenidos desde la base de datos a través de la API.
* **Añadir al Carrito:** Botones para agregar cualquier producto al carrito de compras.
* **Vista del Carrito:** Un componente dinámico que muestra los productos añadidos, cantidades y subtotales.
* **Actualización en Tiempo Real:** Permite modificar la cantidad de productos o eliminarlos del carrito, con actualizaciones instantáneas en la interfaz.
* **API RESTful:** Endpoints bien definidos en Laravel para gestionar la lógica de productos y del carrito.

## 🛠️ Tecnologías Utilizadas

* **Backend:** Laravel
* **Frontend:** Vue.js
* **Base de Datos:** MySQL
* **Comunicación API:** Axios
* **Gestor de Paquetes:** Composer (PHP), NPM (JavaScript)

## ⚙️ Instalación y Puesta en Marcha

Sigue estos pasos para levantar el proyecto en tu entorno de desarrollo local.

```bash
# 1. Clona el repositorio (usa la URL del repo ya renombrado)
git clone [https://github.com/EleazarL/carrito-compras-laravel-vue.git](https://github.com/EleazarL/carrito-compras-laravel-vue.git)

# 2. Navega al directorio
cd carrito-compras-laravel-vue

# 3. Instala las dependencias de PHP
composer install

# 4. Crea y configura tu archivo de entorno
cp .env.example .env
php artisan key:generate

# 5. Edita el archivo .env con tus credenciales de base de datos
# DB_DATABASE=laravel_vue_cart
# DB_USERNAME=root
# DB_PASSWORD=

# 6. Ejecuta las migraciones para crear las tablas en la BD
# (Si tienes seeders para productos, es un buen momento para ejecutarlos)
php artisan migrate --seed

# 7. Instala las dependencias de JavaScript (Vue, Axios, etc.)
npm install

# 8. Compila los archivos de frontend y mantenlos observando cambios
npm run dev

# 9. En otra terminal, inicia el servidor de Laravel
php artisan serve
```

¡Excelente! Ahora puedes acceder a la aplicación desde tu navegador en `http://127.0.0.1:8000`.
