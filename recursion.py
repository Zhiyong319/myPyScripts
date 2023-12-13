def factorial(n):
    if n>1:
        return n * factorial(n-1)
    else:
        return 1

n=10 
print('Factorial of ' +str(n) + ' is '+ str(factorial(n)))

def Fibonacci(n):
    # return the nth Fibonacci number
    if n>2:
        return Fibonacci(n-1) + Fibonacci(n-2)
    elif n==2:
        return 1
    elif n==1:
        return 0
    else:
        return -1

print('The '+str(n)+'th Fibonacci number is ' + str(Fibonacci(n)))

def FibonacciList(n):
    # return an n-element Fibonacci List
    if n<=0:
        return -1
    else:
        return [Fibonacci(x) for x in range(1,n+1)]

print('The ' + str(n) +'-element Fibonacci list is:' + str(FibonacciList(n)))

def FibLst(n):
    # return an n-element Fibonacci List
    if n < 1:
        return -1
    elif n==1:
        return [0]
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            next_value = sequence[len(sequence)-1] + sequence[len(sequence)-2]
            sequence.append(next_value)
        return sequence

print('The ' + str(n) +'-element Fibonacci list is:' + str(FibLst(n)))

# Build a function PascalsT which takes an integer n as an input and generate a n layer Pascals Triangle.
def PascalsT(n):
    if n==1:
        return [1]
    elif n==2:
        return[[1],[1,1]]
    else:
        layers=[[1],[1,1]]
        while len(layers)<n:
            newlayer_middle =[]
            lastlayer = layers[len(layers)-1] 
            for i in range(1,len(lastlayer)):
                newlayer_middle.append(lastlayer[i-1]+lastlayer[i])
            newlayer=[1]+newlayer_middle+[1]
            layers.append(newlayer)
        return layers 
print(PascalsT(5) )   

def SepNum(x):
    oddx =  []
    evenx = []
    # don't use oddx = evenx = [], oddx and evenx will be linked and pointed to the same values
    for i in x:
        if int(i)%2==0:
            evenx.append(i)
        else:
            oddx.append(i)

    return evenx + oddx

print(SepNum([1, 2, 3, 4, 5, 6]))

# concatenate two lists
list1 = [1, 3, 5]
list2 = [2, 4, 6, 8]

# Using + operator
mylist = list1 + list2

# Using extend()
import copy
mylist=copy.deepcopy(list1)
# mylist = list1 *1 # a copy of list1, mylist = list1 will make a link. Both list1 and mylist will be updated. 
mylist.extend(list2)

print(list1,list2)
print(list2)
print(mylist)