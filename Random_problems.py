# Create a fibonacci sequence
fibonacci = 0
sterm = 1
while sterm <= 9 :
    print (sterm)
    temporal = sterm
    sterm += fibonacci
    fibonacci = temporal
#%% Create a non-recursive function that is passed an integer n as an argument and returns a list of n elements of the Fibonacci series. 
def fibo(lim):
    aux=1
    fib=0
    init=1
    while init <= lim:
        aux += fib 
        fib = aux - fib
        init += 1
        fi.append(fib)            

lim = int(input("Elements of the sequence: "))
fi=[]
fibo(lim)
print(fi)
#%% Create a recursive function that is passed an integer number n as an argument and returns the list of n elements of the series.
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
#main program
n= int(input("Elements of the sequence: "))
serie_fib=[]
for i in range(n):
    serie_fib.append(fib(i))

print (serie_fib)

#%% Write a code that allows user capture day and month and write "True" if the day of the month is between March 10 and July 10 and "False" otherwise. 
def mes_no (v1,v2):
    if v1 in meses31:
        if v2 in range (1,32):
            print ('True')
        else:
            print ('False')
    elif v1 in meses30:
        if v2 in range (1,31):
            print ('True')
        else:
            print('False')
    else:
        print ('False (Non-existent date)')
        
#main program    
meses30= ['april','may','june']
meses31=['march','july']
print('Enter month and day:  ' )
m= str(input())
d= int(input())
mes_no(m,d)
#%% Same with datetime
import datetime

def date (d,m):
    b=datetime.date(2019,m,d)
    date= datetime.date(2019,7,10)
    date1=datetime.date(2019,3,10)
    if b <= date and b>=date1:
        print ('true')
    else: 
        print ('false')

d=int(input('Enter day: '))
m=int(input('Enter month: '))
date(d,m)
 
#%% Create a code that show the lenght and furthest point of the coordinate values enter: (-3,4) (3, -4) and (-1,1)
import math
x = [] 	# list of x
y = []	# list of y
longi = []	# list with all the lengths of the lines from (0,0) to the typed coordinate 
for i in range(3):	# repeats 3 times because they are three coordinates
    x.append(int(input("Enter the x coordinate of the point: "))) # plus
    y.append(int(input("Enter the y coordinate of the point: ")))
    longi.append(math.sqrt(x[i]**2+y[i]**2)) # the length of the hypotenuse is the distance to the coordinate 
print(x)
for i in range(2):
    a = longi[i]
    b = longi[i+1]
    if a <= b:	 #the greater the index of the greater length
        mayor = i+1
    else: mayor = i
         
print("Coordinate of the furthest point is:  (",
      x[mayor], ",",y[mayor],") with length:  ",longi[mayor])

#%% 4 con if 
a=float (input ('a = '))
b=float (input ('b = '))
c=float (input ('c = '))

if a==0:
    print ('La ecuación no es cuadrátiva x es ' , -c/b)
else: 
    disc= b**2-4*a*c
    if disc == 0 :
        r1=-b/2*a
        print('El discriminante es cero,por lo que hay una sola solución y x es', r1 )
    else: 
        if disc > 0: 
            r1 = -(b+ disc **(1/2))/2*a
            r2 = -(b - disc **(1/2))/2*a
            print ('Hay dos soluciones reales (dos raices): ', r1 ,'y', r2)
        else:
            rp=- b/2*a
            lp = - (disc**(1/2))/2*a
            r1 =rp + lp
            r2= rp - lp
            print ('Hay dos soluciones complejas (dos raíces): ', r1, 'y',r2)
#%%Create a Bounded Linear Search algorithm to locate duplicate values in a sequence.
# This is a powerful technique for unsorting a wide variety of summary reports. A failure to use this algorithm leads to excessive over-processing in many types of applications. 
def valores(seq,a):
    for v in seq:
        i=0
        a.append(v)
        while a[i] != v:
                i +=1
        if  i == len(a):
            a.append(v)
        elif i!= (len(a)-1):
            a.remove(v)
    return a

seq =[1,2,33,2]
a=[]
valores(seq,a)
print(a)
#%%Binary search. This is not as universally useful as the limited linear search (above) because it requires the data to be ordered. Two parameters are passed: the sequence seq and the sought value tgt.
def binarySearch(arr, tgt):
    l=0
    r=len(arr)
    mid = (l + r) // 2
    while (l+l) < r and arr[mid] != tgt:

        if tgt < arr[mid]:
            r = mid
        if tgt > arr[mid]:
            l = mid
        mid=(l + r) // 2;
    if tgt == arr[mid]:
        return mid
    if tgt != arr[mid]:
        return -1
