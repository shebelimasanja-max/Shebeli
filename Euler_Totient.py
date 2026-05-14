numlistA=[]
numlistB=[]
Finallist=[]
number=int(input("Enter The Number: "))
for i in range(1,number):
    if number%i!=0: # proceed only with numbers which are not factors of a number
        k=2
        while k<=i: # loop from 2 to the non factor of a number
            for j in range(2,i+1): 
                if i%j==0 and number%j==0:
                    break
            else:
                Finallist.append(i)
            k+=1
Finallist.insert(0,1)
Finallist=set(Finallist)
print(f"Number of coprime to {number} is {len(Finallist)}")
print(f"Coprime Numbers are: ")
for m in Finallist: # Extracting numbers from the set
    print(m)
