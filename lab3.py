import functools
import time

def timed_logged(func):
    @functools.wraps(func)
    
    def tl_f(*args, **kwargs):
        start =  time.perf_counter() 

        try:
            final_res = func(*args, **kwargs)
            
        except Exception as error:
            finish = time.perf_counter() 

            print("Тип исключения:", type(error).__name__)
            print("Сообщение:", error) 
            print("Имя функции:", func.__name__) 
            print("Время выполнения:", round((finish - start) * 1000, 2), "мс") 
            print("Аргументы: args =",args, "kwargs =",kwargs)
            print("Результат:", "ошибка выполнения")
            
            raise 

        finish = time.perf_counter() 

        print("Имя функции:", func.__name__) 
        print("Время выполнения:", round((finish - start) * 1000, 2), "мс") 
        print("Аргументы: args =",args, "kwargs =",kwargs)
        print("Результат:", final_res)

        return final_res
    return tl_f