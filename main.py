from Reading_File import ReadingFile
from mysort_bubble import bubble_sort
myfile = ReadingFile(r"C:\Users\andre\Desktop\Valid_data.txt")
norm_text = myfile.get_data_without_json()
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
