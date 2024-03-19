def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорійності до вартості від найбільшого до найменшого
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    total_calories = 0
    selected_items = []

    for item, values in sorted_items:
        if budget >= values["cost"]:
            budget -= values["cost"]
            total_calories += values["calories"]
            selected_items.append(item)

    return selected_items, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    costs = [items[item]["cost"] for item in item_names]
    calories = [items[item]["calories"] for item in item_names]

    # Створення таблиці для зберігання максимальної калорійності, яку можна отримати при кожному бюджеті
    dp = [[0 for x in range(budget + 1)] for y in range(n + 1)]

    # Заповнення таблиці
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(
                    calories[i - 1] + dp[i - 1][w - costs[i - 1]], dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлення списку вибраних страв
    w = budget
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= costs[i - 1]

    selected_items.reverse()

    return selected_items, dp[n][budget]


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dynamic_result = dynamic_programming(items, budget)
    print(greedy_algorithm(items, budget))
    print(dynamic_programming(items, budget))
