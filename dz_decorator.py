def check_division_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("Помилка: Ділення на нуль.")
            raise ZeroDivisionError("Помилка: Ділення на нуль.")
    return wrapper

def check_index_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            print("Помилка: Індекс виходить за межі списку.")
            raise IndexError("Помилка: Індекс виходить за межі списку.")
    return wrapper

@check_division_error
def divide(a, b):
    return a / b

@check_index_error
def get_element(lst, idx):
    return lst[idx]

def run_tests():
    print("Тестування divide(6, 2):", divide(6, 2))
    print("Тестування divide(5, 0):", divide(5, 5))

    test_list = [1, 2, 3, 4]
    print("Тестування get_element([1, 2, 3, 4], 2):", get_element(test_list, 2))
    print("Тестування get_element([1, 2, 3, 4], 5):", get_element(test_list, 2))

run_tests()