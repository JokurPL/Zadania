import time

liczby = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 18, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def czyPierwsza(numbers:list):
    startTime = time.time()
    for number in numbers:
        if number == 2:
            print("TAK")
        elif number % 2 == 0 or number <= 1:
            print("NIE")
        else: 
            print("TAK")
    endTime = time.time()
    return f"Operacja zajela: {endTime - startTime}"
        

print(czyPierwsza(liczby))