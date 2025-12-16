# Workplace Booking (demo)

## Инструкция по развертыванию проекта
1. Создать виртуальное окружение
```
python3 -m venv .env
```

2. Активировать вирутальное окружение
```
source .env/bin/activate
```

3. Установить pip-tools
```
py -m pip install pip-tools
```

4. Скомпилировать новый requirements.txt (при необходимости)
```
pip-compile --output-file=- > requirements.txt 
```

5. Установить нужные библиотеки в виртуальное окружение
```
pip install -r requirements.txt
```