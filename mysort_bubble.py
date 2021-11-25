from tqdm import tqdm
# вес паспорт снилс возраст


def bubble_sort(lst: list, name_field: str):
    """Сортировка пузырьком"""
    n = len(lst)
    check = True
    while check:
        check = False
        for i in tqdm(range(n - 1)):
            if lst[i][name_field] > lst[i + 1][name_field]:
                c = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = c
                check = True
