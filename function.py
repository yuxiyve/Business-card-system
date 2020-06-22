import tools

userwant = tools.screen()
while True:

    if userwant == "1":
        tools.function1()
    elif userwant == "2":
        tools.function2()
    elif userwant == "3":
        tools.function3()
    elif userwant == "0":
        break
    else:
        print("please choose from 1,2,3,0")

    userwant = tools.screen()

tools.function0()
