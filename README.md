# Discord-бот (администрирование сервера)

> Учебный/личный проект: бот для Discord на Python с модульной архитектурой **cogs**.
> Автор: Бугаев Евгений Валерьевич.

Многофункциональный бот для управления Discord-сервером: верификация участников,
выдача ролей по кнопкам/меню, модерация и служебные команды.

## Возможности
- **Верификация** через модальное окно (`modal-verification`).
- **Роли по кнопкам и выпадающему меню** (`buttons-role`, `select-roles`).
- Модерация: бан/разбан (`ban-unban`), тайм-аут (`timeout`), очистка сообщений (`clear`).
- Служебное: `ping`, вывод аватара (`avatar`), баннер (`banner`), отправка embed-сообщений (`embed`).

## Технологии
- Python 3
- **disnake** (современный форк discord.py)
- Архитектура расширений **cogs**

## Структура
```
main.py            # точка входа: создание бота и загрузка cogs
cogs/
  ├─ avatar.py
  ├─ ban-unban.py
  ├─ banner.py
  ├─ buttons-role.py
  ├─ clear.py
  ├─ embed.py
  ├─ modal-verification.py
  ├─ ping.py
  ├─ select-roles.py
  └─ timeout.py
```

## Запуск
1. `pip install -r requirements.txt`
2. Задать токен в переменной окружения (НЕ храните токен в коде!):
   ```bash
   set DISCORD_TOKEN=ваш_токен        # Windows
   export DISCORD_TOKEN=ваш_токен     # Linux/macOS
   ```
3. `python main.py`

> ⚠️ Токен бота в репозиторий не коммитится.
