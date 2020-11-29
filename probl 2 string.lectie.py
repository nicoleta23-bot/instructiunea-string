c=input("Dati cuvantul: ")
l=input("Dati litera: ")
for i in range(len(c)):
    print(c[:i]+l+c[i+1:])