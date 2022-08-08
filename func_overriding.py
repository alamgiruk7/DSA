# def funret(num):
#     if num == 0:
#         return print

#     if num == 1:
#         return sum

# print(funret(0))


# def executor(func):
#     func("Hi")


# executor(print)


def dec1(func1):
    def now_exec():
        print("Executing Now...")
        func1()
        print("Executed!")

    return now_exec

@dec1
def greet():
    print("Hello People")


greet()