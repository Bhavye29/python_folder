def first():
	import time
	import random
	y=int(input("Enter Lowerlimit : "))
	z=int(input("Enter Upperlimit : "))
	l=[]
	for i in range(y,z+1):
		x = random.randint(y,z+1)
		l.append(x)
	print(l)


	def func(l):
		print("\n")
		s=0
		m,n=0,0
		start = time.time()
		for i in l:
			if i%2==0:
				print(i," Even")
				s=s+1
				m=m+1
			else:
				print(i," Odd")
				s=s+1
				n=n+1
		end = time.time()
		t=end-start
		print("\n")
		print("Total" , s)
		print("Even :",m)
		print("Odd :",n)

		print("Total time :",t)

		while True:
			c = input('$ ')
			print(c)
			if c[0:] == "even":
				print(m)
			elif c[0:] == "odd":
				print(n)
			elif c[0:] == "type":
				print(type(l))
			elif c[0:] == "exit":
				exit()
			elif c[0:] == "l":
				print(l)
			else:
				print("Invalid Command!")
	func(l)

def arithmetic_progression(s):
	count = 0
	n = 2
	while (2*s+n-n**2) > 0:
		a= (2*s+n-n**2)/(2*n)
		if a - int(a) == 0:
			print(a,n)
			count+=1
		n+=1
	print(count)
#arithmetic_progression(100)

def even_odd():
	n=int(input("Enter number : "))
	if n>=1 and n<=100:
	    if n%2!=0:
	        print("Weird")
	    elif n%2==0 and  n>=2 and n<=5:
	        print("Not Weird")
	    elif n%2==0 and  n>=6  and n<=20:
	        print("Not Weird")
	    elif n%2==0 and  n>=20 :
	        print("Not Weird")
#even_odd()

def is_leap(year):
    leap = False
    if year>=1900 and year<=10**5  and year%4==0 and year%100==0 and year%400==0:
        return True
    # Write your logic here
    else:
        return leap

#year = int(input())
#print(is_leap(year))

def find_pair(l,target):#l=input list
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if l[i]+l[j]==target:
				#print([l[i],l[j]])
				if l[i]>l[j]:
					print([l[j],l[i]])
				else:
					print([l[i],l[j]])
#find_pair([10,20,30,40,50],90)

def prime_factor(a):
	for i in range(2,a):
		if a%i==0:
			print(i,end=" ")
			a = a//i
#prime_factor(63)

def prime():
	for num in range(2,i):  
	   if num > 1:  
	       for i in range(2,num):  
	           if (num % i) == 0:  
	               break  
	       else:  
	           print(num)  

def if_else():
	def greater():
		a=int(input())
		b=int(input())
		if a==b:
			print("equal")
		if a>b:
			print("a greater than b")
		else:
			print("a is less than b")


	def namste():
		a=int(input())
		if a==1:
			print("Namaste")
		elif a==2:
			print("Hello")
		elif a==3:
			print("boujrne")
		else:
			print("Invalid")
	#namste()

	def calculator():
		a=int(input())
		b=int(input())
		op=input("Enter operator : ")
		if op=="+":
			print(a+b)
		elif op=="-":
			print(a-b)
		elif op=="*":
			print(a*b)
		elif op=="/":
			print(a/b)
		elif op=="%":
			print(a%b)
		else:
			print("Invalid operator")
	#calculator()
if_else()

def for_while():
	def rn():
		for i in range(0,11):
			print(i,end="-")
		print()

	def even():
		n=int(input())
		i=0
		while i <= n:
			print(i)
			i=i+2
	#even()

	def menu():
		a=int(input())
		if a==1:
			s=0
			while True:
				b=int(input())
				s=s+b
				if b==0:
					if s>=90:
						print("This is good")
						break
					elif s<=89 and s>=60:
						print("This is also good")
						break
					elif s<=59 and s>=0:
						print("This is good as well")
						break
		elif a==0:
			print("Ok")
	#menu()

	def prime():
		a=int(input())
		flag = False
		for i in range(2,a):
			if a%i==0:
				flag = True
				break
		if flag == True:
			print("Not prime")
		else:
			print("prime")

	def table():
		a = int(input())
		for i in range(1,11):
			print(a*i)

	def prime_range():
		n=int(input("Enter range : "))
		for i in range(2,n+1):
			flag = False
			for j in range(2,i):
				if i%j==0:
					flag = True
					break
			if flag == False:
				print(i)
	prime_range()


	#prime() #table() 
