from Reading_File import ReadingFile
from mysort_bubble import bubble_sort
import timeit

myfile = ReadingFile(r"C:\Users\andre\Desktop\Valid_data.txt")
norm_text = myfile.get_data_without_json()

print("Выберите по какому полю отсортировать записи")
menu = {
    1: 'Снилс',
    2: 'Паспорт',
    3: 'Возраст',
    4: 'Вес',
}
check = True
while(check):
        for key in menu.keys():
            print(key, ':', menu[key])
        name_field = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Надо число')
        if option == 1:
           name_field = "snils"
           check = False
        elif option == 2:
           name_field = 'passport_number'
           check = False
        elif option == 3:
            name_field = "age"
            check = False
        elif option == 4:
            name_field = "weight"
            check = False
        else:
            print("Что то пошло не по плану")

start_time = timeit.default_timer()
bubble_sort(norm_text, name_field)
t = timeit.default_timer() - start_time
print("Вы потратили " + str(t) + " секунд жизни впустую")
for i in range(10):
    print(norm_text[i])

