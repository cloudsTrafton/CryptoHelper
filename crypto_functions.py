#Written by Claudia Trafton, Latest update 7/12/2018


#Functions to help you with some of the math behind cryptography.
#not all are totally original, I cited them.

#If you use these for your own class and work, PLEASE cite me!!
#also I would encourage you to please try and understand why these work
#and ask your professor for help if you don't understand.
#These are meant to be learning aids, not homework shortcuts.



#Thank you, wikibooks!
#https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
import fractions

#Extended Euclidean Algorithm to find Bezout Coefficients
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

#Use those coefficients to find the modular inverse of a number a in mod space m
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

#Thank you, rumpel!
#https://stackoverflow.com/questions/18114138/computing-eulers-totient-function
def totient(n):
    amount = 0        
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1
    return amount

def gcd(a,b):
    return fractions.gcd(a,b)

#a and b are the numbers to multiply or add in mod m1 * m2 space
#op is the operation. Put in "+" for addition, "*" for multiplication
def crt_mult(a, p):
    M = m1 * m2
    M2 = m1
    M1 = m2
    
    M1_inv = modinv(M1, M)
    M2_inv = modinv(M2, M)
    
    c1 = M1 * M1_inv
    c2 = M2 * M2_inv

    s,t = a % m1, a % m2
    u,v = b % m1, b % m2

    f_inv = (c1 * s) + (c2 * t)
    
#https://math.stackexchange.com/questions/614248/chinese-remainder-theorem-explanation
#Take in two lists, find x for these lists
def crt(m1, m2):
    total = 0
    prod = 1
    p = 0
    
    M = m1 * m2


#Find the quadratic residues of a prime number p. Only works for primes.
#Method: Find all elements of Z*p by counting from 1 to phi(p), inclusive
#Check if every element of Z*p meets Euler's criterion as outlined in the week 7 slides
def quadratic_residue_prime(p):
    print("finding all the quadriatic residues for " + str(p) + "...")
    Z_p = []
    qr = []

    for z in range(1,p):
        Z_p.append(z)

    print("The elements in Z*" + str(p) + " are..")
    print(str(Z_p))

    #Check Euler's Criterion for every element in Z*p.
    #Euler's Criterion: a is a quadratic residude if a^((p-1)/2) ~= 1 mod p
    for a in Z_p:
        print("")
        print("Check if " + str(a) + "^(" + str(p) + "-1/2) % " + str(p) + "== 1")
        if (a ** ((p-1)/2)) % p == 1:
            print("Yes it does! adding to residue list..")
            qr.append(a)
    print("")
    print("Quadratic residues are: ")
    return qr


#calculate the square roots in mod space of a prime p = q*r if a is given
#there will be 4 square roots, two for each prime
#currently, the code only works if p,q ~= 3 mod 4
def modular_square_roots(p,q,a):
    n = p * q
    b = (a ** ((p + 1)/4)) % p


#Code sources cited:
#https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python/6667361
#https://docs.python.org/3/tutorial/datastructures.html


#Method:
#Find the multiplication table mod k over the field k


#get the power table over the Field k
def power_table(k):
    eulerPhi_k = totient(k)

    #Create phi(k) x phi(k) matrix values of row ^ col mod k vaues
    #this is called list comprehension in Python
    F_k_pow = [[(a ** n) % k for n in range(1, eulerPhi_k + 1)] for a in range(1, eulerPhi_k + 1)]

    #print the values, so we can see them
    print("The power table. Each sublist is a row.")
    for row in F_k_pow:
        print(row)
    print("")
    return F_k_pow


#if the first occurrence of 1 is in the phi(k)th column, then it is a generator
#this is because a generator is defined as the minimum value where the element
#g mod k = phi(k)
#Check each sublist. If only the sub element's last value of sublist q is 1,
#then we know q is a primitive element by definition stated above.
def generators(k):
    prims = []
    F_k_pow = power_table(k)
    eulerPhi_k = totient(k)
    index_1 = 0 #hold the index of where we saw 1 for the first time
    rowNum = 1
    for row in F_k_pow:
        print("current row number " + str(rowNum) + ": " + str(row))
        print("is the first index of 1 equal to " + str(eulerPhi_k) + "?")
        if row.index(1) == eulerPhi_k-1: #if the first occurence of 1 is at the end, its a generator
            print("Yes it is! saving " + str(rowNum) + " to our list of generators...")
            prims.append(rowNum)
        print("")
            
        rowNum+=1 #go to the next row
            
    print("Generators are: ")           
    return prims
    
    
