# Два велосипеда
# Все языки	OpenJDK Java 11
# Ограничение времени	0.5 секунд	0.7 секунд
# Ограничение памяти	121Mb	121Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Вася решил накопить денег на два одинаковых велосипеда — себе и сестре. У Васи есть копилка, в которую каждый день он может добавлять деньги (если, конечно, у него есть такая финансовая возможность). В процессе накопления Вася не вынимает деньги из копилки.

# У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке было денег в каждый из дней.

# Ваша задача — по заданной стоимости велосипеда определить

# первый день, в которой Вася смог бы купить один велосипед,
# и первый день, в который Вася смог бы купить два велосипеда.
# Подсказка: решение должно работать за O(log n).

# Формат ввода
# В первой строке дано число дней n, по которым велись наблюдения за Васиными накоплениями. 1 ≤ n ≤ 106.

# В следующей строке записаны n целых неотрицательных чисел. Числа идут в порядке неубывания. Каждое из чисел не превосходит 106.

# В третьей строке записано целое положительное число s — стоимость велосипеда. Это число не превосходит 106.

# Формат вывода
# Нужно вывести два числа — номера дней по условию задачи.

# Если необходимой суммы в копилке не нашлось, нужно вернуть -1 вместо номера дня.


# Пример 1
# 6
# 1 2 4 4 6 8
# 3

# 3 5


# Пример 2
# 6
# 1 2 4 4 4 4
# 3

# 3 -1


# Пример 3
# 6
# 1 2 4 4 4 4
# 10

# -1 -1

def bike(days,array,price, answer = [-1,-1]):
    price_2 =  2*price
    lenth = days - len(array)
    if lenth == 0:
        answer = [-1,-1]
    if days-len(array) == len(array) :
        return answer
    else:
        if array[lenth] - price_2 >= 0 and answer[1] == -1:
            answer[1] = lenth + 1  
            if -1 in answer:
                return bike(days + 1, array, price, answer)
            else:
                return answer
        elif array[lenth] - price >= 0 and answer[0] == -1:
            answer[0] = lenth + 1  
            if -1 in answer:
                return bike(days + 1, array, price, answer)
            else:
                return answer    
        else:
            return bike(days + 1, array, price, answer)



def test(result, expected):
    if result != expected:
        print(f'Ошибка: {result} != {expected}')
    else:
        print('Ok!')

test(bike(6,[1,2,4,4,6,8],3),[3, 5])