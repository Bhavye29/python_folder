def even_odd(n):
    if n%2==0:
        return True
    else:
        return False

def diamond(n):
    for i in range(1,n+1):
            space = n - i
            star = 2*i - 1
            print(space*" "+"*"*star)

    i = n - 1
    space = 1
    while i>=1:
        star = 2*i - 1
        print(" "*space + star*"*")
        space = space + 1
        i = i - 1



def diamond_boundary(n):
    #Program to print diamond shape
    s = 1
    space1 = n - 1
    for i in range(1,n+1):
            if i==1:
                    print(" "*space1 + "*")
            else:
                    space = n - i
                    #print(space)
                    print(" "*space + "*" + " "*s + "*")
                    s = s + 2
    #print(s)
    #print(space)

    i =  n - 1
    s = 2*n - 5
    space = 1
    while i>=1:
        if i==1:
                print(" "*space1 + "*")
        else:
            print(" "*space + "*" + " "*s + "*")
            s = s - 2
            space = space + 1
        i = i - 1
    #print(s)

def hollow_square(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i==1 or j==1 or i==n or j==n):
                print("*",end = " ")
            else:
                print(" ",end=" ")
        print()
                


def word_count(l):
    print(l)
    d = {}
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    #print(d)


    for i in d.keys():
        print(i,d[i])


def vowel_count(a):#string
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    m = []
    n = []
    for i in d.keys():
        m.append(i)
    for i in d.values():
        n.append(i)
    #print(m)
    #print(n)

    for i in range(len(m)):
        if m[i] in "aeiou":
            print(m[i],n[i])




#n = 5

def sort(l):
    #l = [] list
    print(l)
    print(len(l))
    for i in range(len(l)):
        for j in range(i,len(l)):
            if l[i]>l[j]:
                l[i],l[j] = l[j],l[i]
        
    print(l)



def right_word_trianle(l): #string
    for i in range(len(l)):
        for j in range(i+1):
            print(l[j],end = " ")
        print()

    second_last = len(l)-1
    while second_last>=0:
        for i in range(second_last):
            print(l[i],end = " ")
        print()
        second_last = second_last - 1

def inputer():
    b = int(input())
    a = input()
    x = a.split()
    if len(x)==b:
        print(True)
    else:
        print(False)



def biggest_substring(a):#a --> string
    print(a)
    substring = a.split()
    length = len(substring)
    #print(substring)
    for i in range(length):
        for j in range(i,length):
            if len(substring[i])>len(substring[j]):
                substring[i],substring[j] = substring[j],substring[i]
    print(substring[length-1])



def alternate_capital(a):#a--> string
    print(a)
    b = ""
    for i in range(len(a)):
        if i%2==0:
            b = b + a[i]
        else:
            b = b + a[i].upper()
    a = b
    print(a)



def square_diamond(n):
    #Upper half
    #n = 10
    a = n
    while n>=1:
        if (n==a):
            print((2*n-1)*"*")
        else:
            x = 2*a-1
            space = x - 2*n
            print("*"*n + " "*space + "*"*n)
        n = n - 1

    #lower half
    n = 2
    while n<=a:
        c = 2*a - 1
        space = c - 2*n
        if n==a:
            print((2*a-1)*"*")
        else:
            print("*"*n + " "*space + "*"*n)
        n = n + 1


def triangle_pattern(a):
    #a = 5
    n = 1
    while n<=a:
        c = 2*a - 1
        space = c - 2*n
        if n==a:
            print((2*a-1)*"*")
        else:
            print("*"*n + " "*space + "*"*n)

        n = n + 1


    n = a - 1
    while n>=1:
        if (n==a):
            print((2*n-1)*"*")
        else:
            x = 2*a-1
            space = x - 2*n
            print("*"*n + " "*space + "*"*n)
        n = n - 1



def slided_pattern(n):
    #n = 5
    i = 1
    for j in range(1,n+1):
        space = n - i
        print(" "*space + "*"*5)
        i = i + 1

def number_triangle(n):
    #n = 10
    for i in range(1,n+1):
        total = 2*i - 1
        spaces = n - i 
        #print(total)
        print(" "*spaces,end = "")
        for j in range(1,total + 1):
            if j%2==0:
                print("2" , end = "")
            else:
                print("1" , end = "")
        print()


'''
#left slant
n = 4
for i in range(1,n+1):
    space = n - i
    print(" "*space + "*")


#right slant
n = 4
space = 1
for i in range(1,n+1):
    print(" "*space + "*")
    space+=1
    
'''


def number_pyramid(n):
    #n = 10
    for i in range(1,n+1):
        s = i
        while s>=1:
            print(s,end = "")
            s = s - 1
        print()


'''
n = 3
while n>=1:
    print("*"*n)
    n = n - 1
'''

def reverse_number_triangle(n):
    #n = 5
    while n>=1:
        i = 1
        while i<=n:
            print(i,end = "")
            i = i + 1
        print()
        n = n - 1

'''
n = 5
i = 1
while i<=n:
    j = 1
    while j<=i:
        print(j,end = "")
        j = j + 1
    print()
    i = i + 1
'''

def number_continous_pattern(n):
    #n = 5
    s = 1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(s,end = "")
            s = s + 1
        print()
        


def alphabet_triangle(n):
    #n = 5
    s = 65
    for i in range(1,n+1):
        for j in range(1,i+1):
            print((chr(s)+" "),end = "")
            s = s + 1
        print()

def prime_number_checker(n):
    #n = 10
    flag = True
    for i in range(2,n):
        if n%i==0:
            flag = False
            break
    if flag:
        print("odd")
    else:
        print("even")



def prime_series(k): # primes till k
    #k = 5
    cnt = 0
    for n in range(1,k+1):
        flag = True
        for i in range(2,n):
            if n%i==0:
                flag = False
                break
        if flag:
            print(n,end = " ")
            cnt = cnt + 1

    print()
    print(f"Number of primes : {cnt}")



def number_pattern(n):
    #n = 5
    for i in range(1,n+1):
        j = 1
        while j<=n:
            print(j,end = " ")
            j = j + 1
        print()
        


def number_pattern_reverse(n):
    #n = 5
    for i in range(1,n+1):
        j = n
        while j>=1:
            print(j,end = " ")
            j = j - 1
        print()


def continous_number_pattern_sum(n):
    #n = 3
    s = 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(s,end =" ")
            s = s + 1
        print()
            

def number_triangle_continous(n):
    #n = 4
    for i in range(1,n+1):
        #print(i)
        j = i
        for k in range(1,i+1):
            print(j,end = " ")
            j = j + 1
        print()




def character_square(n):
    #n = 6
    c = 65
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(chr(c),end = " ")
        c = c + 1
        print()


def left_trianle_star(n):
    #n = 4
    i = 1
    while i<=n:
        space = n - i 
        print(" "*space + "*"*i)
        i+=1


def invert_left_triangle(n):
    #n = 4
    i = 1
    space = n - i
    while i<=n:
        j = 1
        print(" "*space,end = "")
        while j<=i:
            print(j,end = "")
            j = j + 1
        print()
        i = i + 1
        space = space - 1
