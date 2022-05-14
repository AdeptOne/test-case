# test-case
test task for ITeritory

## Процесс развертывания

### 1. Создание вируально окружения

`python -m venv your_virtual_enviroment_name`

`python -m pip install -r requirements.txt`

### 2. Активация виртуального окружения

На Linux: `source your_virtual_enviroment_name/bin/activate`\
На windows: `path_to_your_virtual_enviroment\Scripts\activate`

### 3. Установка зависимостей 

`python -m pip install -r requirements.txt`

### 4. Создание миграций в базу данных

`python manage.py migrate`


### 5. Запуск сервера

`python manage.py runserver`