#for_while()

def pattern():
	def square():
		for i in range(1,5):
			#print("*"*5)
			for j in range(1,60):
				print("*",end="")
			print()
	#square()
	def inward_pyramid():
		i=3
		while i>=1:
			print("*"*i)
			i=i-1
	#inward_pyramid()
	def pyramid():
		i=1
		while i<=5:
			print("*"*i)
			i=i+1
	#pyramid()

pattern()


def vowcount():
        s = input()
        m = s.split()
        cnt = 0
        #l = []
        for i in m:
                if (i[0] in "aeiou") or (i[0] in "AEIOU"):
                       print(i)
                       cnt = cnt + 1
        '''
        for i in l:
                print(i)
        '''
        print(cnt)

def max_length():
        s = input()
        m = s.split()
        d = {}
        for i in m:
                d[len(i)] = i
        #print(d)

        t = max(d.keys())
        x = d.get(t)
        print(f"max length : {x}")


def counter():
        s = input()
        m = s.split()
        o = ""
        d = {}
        for i in range(len(s)):
                if s[i] not in d:
                        d[s[i]] = 1
                else:
                        d[s[i]] = d[s[i]] + 1

        print(d)


def rsa():
    import time

    p,q = 53,59
    n = p*q
    e = 3
    t = (p-1)*(q-1)
    k = 2
    d = (k*t + 1)/e
    d = (k*t + 1)//e

    xy = "abcdefghijklmnopqrstuvwxyz "
    ox = {}
    for i in range(len(xy)):
        ox[i] = xy[i]

    print(ox)

    data = input()
    print(data)
    start = time.time()
    raw_data = ""


    for i in range(len(ox)):
        for j in range(len(data)):
            if data[j] == ox[i]:
                raw_data = raw_data + str(i + 1)


    print(f"Raw data : {raw_data}")

    def encrypt(raw_data):
        global encrypted
        encrypted = (int(raw_data)**e) % n
        print(f"Encrypted messege : {encrypted}")

    encrypt(raw_data)



    def decrypt(encrypted_data):
        global decrypted
        decrypted = ((encrypted_data)**d) % n
        #print(f"decrypted messege : {decrypted}")
        back = str(decrypted)
        original_data = ""
        for i in back:
            if int(i) in ox:
                original_data = original_data + ox[int(i)-1]
        print(f"Decrypted messege : {original_data}")
        print(f"Decrypted messege : {decrypted}")


    decrypt(encrypted)
    end = time.time()
    print(f"Elapsed time : {end-start}")
#rsa()



def circle():
    import math
    import matplotlib.pyplot as plt
    l = []#x-axis
    m = []#y-axis
    cnt = 0
    r = int(input())
    for i in range(-r,r+1):
        for j in range(-r,r+1):
            if (i**2) + (j**2) == r:
                cnt = cnt + 1
                print(f"({i},{j})")
                l.append(i)
                m.append(j)
    '''
    print(f"(0,{r})")
    l.append(0)
    m.append(r)
    print(f"(0,{-r})")
    l.append(0)
    m.append(-r)
    print(f"({r},{0})")
    l.append(r)
    m.append(0)
    print(f"({-r},{0})")
    l.append(-r)
    m.append(0)
    '''


    print(f"Radius = {r}")
    print(f"Circumfrence = {2*math.pi*r}")
    print(f"Area = {math.pi*(r**2)}")
    print(f"Number of points = {cnt}")
    print(l)
    print(m)


    for i in range(len(l)):
            plt.plot(l[i],m[i],"bo")
    plt.show()


def win_defeat():
	n = 10
	k = 2
	while n>=k:
		n = n - k
		k = k//2
		if k<n :
			print("defeat")
			break
		elif n<k :
			print("win")
			break

def win_lose():
        l,m = [],[]
        attacker = int(input())
        opponent = int(input())
        for i in range(opponent):
                opponent = opponent - attacker
                l.append(opponent)
                attacker = attacker//2
                m.append(attacker)
                
        print(l,m)
        if l[len(l)-1]<m[len(l)-1]:
                print("wins")
        else:
                print("lose")

#range(start,stop,step(start-something))