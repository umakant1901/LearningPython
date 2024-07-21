
# v1 = 2
# v2 = 3
# v3 = 2

# print("id of v1 is : ", id(v1))
# print("id of v2 is : ", id(v2))
# print("id of v3 is : ", id(v3))

# v2 = v2-1
# print("id of v2 is : ", id(v2))


# user_name = input("Enter you name : ")
# print(user_name)

# number = input("Enter a Number : ")
# sum = int(number)+10
# print(sum)
# print(type(sum))


def printMessage():
    print("here is the message...!")


message = None
message = printMessage
print(id(message))
print(id(printMessage))
print(message())
print(printMessage())

printMessage()
