s=input("Introdu prenumele si numele tau: ")
s1=s.split()
if((s1[0]==s1[0].title())and(s1[1]==s1[1].title())):
    print("Corecte")
else:
    print("Gresit")