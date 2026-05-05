Результати для алгоритму Кнут-Морріс-Прат:

|  Text Source  |  Scenario  |  Result  |
| :---------    | :--------  | :------  |
|   article_1   |  positive  |   0.141  |
|   article_2   |  positive  |   0.201  |
|   article_1   |  negative  |   0.148  |
|   article_2   |  negative  |   0.220  |


Результати для алгоритму Боєра-Мура:

|  Text Source  |  Scenario  |  Result  |
| :---------    | :--------  | :------  |
|   article_1   |  positive  |   0.084  |
|   article_2   |  positive  |   0.117  |
|   article_1   |  negative  |   0.049  |
|   article_2   |  negative  |   0.064  |


Результати для алгоритму Рабін-Карп:

|  Text Source  |  Scenario  |  Result  |
| :---------    | :--------  | :------  |
|   article_1   |  positive  |   0.305  |
|   article_2   |  positive  |   0.427  |
|   article_1   |  negative  |   0.323  |
|   article_2   |  negative  |   0.462  |


Найкращий алгоритм для пошуку тексту це алгоритм Боєра-Мура, тому що при повному неспівпадінні символа він зсувається відразу на певну кількість елементів, розраховану на підготовчому етапі, що в найкращому випадку гарантує часову складність O(n), що добре видно на негативних сценаріях. 