print("*"*20,"ATM Meachine","*"*20)
amount=int(input("Enter the amount: "))
l=[500,200,100,50,20,10,5,2,1]
c=0
for i in l:
    notes=amount//i
    c=c+notes
    print(f"{i} notes are --> {notes}")
    amount=amount-i*notes
    #or we can use amount=amount%i
    if(c.count(notes)==1):
        l2=[c]
        print(sum(l2))
print(f" Minimum number of notes-->{c}")
