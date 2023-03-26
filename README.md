Запуск проекта в dev-режиме
Клонировать репозиторий и перейти в него в командной строке.
Установите и активируйте виртуальное окружение c учетом версии Python 3.7 (выбираем python не ниже 3.7):
python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip
Затем нужно установить все зависимости из файла requirements.txt
cd yatube_api
pip install -r requirements.txt
Выполняем миграции:
python manage.py migrate
Создаем суперпользователя:
python manage.py createsuperuser
Запускаем проект:
python manage.py runserver