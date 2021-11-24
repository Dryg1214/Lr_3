lst = [188, 3, 7, 10, 9, 16, 17, 1]
# вес паспорт снилс возраст
def bubble_sort(lst, name_field):
    n = len(lst)
    check = True
    while check:
        check = False
        for i in range(n-1):
            if lst[i] > lst[i + 1]:
                c = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = c
                check = True

bubble_sort(lst)
print(lst)
