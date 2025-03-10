import numpy as np

def binary_search_guess(number: int = None) -> int:
    """Функция угадывания числа методом бинарного поиска."""
    if number is None:
        number = np.random.randint(1, 101)
    
    low, high = 1, 100
    count = 0
    
    while True:
        count += 1
        predict = (low + high) // 2  # Бинарный поиск
        
        if predict == number:
            return count  # Возвращаем количество попыток
        elif predict > number:
            high = predict - 1
        else:
            low = predict + 1

# Проверяем работу алгоритма
if __name__ == "__main__":
    np.random.seed(1)  # Фиксируем seed для воспроизводимости
    attempts = [binary_search_guess(np.random.randint(1, 101)) for _ in range(1000)]
    print(f"Среднее количество попыток: {np.mean(attempts)}")
