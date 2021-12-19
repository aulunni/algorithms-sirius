# Комбинации
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# На клавиатуре старых мобильных телефонов каждой цифре соответствовало несколько букв. Примерно так:

# 2:'abc',
# 3:'def',
# 4:'ghi',
# 5:'jkl',
# 6:'mno',
# 7:'pqrs',
# 8:'tuv',
# 9:'wxyz'

# Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов. Напечатайте все комбинации букв, которые можно набрать такой последовательностью нажатий.

# Формат ввода
# На вход подается строка, состоящая из цифр 2-9 включительно. Длина строки не превосходит 10 символов.

# Формат вывода
# Выведите все возможные комбинации букв через пробел.

# 23
# ad ae af bd be bf cd ce cf

# 92
# wa wb wc xa xb xc ya yb yc za zb zc

class Solution():
    def letterCombinations(self, digits):
        phone_digit = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        all_combinations = ['']
        for digit in digits:
            current_combinations = list()
            for letter in phone_digit[digit]:
                for combination in all_combinations:
                    current_combinations.append(combination + letter)
            all_combinations = current_combinations
        return all_combinations

test=Solution()
print(test.letterCombinations('52'))