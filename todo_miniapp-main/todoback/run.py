import asyncio
import uvicorn
from bot import main as bot_main

async def run_app():
    # Запускаем сервер FastAPI в отдельном процессе
    server = asyncio.create_task(
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=8000,
            reload=True
        )
    )
    
    # Запускаем бота
    bot = asyncio.create_task(bot_main())
    
    # Ждем завершения задач
    await asyncio.gather(server, bot)

if __name__ == "__main__":
    asyncio.run(run_app()) 