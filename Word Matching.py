str_list = ['Bat','Cat','Dog','Monkey','Car','Cab']
count = 0
print(str_list)
for i in str_list:
    if len(i)>2:
        count+=1
        print(i[0])
        print(i[-1])
        print('-----')
print('The number of strings with more than 2 letters are',count)
