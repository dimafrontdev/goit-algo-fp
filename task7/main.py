import random
import matplotlib.pyplot as plt


def roll_dice(num_rolls):
    """Симуляція кидків двох кубиків і підрахунок сум."""
    counts = {sum: 0 for sum in range(
        2, 13)}  # Ініціалізація лічильників для кожної можливої суми
    for _ in range(num_rolls):
        # Кидок двох кубиків і обчислення їх суми
        roll = random.randint(1, 6) + random.randint(1, 6)
        counts[roll] += 1
    return counts


def calculate_probabilities(counts, num_rolls):
    """Обчислення ймовірностей для кожної суми."""
    probabilities = {sum: count / num_rolls for sum, count in counts.items()}
    return probabilities


if __name__ == "__main__":
    num_rolls = 1000000  # Кількість кидків
    counts = roll_dice(num_rolls)
    probabilities = calculate_probabilities(counts, num_rolls)

    # Виведення отриманих результатів
    print("Сума\tЙмовірність")
    for sum, probability in probabilities.items():
        print(f"{sum}\t{probability:.2%}")

    # Побудова графіка
    sums = list(probabilities.keys())
    values = list(probabilities.values())

    plt.bar(sums, values, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум при киданні двох кубиків')
    plt.show()
