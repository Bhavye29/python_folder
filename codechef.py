def atm():
	x1,y1 = input().split() 
	x = int(x1)    #withdraw cash
	y = float(y1)  #account balance
	if x<y:
		if x>0 and x<=2000:
			if x%5==0:
				y=y-x-0.50				
				print(float(y))
			else:
				print(y)
	elif x>y:
		print(y)
#atm()

def enormous_input():
	import time
	n1,k1 = input().split()
	n  = int(n1)
	k = int(k1)
	count = 0
	start  = time.time()
	if k<=(10**7):
		for i in range(1,n+1):
			tj = int(input())
			if tj<(10**9):
				if tj%k==0:
					count = count+1
	end = time.time()
	print(count)
	print(end-start)
def sum():
	t = int(input()) #testcases number
	l = []
	for i in range(1,t+1):
		a1,b1 = input().split()
		a,b = int(a1),int(b1)
		s = a+b
		l.append(s)
	for j in l:
		print(j)

def sum_digits():
	t = int(input()) #testcases number
	l = []
	for i in range(1,t+1):
		n1 = input()
		s = 0
		for i in n1:
			s = s + int(i)
		l.append(s)
	for j in l:
	        print(j)

def remainder():
	t = int(input()) #testcases number
	l = []
	for i in range(1,t+1):
		a1,b1 = input().split()
		a,b = int(a1),int(b1)
		l.append(a%b)
	for j in l:
		print(j)

def sum_last_first():
	t = int(input()) #testcases number
	l = []
	if t>=1 or t<=1000:
		for i in range(1,t+1):
			s = 0
			n = input()
			s = int(n[0]) + int(n[len(n)-1])
			l.append(s)
	for j in l:
		print(j)

def team()		:
	n = int(input()) #testcases number
	count = 0
	for i in range(n):
			a1,b1,c1 = input().split()
			a = int(a1)
			b = int(b1)
			c = int(c1)
			if (a==1 and b==1) or (b==1 and c==1) or (a==1 and c==1) or (a==1 and b==1 and c==1):
					count = count + 1
	print(count)
#team()
def boy_girl():
	a = input()#string
	l = []
	for i in a:
		if i not in l :
			l.append(i)
	if len(l)%2 == 0:
		print("CHAT WITH HER!")
	else:
		print("IGNORE HIM!")
def linear_eq():
	n1,m1 = input().split()
	n = int(n1)
	m = int(m1)
	if n>m:
		count = 0
		for a in range(0,n+1):
			for b in range(0, n+1):
				if (((a**2)+b)==n) and ((a+(b**2))==m):
					count = count+1
		print(count)

	elif m>n:
		count = 0
		for a in range(0,m+1):
			for b in range(0, m+1):
				if (((a**2)+b)==n) and ((a+(b**2))==m):
					count = count+1
		print(count)
	elif n == m:
		count = 0
		for a in range(0,n+1):
			for b in range(0, m+1):
				if (((a**2)+b)==n) and ((a+(b**2))==m):
					count = count+1
		print(count)

def multiple():
	n = int(input())
	count = 0
	for i in range(1,n):
		if (i%3==0 or i%5==0):
			count = count + i
			print(i)
	print(count)

def fibonacci_even_sum():
	a = 1
	b = 2
	c = 0
	l = []
	print(a,end = ",")
	print(b,end = ",")
	l.append(a)
	l.append(b)
	for i in range(10000000):
		c = a + b
		if c<=4000000:
			print(c,end = ",")
			l.append(c)
			a  = b
			b = c
	s=0
	for j in l:
		if j%2==0:
			s=s+j
	print("\n")
	print(s)

def sum_square_diff():
	n = int(input())
	s = 0
	for i in range(1,n+1):
		s = s + (i**2)
	print(s)

	k = 0
	for j in range(1,n+1):
		k = k+j
	t = (k**2)
	print(t)
	if t>s:
		diff  = t-s
		print(diff)
	else:
		diff  = s-t
		print(diff)

def pythagorean_triplet():
	'''
	a = int(input())
	b = int(input())
	c = int(input())
	if ((a**2)+(b**2)) == (c**2):
		print("triple")


	'''
	for a in range(1,1000):
	        for b in range(2,1000):
	                for c in range(3,1000):
	                        if (a+b+c)==1000:
	                                if ((a**2)+(b**2)) == (c**2):
	                                        '''
	                                        print(a)
	                                        print(b)
	                                        print(c)
	                                        '''
	                                        print(a*b*c)
	                                        break


