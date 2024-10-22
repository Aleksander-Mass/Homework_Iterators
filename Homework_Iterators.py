# Пункты задачи:
# 1. Создать пользовательский класс исключения StepValueError, который наследуется от ValueError.

class StepValueError(ValueError):
    pass
###   Этот класс наследует от ValueError и будет использован для генерации исключений, если значение шага равно 0.

# Шаг 2: Создание класса Iterator
# Теперь опишем класс Iterator, который будет иметь атрибуты start, stop, step, pointer, а также методы __init__, __iter__ и __next__.
#
# В конструкторе (__init__) проверим значение step и при необходимости вызовем исключение StepValueError.
# Метод __iter__ должен сбрасывать указатель (pointer) на начальное значение и возвращать сам объект итератора.
# Метод __next__ должен обновлять значение указателя в зависимости от шага и определять конец итерации в зависимости от знака шага.

class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError("шаг не может быть равен 0")
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
        current_value = self.pointer
        self.pointer += self.step
        return current_value

# 3. Создайте несколько объектов класса Iterator и совершите итерации с ними при помощи цикла for.

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()

# Вывод на консоль:
# Шаг указан неверно
# -5 -4 -3 -2 -1 0 1
# 6 8 10 12 14
# 5 4 3 2 1