width = 17
height = 12.0

value1 = width // 2
value1_no_floor = width / 2

print(value1, type(value1))

print(f"This is the value without floor division: {value1_no_floor}")

# the // operator in python performs floor division. It rounds down to the nearest whole number

value2 = width / 2.0

print(value2, type(value2))

# value2 automatically becomes type 'float' because divisor was a float


# value3 = 1 + 2 /* 5

# print(value3)

# here python throws an error because there is no such operator
