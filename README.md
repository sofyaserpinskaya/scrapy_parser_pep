# scrapy_parser_pep - Асинхронный парсер PEP

### Описание:

Парсер выводит собранную информацию о [PEP](https://peps.python.org) в два файла .csv:
1) список всех PEP: номер, название и статус;
2) сводка по статусам PEP — сколько найдено документов в каждом статусе (статус, количество) и общее количество PEP.

### Автор:

pep_parse - [Софья Серпинская](https://github.com/sofyaserpinskaya)

tests - [Яндекс.Практикум](https://github.com/yandex-praktikum)

### Технологии:

Python, Scrapy

### Запуск проекта:

Склонировать проект.
Создать и активировать виртуальное окружение:

```
python -m venv venv
source venv/bin/activate
```

Установить зависимости:

```
(venv) .../scrapy_parser_pep $ pip install -r requirements.txt
```

Запустить парсер:
```
(venv) .../scrapy_parser_pep $ scrapy crawl pep
```

Парсер сохранит данные в файлы .csv в директорию results/ в корне проекта.
