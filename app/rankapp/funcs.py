import numpy as np  # Подключение библиотеки для мат. вычислений


def rank(cols, rows, args):  # Создание функции с тремя переменными (столбцы, строки, аргументы в матрице)
    try:  # используем функцию try/except для проработки ошибок в вводе
        rows = int(rows)  # Ввод кол-ва строк типа integer
        if rows < 1:  # Проверка на то, что введено число больше или равное единце
            return "EROR! Please correct your ROWS! Please enter a number greater than zero!"
    except Exception as e:  # Проверка на то, что введено число
        return "EROR! Please correct your ROWS! Type doesn't match!"

    try:
        cols = int(cols)  # Ввод кол-ва столбцов типа integer
        if cols < 1:  # Проверка на то, что введено число большее или равное единце
            return "EROR! Please correct your COLS! Please enter a number greater than zero!"
    except Exception as e:  # Проверка на то, что введено число
        return "EROR! Please correct your COLS! Type doesn't match!"

    matrix = []  # Создаём пустую переменную matrix, типа массив

    try:
        args = [int(x) for x in args.split('_')]  # Проверка на то, что введены числа корректно, через "_"
    except Exception as e:
        return "EROR! Please correct your ARGS! Type doesn't match!"

    if len(args) != cols * rows:  # Проверка на кол-во введённых аргументов
        return "EROR! Please correct your ARGS! Amount doesn't match!"

    for i in range(int(rows)):  # Приведение вида массива в вид матрицы
        matrix.append(args[i * cols:(i + 1) * cols])
        # print(matrix[i])  # Печать в терминал

    return np.linalg.matrix_rank(np.array(matrix)) # Вывод Ранга Матрицы


# http://127.0.0.1:8000/rank?cols=3&rows=2&args=2_5_6_-8_9_2 пример запроса
# http://127.0.0.1:8000/api/3/3/1_2_3_4_5_6_7_8_9_1 пример запроса в api
# http://127.0.0.1:8000/docs/

# for i in range(int(rows)):  # распредилить массивы на малые массивы для создания матрицы
#     try:
#         matrix.append(args[i * cols:(i + 1) * cols])
#         print(matrix[i])
#     except Exception as e:
#         return "Ошибка ввода! Проверьте введенные значения!"
# return np.linalg.matrix_rank(matrix)
# return np.array(matrix)

