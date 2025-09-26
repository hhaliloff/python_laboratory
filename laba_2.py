
def user_input() -> list:
    """функция принимает значения с клавиатуры и возвращает их"""
    user = []
    print("Введите загаданное число:")
    user.append(int(input()))
    print("Введите нижнюю границу:")
    user.append(int(input()))
    print("Введите верхнюю границу:")
    user.append(int(input()))
    return user

def getlist(userex) -> list:
    """получает на вход верхнюю и нижнюю границу и возвращает полный список чисел в диапазоне

    > getlist(-3, 7)
    [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
    """
    listex = []
    list2ex = []
    list2ex.append(userex[0])
    lower = userex[1]
    higher = userex[2]
    for i in range(lower, higher + 1):
        listex.append(i)
    list2ex.append(listex)
    return list2ex


def findnum(listex) -> str:
    """основная функция
    проводит бинарный поиск и угадывает число за минимально возможное количество попыток

    > findnum([0, 0, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    Попробую:5
    Попробую:2
    Попробую:1
    Попробую:0
    Это число: 0
    Количество попыток: 4
    """
    k = 0
    x = listex[0]
    list1 = listex[1]
    while len(list1) != 0:
        k = k + 1
        ind = len(list1)//2
        print("Попробую:" + str(list1[ind]))
        if list1[ind] == x:
            print("количество попыток: " + str(k))
            return "Это число: " + str(x)
        elif list1[ind] < x:
            list1 = list1[ind:]
        elif list1[ind] > x:
            list1 = list1[:ind]

#userex = user_input()
#listex = getlist(userex)
#print(findnum(listex))
