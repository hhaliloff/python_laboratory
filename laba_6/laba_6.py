from laba_3.laba_3 import gen_bin_tree as recursive
from laba_5.laba_5 import gen_bin_tree as nonrecursive
import timeit
import matplotlib.pyplot as plt

def function(func, height):
    return func(2, height, lambda l_r: l_r + 3, lambda r_r: r_r * 2)

def compare_trees(funcre, funcnonre):
    height_data = [i for i in range(1, 15)]
    recursive_time = []
    nonrecursive_time = []
    for n in height_data:
        recursive_time.append(timeit.timeit(lambda: function(funcre, n), number=10))
        nonrecursive_time.append(timeit.timeit(lambda: function(funcnonre, n), number=10))
    return [height_data, recursive_time, nonrecursive_time]

def draw_plot(funcre, funcnonre):
    data_for_plot = compare_trees(funcre, funcnonre)
    height_data = data_for_plot[0]
    recursive_time = data_for_plot[1]
    nonrecursive_time = data_for_plot[2]
    plt.plot(height_data, recursive_time, label='Рекурсивная функция')
    plt.plot(height_data, nonrecursive_time, label='Итеративная функция')
    plt.xlabel('Высота дерева')
    plt.ylabel('Время выполнения (секунды)')
    plt.title("Сравнение времени выполнения рекурсивной и итеративной функций")
    plt.legend()
    plt.show()

draw_plot(recursive, nonrecursive)