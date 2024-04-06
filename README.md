# test_parser

Текст [задания](task.md).
Проект для сравнения ставок com и bet версий бк olimp

## Установка

1. Установите зависимости

```bash
pip install -r requirements.txt
```

2. Создайте файл `.env` по [примеру](env_example)

```bash
touch .env
```

API_ID и HASH_id - получите с [my.telegram.org](https://my.telegram.org/apps)
PHONE - ваш мобильный, к которуму привязан телеграм
COM_URL - получается при помощи [бота](https://t.me/olimpbet_bot) с командой `/mirror'. Вам нужно активировать бота и не находится на его странице во время запуска скрипта. Запуск скрипта [com_url](com_url.py) перезапишет COM_URL на валидный.

## Использование

Сохранит данные в json файл.

1. Запустить скрипт для получение валидного `url` com версии:

```bash
python3 com_url.py
```

2. Запустить скрипт для получение результатов сравнения ставок:

```bash
python3 main.py
```

## Результат

После завершения скрипта вы увидите сообщение "Matches fetched successfully", а также будет создан файл [bets.log](bets.log) в корне проекта, где вы можете увидеть все результаты.
![изображение](https://github.com/Rikoze777/test_parser/assets/61386361/6d830a84-a660-4e5a-b71d-261c0968df9c)