def prime_sum():
        n = int(input())
        s = 0
        for i in range(2,n+1):
                flag = False
                for j in range(2,i):
                        if i%j==0:
                                flag = True
                                break
                if flag==False:
                        #print(i,end = ",")
                        s=s+i
        print(s)


def amicable_no():
	k = int(input())# range
	def proper_divisor(n):
            global c
            c = 0
            for i in range(1,n):
                    if n%i==0:
                            #print(i)
                            c = c + i
            #print(c)

	s = 0
	for a in range(1,k):

		for b in range(1,k):
			proper_divisor(a)
			x = c
			proper_divisor(b)
			y = c

			if x==b and y==a:
				print(x,end=",")
				print(y)
				s = s + x + y
	print(s)

#amicable_no()

def quad_prime():
        def prime(x):
                y = x
                s = 0
                global flag
                global k
                k = 0
                for i in range(2,y+1):
                        flag = False
                        for j in range(2,i):
                                if i%j==0:
                                        flag = True
                                        break
                        if flag==False:
                                k = 1
                                #print(i,end = ",")
                        
        l = []
        for n in range(0,1001):
                a = 0
                b = 0
                while a<1000:
                        while b<=1000:
                                x = ((n**2) + a*n + b)
                                prime(x)        
                                if k==1:
                                        print(a*b)
                        b = b + 1
                a = a + 1
        quadratic_prime()
        #print(l)

def list_multiply():
	l = "0."
	for i in range(1,1000003):
	        l = l + str(i)
	#print(l)


	c = [1,10,100,1000,10000,100000,1000000]
	k = 1
	for i in range(len(c)):
	        k = k * int(l[c[i]+1])
	print(k)


def number_digits():
        a = 1
        b = 1
        c = 0
        l = []
        l.append(a)
        l.append(b)
        while len(str(c))!=1000:
                c = a + b
                l.append(c)
                a = b
                b = c
        print(c)
        print(l)
        print(len(l))
def palindrome():

	l = input()
	if len(l)%2==0:
		#print("Even")
		if l == l[::-1]:
			print("palindrome")
		else:
			print("not palindrome")
 
