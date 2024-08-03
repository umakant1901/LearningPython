
# ----------- example 1 ----------- without parameter

def movieName():
    print("300")


# movieName()
# ----------- example 2 ----------- with parameter


def isValidAgeToDrive(name, age, minage):
    if age >= minage:
        print(f"{name} age is {age} and allow to drive")
    else:
        print(f"{name} age is {age} and is not allow to drive")


# isValidAgeToDrive("Sachin", 30, 21)
# isValidAgeToDrive("Abhijeet", 27, 21)
# isValidAgeToDrive("Pari", 10, 21)
# isValidAgeToDrive("Saurabh", 21, 21)


# ----------- example 3 ----------- return type
def userSatus(name, status):
    return f"{name} is {status}"


print(userSatus("Sachin", "online"))


# ----------- example 4 ----------- Keyword driven
# print(userSatus(name="Hari", status="offline"))

# ----------- example 5 ----------- required and optional parameter
# optional parameter should be last
# optional parameter have default value


def subs(x, y, z=10):
    return x-y-z


# print(subs(100, 30))
# print(subs(100, 30, 20))

# ----------- example 6 ----------- Non-keyword argument
# when we don't know how many argument user will provide.
# it is kind of tuple


def nums(*numbers):
    return numbers


# print(nums(2, 3, 5, 10))

# ----------- Example 7 -------


def subs(*nums):
    n1 = 1000
    for x in nums:
        n1 = n1-x
        print(n1)
    return n1


# print(subs(2, 3, 5, 10, 20, 30, -20))

# ----------- example 8 ----------- keyword argument
# when we don't know how many argument user will provide.
# it is kind of dictionary

def taskStatus(**statusOf):
    return statusOf


status = taskStatus(musin="Not Started", exercise="Pending", office="Done")
print(status)
