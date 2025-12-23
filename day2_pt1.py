file_path = 'data.txt'
data_list_tmp = []
data_list = []

with open(file_path, 'r') as file:
    for line in file:
        row = line.split(',')
        data_list_tmp = row
    for element in row:
        dash_num = element.split('-')
        data_list.append(dash_num)

print(data_list) # type -> [[str]]

numbers_worked = []
for element in data_list:
    beg = int(element[0])
    end = int(element[1])
    for i in range(beg, end+1, 1):
        # print("number is ", i)
        length = len(str(i))
        # print("length is ", length)
        middle = length//2
        # print("middle is ", middle)
        # print("left half is ", str(i)[:middle])
        # print("right half is ", str(i)[middle:])
        if str(i)[:middle] == str(i)[middle:]:
            print("works for nums: ", i)
            numbers_worked.append(i)
            
print(sum(numbers_worked))


