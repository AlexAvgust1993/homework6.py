my_dict = {'Alex': 1993, 'Andre': 1992, 'Vlad': 1995}
print('My_dict:' ,my_dict)
print('My_dict:' ,my_dict['Alex']) # Вывести одино значение, без ключа
my_dict['Sveta'] = 1995 # Добавить в список ключ с значанием
print('My_dict:' ,my_dict)
del my_dict['Andre'] # Уничтожить к х..м, между командой и переменной ПРОБЕЛ
print('My_dict:' ,my_dict)
my_dict.update({'Ira': 1990, # Засунуть несколько
                'Gleb': 1991})
print('My_dict:' ,my_dict)

my_set = {1, 4, 3, 2, 5, 4, 3, 6,'fire', 'water','metal'}
print(my_set)
print(my_set.discard('metal')) # Удалить
print(my_set)
print(my_set.update(['air'], ['earth'])) # Добавить
print(my_set)