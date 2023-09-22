from csv import *
with open("c:\\sqlite\\result.csv",'r') as file_read:
    data = reader(file_read)
    file_data = []
    data_header = next(data)
    data_header.append("Total Marks")
    data_header.append("Percentage")
    file_data.append(data_header)
    for i in data:
        if len(i)==7:
            if len(i)!=0:
                total = sum(int(i) for i in i[2:])
                i.append(total)
                i.append(total/5)
                file_data.append(i)

if len(file_data)!=1:
    with open("c:\\sqlite\\result.csv",'w',newline="") as file_write:
        file_write_data = writer(file_write)
        file_write_data.writerows(file_data)

with open("c:\\sqlite\\result.csv",'r') as file_read:
    file_read_data =  reader(file_read)
    for i in file_read_data:
        print(i)