def middle():
	l = [10,20,30,40]
	print(l)
	if len(l)%2==0:
		middle  = l[(len(l)//2)-1]
		print(middle)
	else:
		middle  = l[((len(l)+1)//2)-1]
		print(middle)

def num_mirror():
	n = int(input())
	if n>=0 and n<=(10**5):
		print(n)


def lucky_four():
        t = int(input()) #testcases number
        l = []
        if t>=1 or t<=100000:
                for i in range(1,t+1):
                        s = input()
                        count  = 0
                        for i in s:
                                if i == "4":
                                        count = count+1
                        l.append(count)



        for i in l:
                print(i)


def small_factorials():
	t = int(input()) #testcases number
	l = []
	if t>=1 or t<=100:
	        for i in range(1,t+1):
	                s = int(input())
	                c = 1
	                for i in range(1,s+1):
	                        c = c*i
	                l.append(c)
	for i in l:
	        print(i)



def reverse_num():
        t = int(input()) #testcases number
        l = []
        if t>=1 or t<=1000:
                for i in range(1,t+1):
                        n = input()
                        c = ""
                        b = 1
                        i = len(n)-1
                        while i!=0:
                                c = c + n[i]
                                i = i - 1
                        c = c + n[0]
                        l.append(c)
        for i in l:
                print(i)
                
def lead_game():
        n = int(input())
        l = []
        x = []
        y = []
        for i in range(n):
                a1,b1 = input().split()
                a = int(a1)
                b = int(b1)
                c = abs(a-b)
                l.append(c)
                x.append(a)
                y.append(b)
                
        l.sort()

        #print(l)
        z = max(l)
        for i in x:
                for j in y:
                        if ((abs(i-j))==z) and i>j:
                                print("1 ",z)
                        elif ((abs(i-j))==z) and j>i:
                                print("2 ",z)


def palindrome():
        t = int(input())
        l = []
        for i in range(t):
                n = input()

                c = ""
                j  = len(n)-1
                while j>=0:
                        #print(a[i])
                        c = c + n[j]
                        j = j - 1
                if c==n:
                        #print("wins")
                        l.append("wins")
                else:
                        #print("loses")
                        l.append("loses")
                
        for j in l:
                print(j)

def approx():
        a = float(input())
        x = int(a)
        y = x+1
        if abs(y-a) > 0.55:#Nearest approximation
                print(int(a))
        else:
                print(y)


def lead_game_round():
        y = []
        l = []
        d = {}
        t = int(input())
        for i in range(t):
                a1,b1 = input().split()
                a,b = int(a1),int(b1)
                s = abs(a-b)
                if a>b:
                        d[s] = a
                        y.append(a)
                else:
                        d[s] = b
        #print(d)


        for i in d:
                l.append(i)
        x = max(l)
        #print(x)
        if d[x] in y:
                print("1",x)
        else:
                print("2",x)



def primality_test():
        t = int(input())
        l = []
        for i in range(t):
                flag = False
                n = int(input())
                for j in range(2,n):
                        if n%j==0:
                                flag = True
                                break
                if flag == False:
                        l.append("yes")
                else:
                        l.append("no")
        for i in l:
                print(i)


def total_expense():
        t = int(input())
        l = []
        for i in range(t):
                q1,p1 = input().split()
                q = int(q1)
                p = int(p1)
                if q>1000:
                        p = p - 0.1*p
                        l.append(float(p*q))
                else:
                        l.append(float(q*p))
        for i in l:
                print(i)

def gross_salary():
        t = int(input())
        l = []
        for i in range(t):
                salary = int(input())
                if salary<1500:
                        hra = 0.1*salary
                        da  = 0.9*salary
                        gross = salary + hra + da
                        l.append(gross)
                if salary>=1500:
                        hra = 500
                        da = 0.98*salary
                        gross = salary + hra + da
                        l.append(gross)
        for i in l:
                print(i)

def grade_steel():
        t = int(input())
        l = []
        for i in range(t):
                a1,b1,c1 = input().split()
                a,b,c = float(a1),float(b1),float(c1)
                if a>50 and b<0.7 and c>5600:
                        l.append("10")
                elif a>50 and b<0.7 :
                        l.append("9")
                elif b<0.7 and c>5600:
                        l.append("8")
                elif a>50 and c>5600:
                        l.append("7")
                elif a>50 or c>5600 or b<0.7:
                        l.append("6")
                else:
                        l.append("5")
        for i in l:
                print(i)

def rectangle():
        t = int(input())
        l = []
        for i in range(t):
                a1,b1,c1,d1 = input().split()
                a,b,c,d = int(a1),int(b1),int(c1),int(d1)
                #condition
                if (((a==b) and (c==d)) or ((a==c) and (b==d)) or ((a==d) and (b==c))):
                        l.append("YES")
                elif a==b==c==d:
                        l.append("YES")
                else:
                        l.append("NO")
        for i in l:
                print(i)


def length_breadth():
        lm = []
        l = int(input())
        b = int(input())
        ar = l*b
        per = 2*(l+b)
        ml = []


        if ar>per :
                lm.append("Area")
                ml.append(ar)
                
        elif ar<per:
                lm.append("Peri")
                ml.append(per)
        else:
                lm.append("Eq")
                ml.append(ar)
        for i in lm:
                print(i)
        for i in ml:
                print(i)

def matches():
        t = int(input())
        l = []
        for i in range(t):
                a1,b1 = input().split()
                a,b = int(a1),int(b1)
                sume = str(a+b)
                cnt = 0
                for j in sume:
                        if j=="0":
                                cnt = cnt + 6
                        elif j=="1":
                                cnt = cnt + 2
                        elif j == "2":
                                cnt = cnt + 5
                        elif j == "3":
                                cnt = cnt + 5
                        elif j == "4":
                                cnt = cnt + 4
                        elif j == "5":
                                cnt = cnt + 5
                        elif j == "6":
                                cnt = cnt + 6
                        elif j == "7":
                                cnt = cnt + 3
                        elif j == "8":
                                cnt = cnt + 7
                        elif j == "9":
                                cnt = cnt + 6
                l.append(cnt)
        for i in l:
                print(i)

def data():
        t = int(input())
        l = []
        for i in range(t):
                n1,k1 = input().split()
                n,k = int(n1),int(k1)
                s = 0
                for j in range(n):
                        m = 0
                        t1,d1 = input().split()
                        t,d = int(t1),int(d1)
                        if t>k:
                                rup = t*d
                                m = m + rup
                        s = s + m
                l.append(s)
        for i in l:
                print(i)

def heaven():
        t = int(input())
        l = []
        for i in range(t):
                n1,v11,v22 = input().split()
                n,v1,v2 = int(n1),int(v11),int(v22)
                s = (2)**(1/2)
                t1 = (n*s)/v1
                t2 = (n)/v2
                if t1<t2:
                        l.append("Stairs")
                elif t2<t1:
                        l.append("Elevator")
        for i in l:
                print(i)
                
                        
