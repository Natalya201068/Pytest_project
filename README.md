# Pytest_project

### Шаги
1. Склонировать проект `git clone` [ссылка](https://github.com/Natalya201068/Pytest_project.git)
2. Установить зависимости `pip install -r requirements.txt`
3. Добавить в проект файл `.env`. В этот файл поместить СВОИ рабочие proxy в формате `MY_PROXY=http://IP:PORT`
4. Запустить тест `pytest --language=es test_items.py`
5. Добавлять в тестовый файл `sleep` не надо. В тесте реализованы явные ожидания.