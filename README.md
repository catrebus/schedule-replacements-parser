# Schedule Replacements Parser

Парсер замен занятий для сайта https://kmpo.eljur.ru/ с интеграцией Telegram-бот. Парсер отслеживает только замены 1 группы. Для настройки нужно изменить функцию `extract_text_sync` в файле `/parser/pdf_parser/pdf_data_extractor.py` и добавить название группы в дампе `/mysql/central_db/central_api_db_dump.sql` в таблицу `college_group`.

## Запуск

1. Выполнить в терминале `git clone https://github.com/catrebus/schedule-replacements-parser`;
2. Изменить помеченные переменные в `.env_template` на свои значения;
3. Переименовать файл `.env_template` в `.env`;
4. Выполнить в терминале `docker compose build --no-cache`;
5. Выполнить в терминале `docker compose up -d`.