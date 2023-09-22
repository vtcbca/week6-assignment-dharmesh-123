with open('Python.txt','r') as file_read:
    file_data = file_read.read()
    data_list = []
    for i in file_data.split():
        data_list.append([len(i),i])
    sorted_list = sorted(data_list,reverse=True)
    largest_word_no = sorted_list[0][0]
    smallest_word_no = sorted_list[len(sorted_list)-1][0]
    for i in sorted_list:
        if i[0] == largest_word_no:
            print('Largest Word  :: {}'.format(i[1]))
        elif i[0] == smallest_word_no:
            print("Smallest Word :: {}".format(i[1]))
    
