def digits(n):
    count = 0
    while n != 0:
        count += 1
        n = n // 10        
    print(count)


def words(sentence):
    sent = sentence.split(' ')
    print(len(sent))


def largest(a,b,c):
    if a > b and a > c:
        print("Biggest is ", a)
    elif b > a and b > c:
        print("Biggest is ", b)
    else:
        print("Biggest is ", c)


def largest_and_smallest(a,b,c):
    n = [a, b, c]
    n = sorted(n)
    print(f"biggest and smallest are {n[2], n[0]}")
    

def table(a, b):
    i = 1
    while i != b+1:
        print(f"{a}X{i} = {a*i}")
        i += 1


    
def table2(a,b):
    i = 1
    
    while i != a+1:
        j = 1
        while j != b+1:
            print(i*j, end = ' ')
            j += 1
        print("\n")
        i += 1


def average(l):
    sum = 0
    for i in l:
        sum = sum + i
    print("average is ", sum/(len(l)))


def fuzzbuzz(n):
    for i in range (1, n+1):
        if i % 15 == 0:
            print("fuzzbuzz")
        elif i % 3 == 0:
            print("fuzz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


def maximum(l):
    l = sorted(l)
    a = len(l)-1
    print("maximum number is ", l[a])


def panagram(sentence):
    setc = sentence.lower()
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in setc:
            return False
    return True


def freq(sentence):
    sent = {}
    for i in sentence:
        if i in sent:
            sent[i] += 1
        else:
            sent[i] = 1
    print(sent)
        
    
def ARi():
    
