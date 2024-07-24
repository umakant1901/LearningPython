# case 1
# num1 = 1001
# num2 = 200


# if (num1 > num2):
#     print(f"{num1} is greater than {num2}")
# else:
#     print(f"{num1} is less than {num2}")

# case 2 : multiple condition check
temp = -10

if temp >= 45:
    print("Too Hot")
elif temp < 45 and temp >= 37:
    print("It's hot")
elif temp < 37 and temp >= 16:
    print("It's cold out side...!")
elif temp < 16 and temp >= 0:
    print("Freezing point is out side...!")
else:
    print("Temp is in minus...!")


grade = 10

# method 1:
if grade >= 7:
    print("Passed")
else:
    print("Failed")

# method 2:
if grade >= 7:
    result = "Passed"
else:
    result = "Failed"

print(result)


# method 3:

test = "Passed" if grade >= 7 else "failed"

print(test)
