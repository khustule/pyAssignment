##its a faulty calculator for finding cheaters during exam if student used this calculator in exam thair some questions answer will be change
## some calculation which ask in exam if this que. solve using this calculator their answer will be wrong
## 49+7 and 99/16 and 55*7 .


print("Operater are: +,-,*,/")
print("if you want to terminate then write break")

while(1):
    s=input("plz select operater:-")
    if(s=="+" or s=="-" or s=="*" or s=="/"):
        a=int(input("enter your first no."))
        b=int(input("enter your second no."))
        if(s=="+"):
            if(a==49 and b==7):
                print(855)
            else:
                print(a+b)
        elif(s=="-"):
            print(a-b)
        elif(s=="/"):
            if(a==99 and 16):
                print(52)
            else:
                print(a/b)
        elif(s=="*"):
            if(a==55 and b==7):
                print(444)
            else:
                print(a*b)
    elif(s=="break"):
            break




