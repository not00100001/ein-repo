num_list = list()

while True:
    new_num = input("Please enter a number: ")
    if new_num == 'done' : break
    float_num = float(new_num)
    num_list.append(float_num)

average = sum(num_list) / len(num_list)

print(round(average, 2))
