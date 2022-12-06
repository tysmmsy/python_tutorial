# 引数numはリストまたはタプル型のデータを受け取ることができる
def calc(num):
    sum = 0
    for n in num:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))

# 可変長引数 *numbersは可変長引数になり、任意個の引数を受け取ることができる
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))
print(calc(1, 3, 5, 7, 9))
print(calc())
