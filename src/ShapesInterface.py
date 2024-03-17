from typing import Protocol
from abc import abstractmethod


class Shape(Protocol):
    @abstractmethod
    def square(self) -> float:
        raise NotImplementedError
