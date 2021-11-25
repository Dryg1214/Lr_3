from Reading_File import ReadingFile
from mysort_bubble import bubble_sort
from tqdm import tqdm
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
           name_field = 'passport'
           check = False
        elif option == 3:
            name_field = "age"
            check = False
        elif option == 4:
            name_field = "weight"
            check = False
        else:
            print("Что то пошло не по плану")

bubble_sort(norm_text, name_field)
for i in range(5):
    print(norm_text[i])
"""
test_list = []
a = 0
for i in norm_text:
    if a < 10:
        print(i)
        test_list.append(i)
    a += 1
print("AAAAAAAAAAAAAAAAAAAAAAAAAAA")
bubble_sort(test_list, "snils")
for i in test_list:
    print(i["snils"])
    # print(i["age"])
    # print(i["weight"])
"""
