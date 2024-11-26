print("*"*20,"ATM Meachine","*"*20)
amount=int(input("Enter the amount: "))
l=[500,200,100,50,20,10,5,2,1]
c=0
singlenotes=0
for i in l:
    notes=amount//i
    c=c+notes
    print(f"{i} notes are --> {notes}")
    amount=amount-i*notes
    #or we can use amount=amount%i
    if(notes==1):
        singlenotes+=1
print(f" single notes are-->{singlenotes}")
print(f" Minimum number of notes-->{c}")
