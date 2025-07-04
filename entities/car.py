from dataclasses import dataclass

@dataclass
class Car:
    __model: str
    __brand: str
    __year_of_manufacture: int
    __market_value: float
    #getters:
    @property
    def model(self) -> str:
        return self.__model

    @property
    def brand(self) -> str:
        return self.__brand

    @property
    def year_of_manufacture(self) -> int:
        return self.__year_of_manufacture

    @property
    def market_value(self) -> float:
        return self.__market_value