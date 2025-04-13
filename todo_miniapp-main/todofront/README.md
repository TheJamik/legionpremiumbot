# Todo App Frontend

Фронтенд-часть приложения для управления задачами через Telegram WebApp.

## Разработка

```
npm install
npm run dev
```

## Деплой на Netlify

1. Форкните этот репозиторий на GitHub
2. Войдите на [Netlify](https://app.netlify.com/)
3. Нажмите "New site from Git"
4. Выберите GitHub и авторизуйтесь
5. Выберите ваш репозиторий с проектом
6. Настройки сборки уже включены в файл netlify.toml
7. Добавьте переменные окружения:
   - `VITE_API_URL` = URL вашего API бэкенда (например, https://your-app.onrender.com/api)
8. Нажмите "Deploy site"

## Настройка для продакшена

После деплоя на Netlify:

1. Получите URL вашего Netlify сайта (например, https://your-app.netlify.app)
2. Обновите URL в настройках бота через переменную окружения `FRONTEND_URL` на бэкенде

## Бэкенд

Бэкенд можно разместить на:
- [Railway](https://railway.app/) - простой деплой через GitHub
- [Render](https://render.com/) - бесплатный тариф для веб-сервисов
- [PythonAnywhere](https://www.pythonanywhere.com/) - специализированный Python хостинг
- [DigitalOcean](https://www.digitalocean.com/) - для более продвинутой конфигурации

Убедитесь, что вы обновили переменные окружения на обоих концах (фронтенд и бэкенд). 