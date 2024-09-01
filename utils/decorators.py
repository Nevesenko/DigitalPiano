import logging
import time


def add_logger(func):
    def wrapper(*args, **kwargs):
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            # TODO: Закомментированный код всегда должен иметь указание на то, когда его нужно будет раскомментировать
            # TODO: Если он оставлен для истории - тогда его нужно удалить, потому что историю и так хранит git
            # ,filename='data/app.log',# Запись логов в файл
            # filemode='w'# Перезапись файла при каждом запуске программы
        )
        res = func(*args, **kwargs)

        return res

    return wrapper


def add_time_logger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        finish = time.time()
        logging.debug(f"Время работы функции: {finish - start}")
        return res

    return wrapper
