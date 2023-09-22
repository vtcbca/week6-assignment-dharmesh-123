from csv import *
with open("c:\\sqlite\\result.csv",'r') as file_read:
    file_data = DictReader(file_read)
    file_header = next(file_data)
    file_record = list(file_data)
    file_record.sort(key= lambda x : x["Total Marks"] , reverse =True)
    count = 0
    print("STUDENT ID\tSTUDENT NAME\tPERCENTAGE")
    for i in file_record:
        if count <3:
            print(i['Student_ID'],"\t\t",i['Student_Name'],"\t\t",i['Percentage'])
            count += 1
