def citire_lista():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(float(x))
    return l

def nr_negative(l):
    '''
    Functia afiseaza numerele negative nenule din lista
    param:l=lista
    return:rezultat,lista cu numerele negative nenule din lista initiala
    '''
    rezultat=[]
    for x in l:
        if x<0:
            rezultat.append(x)
    return rezultat

def test_nr_negative():
    assert(nr_negative([1,-2,-3,-4,5,6,0,-8]))==[-2,-3,-4,-8]
    assert(nr_negative([-2,-3,-200,2,3,4,-5]))==[-2,-3,-200,-5]
    assert(nr_negative([-1,-2,-3]))==[-1,-2,-3]
test_nr_negative()

def ultima_cifra(l,n):
    '''
    Afiseaza cel mai mic numar din lista cu ultima cifra data
    param:l=lista,n=cifra de verificat
    return:mini=minimul cu ultima cifra n
    '''
    l1=[]
    mini=999999999
    for x in l:
        if x%10==n:
            l1.append(x)
    for x in l1:
        if x<mini:
            mini=x
    return mini
def test_ultima_cifra():
    assert(ultima_cifra([1,6,34,68,30,48,20],8))==48
    assert(ultima_cifra([1,2,3,4,5,6,7,8,28,37,67,3,9],7))==7
    assert(ultima_cifra([10,20,30,40,50],0))==10
test_ultima_cifra()

def check_if_prime(n):
    '''
    Functia verifica daca un numar este prim
    param: n-numarul de verificat
    return: True daca nr este prim, False daca nu
    '''
    if n==2:
        return True
    if n==1 or n<=0:
        return False
    for d in range(2,n):
        if n%d==0:
            return False
    return True

def super_prime(l):
    '''
    Functia afiseaza numerele din lista care sunt superprime(atat numarul cat si prefixele sale sunt prime)
    param:l=lista
    return:rezultat=lista cu numerele superprime
    '''
    rezultat=[]
    for x in l:
        ok=1
        aux=x
        while x>0:
            if check_if_prime(x)==True:
                x=x//10
            else:
                ok=0
                x=x//10
        if ok==1:
            rezultat.append(aux)
    return rezultat

def test_super_prime():
    assert(super_prime([173,239]))==[239]
    assert(super_prime([23,25,37,29]))==[23,37,29]
    assert(super_prime([239,173,25,59]))==[239,59]
test_super_prime()

def cmmdc(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
def test_cmmdc():
    assert(cmmdc(12,24))==12
    assert(cmmdc(50,25))==25
    assert(cmmdc(100,22))==2
test_cmmdc()


def cmmmdc_negativ(l):
    '''
    Afiseaza lista obtinuta in care numerele pozitive au fost inlocuite de cmmdcul lor iar cele negative de numarul cu cifrele in ordine inversa
    param:l=lista
    return:rezultat=lista procesata
    '''
    for i in range(len(l)-1):
        for j in range(len(l)):
            if l[i]>0 and l[j]>0:
                cmmdc1=cmmdc(l[i],l[j])
    for i in range(len(l)):
        if l[i]>0:
            l[i]=cmmdc1
        else:
            aux=l[i]
            aux=-aux
            inv=0
            while aux:
                inv=inv*10+int(aux%10)
                aux=int(aux/10)
            l[i]=-inv
    print(l)
    return l

def test_cmmmdc_negativ():
    assert(cmmmdc_negativ([-76,12,24]))==[-67,12,12]
    assert(cmmmdc_negativ([-32,20,15]))==[-23,5,5]
    assert(cmmmdc_negativ([-123,-15,-16,21,22,23]))==[-321,-51,-61,1,1,1]
test_cmmmdc_negativ()

def main():
    while True:
        print("1. Citire lista")
        print("2. Afiseaza toate numerele negative nenule din lista")
        print("3. Afiseaza minimul din lista cu ultima cifra egala cu un o cifra n data,citita de la tastatura")
        print("4. Afiseaza numerele super prime din lista")
        print("5. Afiseaza lista obtinuta dupa inlocuirea numerelor pozitive cu cmmdcul lor si a celor negative cu inversul lor")
        print("a. Afisare lista") #show all
        print("x. Iesire")

        optiune = input("Dati optiunea: ")

        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            print(nr_negative(l))
        elif optiune == "3":
            n = int(input("Dati un nr.: "))
            print(ultima_cifra(l,n))
        elif optiune == "4":
            print(super_prime(l))
        elif optiune == "5":
            print(cmmmdc_negativ(l))
        elif optiune == "a":
            print(l)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

main()
exit(0)