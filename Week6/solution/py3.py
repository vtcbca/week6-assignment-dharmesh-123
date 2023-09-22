with open('Python.txt','r') as file_read:
    file_data = file_read.read()
    file_data_list = file_data.split()
    for i in set(file_data_list):
        print(i,end="\t")
    print("\nTotal No Of Unique Word :: {}".format(len(set(file_data_list))))
