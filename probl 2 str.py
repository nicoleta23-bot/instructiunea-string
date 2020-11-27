s=str(input("dati sirul: "))
import string
sm=0
smic=0
sp=0
special_chars=string.punctuation
for i in s:
    if i in string.ascii_uppercase:
        sm=sm+1
    elif ((ord(i)<=57) and (ord(i)>=48)):
        smic=smic+1
    if i in special_chars:
        sp=sp+1

print("Nr de majuscule este  ",sm)
print("Nr de cifre este  ",smic)
print("Nr de caractere speciale este  ",sp)