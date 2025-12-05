import functools
import io
import sys
import logging
import requests

io_log = io.StringIO()



quad_log = logging.getLogger("quadratic")
quad_log.setLevel(logging.INFO)

quad_log.handlers.clear()
quad_log.propagate = False

io_file = io.StringIO()
quad_handler = logging.StreamHandler(io_file)
quad_formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
quad_handler.setFormatter(quad_formatter)
quad_log.addHandler(quad_handler)



file_logger = logging.getLogger("currency_file")
file_logger.setLevel(logging.INFO)
file_logger.handlers.clear()

file_handler = logging.FileHandler("currency.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

file_logger.addHandler(file_handler)


def logger(func=None, *, handle=sys.stdout):
    """
    параметризуемый логгер выполняющий логгирование обычным потоком вывода
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            is_stdout = hasattr(handle, "write")
            if is_stdout:
                try:
                    handle.write(f"INFO: starting function {func.__name__} with arguments {args} {kwargs}\n")
                    result = func(*args, **kwargs)
                    handle.write(f"INFO: successfully finished function with result {result}\n")
                    return result
                except Exception as e:
                    handle.write(f"Error: {type(e).__name__} {e}\n")
                    raise
            else:
                try:
                    handle.info(f"starting function {func.__name__} with arguments {args} {kwargs}")
                    result = func(*args, **kwargs)
                    handle.info(f"successfully finished function with result {result}")
                    return result
                except Exception as e:
                    handle.error(f"ERROR: {type(e).__name__} {e}", exc_info=True)

                    raise

        return wrapper

    if func is None:
        return decorator
    else:
        return decorator(func)

@logger(handle=file_logger)
def get_currencies(currency_codes: list, url="https://www.cbr-xml-daily.ru/daily_json.js") -> dict:
    """
    функция принимает на вход список из имен валют
    и возвращает словарь с ключами - именами валют содержимыми - курсом к рублю

    пример:
    ["USD", "JPY", "AZN", "EUR"]
    >> {'USD': 78.2503, 'JPY': 50.2023, 'AZN': 46.0296, 'EUR': 90.788}
    """
    request = requests.get(url)
    values = {}
    try:
        data = request.json()
        for currency in currency_codes:
            values[currency] = data["Valute"][currency]["Value"]
    except Exception as e:
        raise

    return values

@logger(handle=io_file)
def solve_quadratic(a, b, c):
    if not((isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)) and (isinstance(c, int) or isinstance(c, float))):
        quad_log.error("Введите числовые значения для коэффициентов a, b и c")
        raise TypeError("Коэффициенты должны быть числами")
    if a == b == 0:
        quad_log.critical("Коэффициенты a и b не могут быть равны нулю одновременно")
        raise ValueError("Некорректное уравнение")
    D = b**2 - 4*a*c
    if D<0:
        quad_log.warning("Дискриминант меньше нуля, корней нет")
        raise ValueError("Нет вещественных корней")
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    quad_log.info(f"x1 = {x1}")
    quad_log.info(f"x2 = {x2}")
    return x1, x2

a = get_currencies(["USD", "JPY", "AZN", "EUR"])







