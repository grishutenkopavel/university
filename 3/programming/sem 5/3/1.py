from pycbrf.toolbox import ExchangeRates

# Этот метод используется для проверки однократности обращения к сервисуы
def getOne():
    print("One")
    return ExchangeRates('2021-06-26') 

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    
    _rates = getOne()

    def getUSDRate(self):
        return self._rates['USD'].rate


rate = Singleton()
rate2 = Singleton()

print(rate.getUSDRate())
print(rate2.getUSDRate())
print(rate.getUSDRate())
print(rate2.getUSDRate())