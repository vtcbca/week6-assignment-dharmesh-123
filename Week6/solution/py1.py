with open('Python.txt','r') as file_read:
    file_data = file_read.read()
    print(file_data[::-1])
