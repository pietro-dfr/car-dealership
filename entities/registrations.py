from entities import Car

class Registrations:
    __car_list: list[Car] = []
    __menu: str = (
        "====================\n" +
        "   MENU PRINCIPAL   \n" +
        "====================\n" +
        "| [1]. Registrar    |\n" +
        "| [2]. Listar       |\n" +
        "| [3]. Vender       |\n" +
        "| [4]. Sair         |\n" +
        "====================\n" +
        ">> "
    )
    @classmethod
    def add_car(cls, some_car: Car) -> None:
        cls.__car_list.append(some_car)

    @classmethod
    def remove_car(cls, index: int) -> None:
        cls.__car_list.pop(index)

    @classmethod
    def get_registrations(cls):
        print("=============================")
        print("INDEX   MODEL   BRAND   YEAR   VALUE")
        for index, item in enumerate(cls.__car_list, start=1):
            print(f"{index}   {item.model}   {item.brand} {item.year_of_manufacture} {item.market_value}")
        #end-for
        print("=============================")

    @classmethod
    def is_car_list_empty(cls) -> bool:
        return bool(cls.__car_list)

    @classmethod
    def menu(cls):
        return cls.__menu