t=int(input("enter the item to searchr: "))
n = int(input("enter size"))
arr = []
for x in range(0,n):
    x = int(input())
    arr.append(x) 
# Function call
result  = binarySearch(arr, t) +1

if result != -1:
    print("The element is in position: % d" % result)
else:
    print("The element is not present in the range ")
#%% Quicksort A
def sort(a,l,hi):
    middle=int((hi+l)/2)
    ls=l
    hs=hi
    while ls<hs:
        if a[ls]<= a[middle]:
            ls+=1
        elif a[ls] > a[middle]:
             a[ls],a[middle]= a[middle],a[ls] 
        elif a[hs] >= a[middle]:
            hs-=1
        elif a[hs] < a [middle]:
            a[hs],a[middle]= a[middle],a[hs] 
    sort(a,l,middle) 
    sort(a,middle+1,hi) 
 
a=[54,26,93,17] 
sort(a,0,len(a))
print (a)
#%% Quicksort B
def quickSortHelper(alist,first,last):
   if first<last:
       split= partition(alist,first,last)
       quickSortHelper(alist,first,split-1)
       quickSortHelper(alist,split+1,last)

def partition(alist,first,last):
   pivotvalue = alist[first]
   leftmark = first+1
   rightmark = last
   done = False
   while not done:
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSortHelper(alist,0,len(alist)-1)
print(alist)
#%%8 Recursive Search
def binarySearch (arr, l, r, x): 
    if r >= l: 
        mid = l + (r - l)//2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid+1, r, x) 
    else: 
        return -1 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
result = binarySearch(arr, 0, len(arr)-1, x) 
if result != -1: 
    print ("Element is present at index %d" % result )
else: 
    print ("Element is not present in array")

#%% Sieve of Eratosthenes
#Corderbyte- 
def sieve(limit):
  for i in range(1, limit):
    bools.append(True)
  for i in range(2, limit):
    if bools[i-2]:
      for j in range(i*2, limit+1, i):
        bools[j-2] = False
  for p in range(0, len(bools)):
    if (bools[p]):
      primes.append(p+2)
      
  return primes
    
bools = []
primes = []
n =int(input('Prime number limit:  '))
sieve(n)
#%% Sieve of Eratosthenes
#Youtube: "python: Calculating prime numbers"- Joe James
def sieve(lim):
    for x in range (2,lim+1):
        isprime=True
        for y in range (2,x):
            if x % y==0:
                isprime=False
                break #se agrega para parar el programa cuando se ecuentra un %=0
        if isprime:
            primes.append(x)

primes = []
n =int(input('Limite de numeros primos: '))
sieve(n)
print (primes)
    
    
#%% Polynomial arithmetic  
def suma (p,q):
    rsize= max(len(p),len(q))
    p1=p [:]
    i=len(p)
    while i < rsize:
        p1.insert(0,0)
        i+=1
    i=len(q)
    q1=q[:]
    while i < rsize:
        q1.insert(0,0)
        i+=1
    r=[0]*rsize
    for i in range (rsize):
        r[i]=p1[i]+ q1[i]
    return r

def multiplicar (p,q):
    rsize= len(p)+len (q)
    r=[0]*rsize
    for i in range(len(p)):
        for j in range (len(q)):
            r[i+j]= r[i+j]+p[i]*q[j]
    return r 
p=[4,0,3,1]
q=[2,-3,-4]

print('The sum of the polynomial is: ', suma(p,q))
print('The product of the polynomial is: ', multiplicar(p,q))


#%% Dutch national flag.
import random
def swap(arr, i1, i2):
  temp = arr[i1]
  arr[i1] = arr[i2]
  arr[i2] = temp

def dutchNatFlag(arr):
  low = 0
  mid = 0
  high = len(arr) - 1

  while mid <= high:
    if arr[mid] == 0:
      swap(arr, low, mid)
      low += 1
      mid += 1
    elif arr[mid] == 2:
      swap(arr, mid, high)
      high -= 1
    elif arr[mid] == 1:
      mid += 1
      
  return arr
m=[]
for i in range(6*6): 
    arr=[0]*10
    for i in range (10):
        arr[i] = random.randint(0,2)
        pass
    arr=dutchNatFlag(arr)
    m.append(arr)
print (m)