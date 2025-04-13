# Todo App Backend

Бэкенд-часть приложения для управления задачами через Telegram WebApp.

## Разработка

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск сервера для разработки
uvicorn main:app --reload
```

## Деплой на Railway

1. Создайте аккаунт на [Railway](https://railway.app/)
2. Подключите ваш GitHub репозиторий
3. Установите переменные окружения:
   - `BOT_TOKEN` = токен вашего Telegram бота
   - `FRONTEND_URL` = URL вашего фронтенда на Netlify
4. Нажмите Deploy

## Деплой на Render

1. Создайте аккаунт на [Render](https://render.com/)
2. Выберите "New Web Service"
3. Подключите ваш репозиторий
4. Установите:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Добавьте переменные окружения:
   - `BOT_TOKEN` = токен вашего Telegram бота
   - `FRONTEND_URL` = URL вашего фронтенда на Netlify
6. Нажмите "Create Web Service"

## Деплой на PythonAnywhere

1. Создайте аккаунт на [PythonAnywhere](https://www.pythonanywhere.com/)
2. Загрузите файлы через Bash Console или Git
3. Настройте Web app через панель управления:
   - Путь к wsgi файлу: `/home/yourusername/todoback/main.py`
   - Выберите версию Python 3.11
4. Настройте переменные окружения в файле `.env`

## После деплоя

1. Получите URL вашего API (например, https://your-app.onrender.com)
2. Обновите URL в файле `config.js` на фронтенде
3. Повторно опубликуйте фронтенд на Netlify 