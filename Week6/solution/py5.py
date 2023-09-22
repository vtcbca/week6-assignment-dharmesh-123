with open('Python.txt','r') as file_read,\
     open('Python_upper.txt','w+') as file_write:
    file_data = file_read.read()
    file_write_data = file_data.upper()
    file_write.writelines(file_write_data)

with open('Python_upper.txt','r') as file_read:
    file_data = file_read.read()
    print(file_data)
