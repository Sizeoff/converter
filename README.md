API конвертации валют

Нужно написать веб-сервис на django, который предоставляет API для конвертации валют.

Данные хранить в Postgresql. Все явно неописанные форматы и протоколы можно допридумать.

Должны работать следующие локейшены:

GET /convert?from=RUR&to=USD&amount=42: перевести amount из валюты from в валюту to. Ответ в JSON.

POST /database?merge=1: залить данные по валютам в хранилище. Если merge == 0, то старые данные инвалидируются. 

