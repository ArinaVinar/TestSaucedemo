# TestSaucedemo

# Saucedemo E2E UI Test

## Описание
Автоматизированный тест, проходящий путь пользователя на сайте [saucedemo.com](https://www.saucedemo.com) — от логина до завершения покупки.

## Что делает тест

1. Заходит на сайт
2. Авторизуется под пользователем `standard_user`
3. Добавляет товар "Sauce Labs Backpack" в корзину
4. Переходит в корзину и начинает оформление
5. Заполняет форму (имя, фамилия, индекс)
6. Завершает покупку
7. Проверяет сообщение `Thank you for your order!`

## Установка

Клонируйте репозиторий (или скачайте файлы)

```bash
git clone https://github.com/ArinaVinar/TestSaucedemo.git
cd TestSaucedemo
```

1. Установите Python 3.7+
2. Установите зависимости:

```bash
pip install pytest selenium
```
## Запуск

```bash
pytest test.py -v
```

