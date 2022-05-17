print("Kalkulator")
def start():
    x = input("Podaj 1 liczbe: ")
    if x.isdigit() == True:
        x = int(x)
    else:
        print("UPSSS... nie moge wykonać obliczeń na literach")
        start() 
    z = input("podaj znak (+,-,/,*) ")
    if z == "+" or z == "-" or z == "*" or z == "/":   
        y = input("Podaj 2 liczbe: ")
        if y.isdigit() == True:
            y = int(y)
            result(x,z,y)
        else:
            print("UPSSS... nie moge wykonać obliczeń na literach")
            start()
    else:
        print("Takich obliczeń nie potrafię wykonać")
        start()

def result(x,z,y):
    if z == "+":
        print(x,' + ',y,' = ', x + y)
        exit()
    elif z == "-":
        print(x,' - ',y,' = ', x - y)
        exit()
    elif z == "*":
        print(x,' * ',y,' = ', x * y)
        exit()
    elif z == "/":
        print(x,' /',y,' = ', x / y)
        exit()
    else:
        print("UPSSS... coś poszło nie tak, upewnij się że wszystko dobrze wpisałeś")
        start()

start()

