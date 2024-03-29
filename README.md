# goit-algo-fp

# Завдання 7. Аналіз результатів симуляції кидків кубиків

## Мета
Мета даної симуляції полягала в імітації великої кількості кидків двох ігрових кубиків для визначення ймовірності кожної можливої суми чисел, що випадають на кубиках.

## Методологія
Для імітації було виконано 1,000,000 кидків двох кубиків. Для кожного кидка було обчислено суму чисел на обох кубиках. На основі отриманих даних було підраховано, скільки разів кожна можлива сума (від 2 до 12) з’являлася у процесі симуляції, та обчислено відповідні ймовірності.

## Результати
Отримані результати симуляції представлені нижче:

| Сума | Теоретичні  | Монте-Карло |
|------|-------------|-------------|
| 2    | 2.78%       | 2.77%       |
| 3    | 5.56%       | 5.52%       |
| 4    | 8.33%       | 8.28%       |
| 5    | 11.11%      | 11.14%      |
| 6    | 13.89%      | 13.87%      |
| 7    | 16.67%      | 16.70%      |
| 8    | 13.89%      | 13.88%      |
| 9    | 11.11%      | 11.10%      |
| 10   | 8.33%       | 8.40%       |
| 11   | 5.56%       | 5.55%       |
| 12   | 2.78%       | 2.77%       |

## Аналіз
Порівняння результатів симуляції з теоретичними розрахунками показує високу збігаємість. Теоретичні ймовірності для сум чисел на двох кубиках варіюються від 2.78% до 16.67%, залежно від суми. Результати, отримані за допомогою методу Монте-Карло, майже ідентичні до теоретичних розрахунків, що демонструє точність і валідність методу Монте-Карло для подібного роду симуляцій.

## Висновок
Симуляція підтвердила, що ймовірності сум чисел при киданні двох кубиків розподілені відповідно до теоретичних розрахунків. Метод Монте-Карло виявився ефективним інструментом для аналізу ймовірностей в іграх на кидання кубиків.
