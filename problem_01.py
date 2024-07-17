def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

def get_numbers():
    """
    # numbers = input("Enter numbers separated by spaces: ").split()
    # numbers = [int(num) for num in numbers]
    # return numbers
    """
    ### VALORES PONTO FLUTUANTE E LISTAS VAZIAS CAUSAVAM ERRO COM DIVISAO POR 0
     ## OU TIPO DE DADOS INCORRETOS
    while True:
        try:
            numbers = input("Enter numbers separated by spaces: ").split()
            numbers = [int(num) for num in numbers]
            if not numbers:
                print("Insira pelo menos um número.")
                continue
            return numbers
        except ValueError:
            print("Inválido. Informe apenas números inteiros separados por espaço.")

def main():
    numbers = get_numbers()
    print("Average:", calculate_average(numbers))
    print("Maximum:", find_max(numbers))

if __name__ == "__main__":
    main()