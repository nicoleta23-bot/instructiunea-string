c1=str(input("Dati cuvantul : "))
c2=str(input("Dati cuvantul : "))
c3=str(input("Dati cuvantul : "))
c4=str(input("Dati cuvantul : "))
n=len(c4)
if  (len(c1)>=3) and (len(c2)>=3) and (len(c3)>=3) and (len(c4)>=3) :
    cuvant=c1[0:2]+c2[0:1]+c3[0:3]+c4[0:(n//2)]
else:
    print("Cuvantul are mai putin de 3 caractere")    

print(c1)
print(c2)
print(c3)
print(c4)
print(cuvant)