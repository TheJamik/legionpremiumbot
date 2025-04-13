// Конфигурация URL API в зависимости от окружения
const API_URL = import.meta.env.VITE_API_URL 
  ? import.meta.env.VITE_API_URL 
  : process.env.NODE_ENV === 'production'
    ? 'https://your-backend-url.com/api' // Резервный URL для продакшена
    : 'http://localhost:8000/api';       // URL для разработки

export default {
  API_URL
};
