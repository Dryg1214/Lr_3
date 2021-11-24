from Reading_File import ReadingFile

myfile = ReadingFile(r"C:\Users\andre\Desktop\Valid_data.txt")
norm_text = myfile.get_data_without_json()
for i in norm_text:
    print(i)
    print(i["weight"])
