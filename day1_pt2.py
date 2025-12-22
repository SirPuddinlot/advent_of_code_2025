file_path = 'data.txt'
data_list = []

with open(file_path, 'r') as file:
    for line in file:
        row = line.strip()
        data_list.append(row)

print(data_list) # type -> [[str]]

zero_count = 0
pointer = 50 # start here
for element in data_list:
    print("current pointer is ", pointer)
    direction = element[0]
    number = int(element[1:])
    print("dir is", direction)
    print("number is", number)
    if direction == "L":
        for _ in range(number):
            pointer -= 1 
            if pointer < 0:
                pointer = 99
            if pointer == 0:
                zero_count += 1
    elif direction == "R":
        for _ in range(number):
            pointer += 1 
            if pointer >= 100:
                pointer = 0
            if pointer == 0:
                zero_count += 1
    else:
        print("somethings wrong")
        
print("current pointer is ", pointer)
print("passwd is", zero_count)
            
        
