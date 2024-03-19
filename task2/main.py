import matplotlib.pyplot as plt
import numpy as np


def draw_tree(x, y, angle, depth, length):
    if depth == 0:
        return

    # Кінцева точка поточної гілки
    x_end = x + np.cos(np.radians(angle)) * length
    y_end = y + np.sin(np.radians(angle)) * length

    # Малюємо гілку
    plt.plot([x, x_end], [y, y_end], "green", lw=1)

    # Рекурсивно малюємо дві нові гілки
    new_length = length * 0.8  # Зменшуємо довжину гілок

    # Права гілка
    draw_tree(x_end, y_end, angle - 45, depth - 1, new_length)
    # Ліва гілка
    draw_tree(x_end, y_end, angle + 45, depth - 1, new_length)


def plot_tree(depth):
    plt.figure(figsize=(10, 8))
    draw_tree(0, 0, 90, depth, 10)
    plt.axis("off")
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    # Встановлюємо рівень рекурсії
    depth = int(input("Введіть рівень рекурсії: "))
    plot_tree(depth)
