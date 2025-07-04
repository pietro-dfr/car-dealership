from entities import Car, Registrations as Rt
from datetime import datetime

def main() -> None:
    actual_year: int = datetime.now().year
    max_market_value: float = 500_000
    min_market_value: float = 6_000
    min_manufactured_year: int = 1973
    while True:
        print(Rt.menu(), end="")
        try:
            option: int = int(input())
        except ValueError:
            print("Insira apenas números inteiros!")
            continue
        match option:
            case 1:
                print("==================")
                print("REGISTRO DE CARROS")
                print("==================")
                model: str = input("MODELO: ")
                brand: str = input("MARCA: ")
                year: int = ask_year_input()
                market_value: float = ask_market_value_input()

                #talvez podia ser uma funcao ja que os 2 if faz a mesma coisa, mas fds
                error: bool = False
                if not min_manufactured_year <= year <= actual_year:
                    print(f"Você só pode registrar carros entre {min_manufactured_year} e {actual_year}!")
                    #é uma concessionaria nao museu, nao vendemos fusca
                    error = True
                if not min_market_value <= market_value <= max_market_value:
                    print(f"Você só pode registrar carros entre R${min_market_value:,.2f} e R${max_market_value:,.2f}!")
                    error = True
                if error:
                    continue



                #adiciona o carro registrado a lista
                Rt.add_car(Car(model, brand, year, market_value))

            case 2:
                if Rt.is_car_list_empty():
                    print("A lista de carros registrados está vazia!")
                    continue
                print(Rt.get_registrations())

            case 3:
                print(f"FUNCIONA {option}")

            case 4:
                print("Tchau.")
                break

            case _:
                print(f"Opção inválida!")
#end-main

def ask_year_input() -> int:
    year: int = 0
    while True:
        try:
            year = int(input("ANO: "))
        except ValueError:
            print("Insira apenas números inteiros!")
            continue
        # end-try
        break
    # end-while
    return year
#enf-def

def ask_market_value_input() -> float:
    market_value: float = 0.0
    while True:
        try:
            market_value = int(input("VALOR: R$"))
        except ValueError:
            print("Insira apenas números reais!")
            continue
        # end-try
        break
    # end-while
    return market_value
#end-def

if __name__ == "__main__":
    main()
