import functools
import time

def timed_logged(func):
    @functools.wraps(func)

    def tl_f(*args, **kwargs):
        start =  time.perf_counter() 

        try:
            final_res = func(*args, **kwargs)
            finish = time.perf_counter() 
            
        except Exception as error:
            print("Тип исключения:", type(error).__name__)
            print("Сообщение:", error) 

        else:
            print("Имя функции:", func.__name__) 
            print("Время выполнения:", round((finish - start) * 1000, 2), "мс") 
            print("Аргументы: args =",args, "kwargs =",kwargs)
            print("Результат:", final_res)

            return final_res
        return 0
    return tl_f


@timed_logged
def slow_sum(a, b, delay=0.5):
    time.sleep(delay)
    return a + b
slow_sum(1, 2, delay=0.2)