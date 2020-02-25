import Calculator

c = Calculator.Calculator(10)
print("Calculator, type something (q = quit):")
while True:
    s = input()
    if (s == "q"):
        print("bye-bye")
        break

    r = c.process(s)
    print(r)