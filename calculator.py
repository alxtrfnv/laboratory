# Функция сложения чисел
def calc(x, y):
    return x+y

print("Выберите действие:")
print("Сложение")

choice = input("Введите номер")

num1 = float(input("Введите первое число"))
num2 = float(input("Введите второе число"))
if choice == '1':
    print("Результат равен: ", calc(num1, num2))
else:
    print("Неправильный выбор действия")
