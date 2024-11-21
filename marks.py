name = input()
marks = int(input())
if(marks>90):
    print(f"{name} have secured 'A' grade")
elif(80<=marks<=89):
    print(f"{name} have secured 'B' grade")
elif(70<=marks<=79):
    print(f"{name} have secured 'c' grade")
elif(60<=marks<=69):
    print(f"{name} have secured 'D' grade")
else:
    print("Fail")