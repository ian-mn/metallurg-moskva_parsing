# Парсинг конкурента
![Black](https://img.shields.io/badge/code%20style-black-black)
![Tests](https://github.com/ian-mn/metallurg-moskva_parsing/actions/workflows/tests.yml/badge.svg?branch=main)

## Запуск
1. Создать файл `.env`;
2. Скопировать содержимое файла `.env.sample` в `.env`;
3. `docker-compose build`;
4. `docker-compose up`.

## Структура проекта
1. Парсер написан с использованием Scrapy и BeautifulSoup;
2. Данные о ценах трансформируются и валидируются в модель pydantic;
3. Завалидированные данные записываются в PostgreSQL;
  ![image](https://github.com/ian-mn/metallurg-moskva_parsing/assets/136719108/8ef8210a-cd9f-4bf4-9476-0bbba8cee285)
4. FastAPI с помощью ручки GET api/v1/recent/ выдает пагинированный результат последнего парсинга;
  ![image](https://github.com/ian-mn/metallurg-moskva_parsing/assets/136719108/6b8ca7ea-0ea7-453c-b45b-28fa8db3fffe)
5. Автоматические тесты API настроены в контейнере newman, так же настроены через Github Actions.  
