# interfaz de reglas
from abc import ABC, abstractmethod

class RuleHandler(ABC):

    @abstractmethod
    def apply(self, invoice, movement, config):
        pass
