from Reading_File import ReadingFile
from mysort_bubble import bubble_sort
from Writing import write_file_json
from Writing import write_file_after_deserialization
import timeit

"""
with open("Нашjson.json") as myfile:
    print(myfile.read())
"""
myfile = ReadingFile("Valid_data.txt")
norm_text = myfile.get_data_without_json()

print("Выберите по какому полю отсортировать записи")
menu = {
    1: 'Снилс',
    2: 'Паспорт',
    3: 'Возраст',
    4: 'Вес',
}
check = True
while check:
    for key in menu.keys():
        print(key, ':', menu[key])
    name_field = ''
    try:
        option = int(input('Enter your choice: '))
    except BaseException:
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

write_file_json(norm_text, "Нашjson")
myfile = ReadingFile(r"C:\Users\andre\PycharmProjects\Lr_3\Нашjson.json")
norm_text = myfile.get_data_json()
write_file_after_deserialization(norm_text, "deserialized_file")
