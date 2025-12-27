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

#print(data_list) # type -> [[str]]

answer_list = []
for domain in data_list:
    begin = int(domain[0])
    end = int(domain[1])
    for i in range(begin, end+1, 1):
        length = len(str(i)) # get length
        #print("length is ", length)
        number = str(i)
        # generate repeating subsequences and check if its the same as i
        # suppose length is 6 and number is 123123
        # prefix = number[0] * length
        # prefix = number[0] . number[1] * length/2
        # prefix = number[0] . number[1] . number[2] * length/3 
        prefix = ""
        #print("number is  ", i)
        for j in range(length):
            prefix = prefix + number[j]
            #print("prefix ", prefix)
            if length % (j+1) != 0:
                continue
            if length // (j+1) < 2:
                continue
            compare_str = prefix * int(length/(j+1))
            #print("comp string ", compare_str)
            if compare_str == str(i):
               # print("answer is ", compare_str)
                answer_list.append(int(compare_str))
                break
print(sum(answer_list))
