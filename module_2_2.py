print('Нам необходимы три числа.')
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second == third:
    print("3.(Все введенные числа равны.)")
elif first == second or first == third or third == second:
    print("2.(2 из 3 введённых чисел равны между собой.)")
elif first != second != third:
    print("0.(Ни одно из введенных вами чисел не равно другому.)")