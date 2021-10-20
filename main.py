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
test_super_prime()




def main():
    while True:
        print("1. Citire lista")
        print("2. Afiseaza toate numerele negative nenule din lista")
        print("3. Afiseaza minimul din lista cu ultima cifra egala cu un o cifra n data,citita de la tastatura")
        print("4. Afiseaza numerele super prime din lista")
        print("5. ")
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
            print()
        elif optiune == "a":
            print(l)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

main()
exit(0)