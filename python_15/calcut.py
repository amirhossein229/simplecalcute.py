print("python calculator,just for 2 num and just 4 operation(+-*/)")
while True:
    num1=int(input("num1 plz"))
    opera=input("operation plz(+,/,*,-)")
    num2=int(input("num2 plz"))

    if opera == "-" :
        print("=")
        print(num1 - num2 )
        print("-" * 10)
    elif opera == "+":
        print("=")
        print(num1 + num2)
        print("-" * 10)
    elif opera == "*":
        print("=")
        print(num1 * num2)
        print("-" * 10)
    elif opera == "/":
        print("=")
        print(num1 / num2)
        print("-" * 10)
    else:
        print("syntax error")