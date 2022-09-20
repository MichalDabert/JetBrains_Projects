memory = 0
result = 0


def honestcalculator():
    global memory
    global result


    msgs = ["Enter an equation",
            "Do you even know what numbers are? Stay focused!",
            "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
            "Yeah... division by zero. Smart move...",
            "Do you want to store the result? (y / n):",
            "Do you want to continue calculations? (y / n):",
            " ... lazy",
            " ... very lazy",
            " ... very, very lazy",
            "You are",
            "Are you sure? It is only one digit! (y / n)",
            "Don't be silly! It's just one number! Add to the memory? (y / n)",
            "Last chance! Do you really want to embarrass yourself? (y / n)"]

    print(msgs[0])
    calc = input()
    x, oper, y = calc.split()

    if x == "M":
        x = memory
    if y == "M":
        y = memory


    def is_one_digit(v):
        if 10 > v > -10 and v.is_integer() is True:
            return True
        else:
            return False


    def check(x, y, oper):
        msg = ""
        if is_one_digit(x) and is_one_digit(y):
            msg = msg + msgs[6]
        if (x == 1 or y == 1) and oper == "*":
            msg = msg + msgs[7]
        if (x == 0 or y == 0) and (oper == "*" or oper == "+" or oper == "-"):
            msg = msg + msgs[8]
        if msg != "":
            msg = msgs[9] + msg
        print(msg)


    try:
        x = float(x)
        y = float(y)
    except ValueError:
            print(msgs[1])
            honestcalculator()

    else:
        if oper in ["+","-","*","/"]:
            if oper == "+":
               check(x, y, oper)
               result = (x + y)
            elif oper == "-":
                check(x, y, oper)
                result = (x - y)
            elif oper == "*":
                check(x, y, oper)
                result = (x * y)
            elif oper == "/" and y != 0:
                check(x, y, oper)
                result = (x / y)
            elif oper == "/" and y == 0:
                check(x, y, oper)
                print(msgs[3]) # div by 0
                honestcalculator()

            print(result)
        else:
            print(msgs[2])
            honestcalculator()




    print(msgs[4]) # Do you want to store the result? (y / n):"
    memans = input()


    if memans == "y":
        if is_one_digit(result):
            msg_index = 10
            while True:
                print(msgs[msg_index])
                sure = input()
                if sure == "y":
                    if msg_index < 12:
                        msg_index = msg_index + 1
                    else:
                        memory = result
                        break
                if sure == "n":
                    break
                else:
                    continue



        if is_one_digit(result) is False:
            memory = result


    elif memans == "n":
        pass


    print(msgs[5]) # "Do you want to continue calculations? (y / n):"
    cont = input()
    if cont == "y":
        honestcalculator()
    else: exit()

honestcalculator()
