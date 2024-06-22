# function to check if expression equals 0
def check_expression(a, b, c):
    for x in [-1, 1]:
        for y in [-1, 1]:
            for z in [-1, 1]:
                if (a*x + b*y + c*z) == 0:
                    return "YES"
    return "NO"

# input number of test cases
t = int(input())

# loop through test cases
for i in range(t):
    # input a, b, c for each test case
    a, b, c = map(int, input().split())

    # check if expression equals 0 and print result
    print(check_expression(a, b, c))
