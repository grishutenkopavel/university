from pycbrf.toolbox import ExchangeRates


class Component():

    def getUSDRate(self):
        pass

class ConcreteComponent(Component):
    
    def getUSDRate(self):
        return ExchangeRates('2021-06-26')['USD'].rate


class Decorator(Component):
    
    _component: Component = None

    def __init__(self, component: Component):
        self._component = component

    @property
    def component(self):
        return self._component

    def getUSDRate(self):
        return self._component.getUSDRate()


component = ConcreteComponent()

rate = Decorator(component)

print(rate.getUSDRate())