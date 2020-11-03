import time
import sys

class Timer:
    def __init__(self, num_runs=1):
        """ Принимает на вход количество проверок и задаёт начальное значение времени выполнения """
        self.num_runs = num_runs
        self.avg_time = 0
    def __call__(self, func):
        """Создаёт функцию-обертку, считает время выполнения и выдаёт оба результата """
        def func_wrapper(*arg, **argv):
            for _ in range(self.num_runs):
                t0 = time.time()
                func(*arg, **argv)
                t1 = time.time()
                self.avg_time += (t1 - t0)
            self.avg_time /= self.num_runs
            print("Выполнение заняло %.10f секунд\n" % self.avg_time)
            return func(*arg, **argv)
        return func_wrapper
    def __enter__(self):
        return self
    def __exit__(self, *arg):
        return self

#Тест
with Timer(num_runs=10) as fi:
    @fi
    def fibonachi():
        a = 0
        b = 1
        s = 0
        while b < 1e100:
            a, b = b, a+b
            s += b
        return s
    print(fibonachi())