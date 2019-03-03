#Authours: Eduardo Roman, Jonathan Gil
import numpy as np
import matplotlib.pyplot as plt
from math import *
import random
import time
count = 0
commoncount = 0
def gcd(m, n):
    global count
    r = m % n
    count += 1
    if r == 0:
        return n
    else:
        m = n
        n = r
        return gcd(m, n)


def consecutiveInteger(m, n):
    consecutiveCount = 0
    t = min(m, n)
    while t > 0:
        if m % t == 0:
            consecutiveCount += 1
            if n % t == 0:
                consecutiveCount += 1
                return consecutiveCount
        consecutiveCount += 1
        t = t - 1
    return consecutiveCount

def fibonacci(k):
    #farray = [j for j in range(k)]
    farray = []
    farray.append(0)
    farray.append(1)
    n1 = 0
    n2 = 1
    count = 0
    nth = 0
    while count < k - 2:
        nth = n1 + n2
        farray.append(nth)
        #update values
        n1 = n2
        n2 = nth
        count += 1
    return farray


def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:

        # If prime[p] is not changed, then it is a prime
        if prime[p] == True:

            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    result = []
    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            result.append(p)
            #print(p)
    return result
def primefactorization(list, k):
    pfnumbers = []
    product = 0
    while k % 2 == 0:
        pfnumbers.append(2)
        k = k / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(sqrt(k) + 1), 2):
        # while i divides n , print i ad divide n
        while k % i == 0:
            pfnumbers.append(i)
            k = k / i

            # Condition if n is a prime
    # number greater than 2
    if k > 2:
        pfnumbers.append(k)

    return pfnumbers
def commonfactors(list1, list2):
    maxlength = max(len(list1), len(list2))
    minlength = min(len(list1), len(list2))

    global commoncount
    mlist = list(list1)
    nlist = list(list2)

    removed = []
    removed2 = []
    commonf = []

    i = 0
    j = 0

    while i < len(mlist) and j < len(nlist):
        curr_full = mlist[i]
        curr_sub = nlist[j]
        if curr_full == curr_sub:
            commoncount += 1
            commonf.append(curr_full)
            i += 1
            j += 1
            continue
        if curr_full < curr_sub:
            commoncount += 1
            i += 1
        else:
            j += 1
    return commonf

def main():
    global count
    global commoncount
    while True:
        try:
            TaskNumber = int(input("Enter the task you want to go into: "))
        except ValueError:
            print("This is not an integer")
            continue

        if TaskNumber == 1:
            try:
                userinput = int(input("Enter your 'n' value: "))
            except ValueError:
                print("This is not an integer")
                continue
            c_count = 0
            print()
            for i in range(1, userinput + 1):
                gcd(userinput, i)
                c_count += consecutiveInteger(userinput, i)

            MD = (count/userinput)
            D = (c_count/userinput)

            print("The AVG Modulo Divisions of ", userinput, "is: ", "%.2f" % MD)
            print("The AVG Consecutive Divisions of ", userinput, "is: ", "%.2f" % D, '\n')

            #reset counter
            count = 0

            UserValue = str(input("Produce Scatter Plot 'yes', 'y'?: "))
            if UserValue == 'yes' or 'y':
                # generate some integers
                #MValue = random.randint(0, 500)
                #NValue = 1  # random.randint(0, 500)
                consCount = 0
                colors = (1, 0, 0)
                area = np.pi * 3
                x_array = []
                y1 = []
                y2 = []
                value = 500
                print("Computing Task 1 ScatterPlot...\n")
                print("GCD plot..")
                #avg = 0
                for m in range(1, value + 1):
                    for n in range(1, m + 1):
                        #print("m: ", m, "n: ", n)
                        gcd(m, n)
                        consCount += consecutiveInteger(n, m)

                    x_array.append(m)
                    avgGcd = count/m
                    avgCons = consCount/m

                    y1.append(avgGcd)
                    y2.append(avgCons)

                    count = 0
                    #consCount = 0

                plt.scatter(x_array, y1, s=area, c=colors, alpha=0.5)
                #plt.scatter(x_array, y2, s=area, c=colors, alpha=0.5)

                plt.title('AVG MD()')
                plt.xlabel('Input size')
                plt.ylabel('AVG Divisions')
                plt.show()

                print('Consecutive integer graph...')
                plt.scatter(x_array, y2, s=area, c=colors, alpha=0.5)
                plt.title('AVG D()')
                plt.xlabel('Input size')
                plt.ylabel('Avg Divisions')
                plt.show()

        if TaskNumber == 2:
            start = time.time()
            k = int(input("Enter a value of K: "))
            nthterm = list(fibonacci(k))
            #print(nthterm)
            print("Fibonacci numbers sequence at k + 1: ", nthterm[k-1], "k: ", nthterm[k-2], "\n")

            colors = (1, 0, 0)
            area = np.pi * 3
            xarray = []
            yarray = []
            for i in range(1, len(nthterm)):
                if i + 1 < len(nthterm):
                    gcd(nthterm[i + 1], nthterm[i])
                    xarray.append(nthterm[i + 1])
                    yarray.append(count)
                    count = 0
            #print("X values: ", xarray, "\n")
            #print("Y values: ", yarray, "\n")

            plt.scatter(xarray, yarray, s=area, c=colors, alpha=0.5)
            print("The GCD of 'K' using the fibonacci sequence is: ", gcd(nthterm[k-1], nthterm[k-2]), "\n")
            plt.title('Modulo divisions using fibonacci')
            plt.xlabel('Input size')
            plt.ylabel('# of divisions')
            end = time.time()
            print("Execution time: ", "%.3f" % (end - start), "s")
            plt.show()

        if TaskNumber == 3:
            m = int(input("Enter value of 'm': "))
            n = int(input("Enter value of 'n': "))
            mprimes = list(SieveOfEratosthenes(m))
            nprimes = list(SieveOfEratosthenes(n))

            mpfnumbers = primefactorization(mprimes, m)
            npfnumbers = primefactorization(mprimes, n)
            print("Prime factors of ", m, "is: ", mpfnumbers)
            print("Prime factors of ", n, "is: ", npfnumbers)

            prime = commonfactors(mpfnumbers, npfnumbers)
            primegcd = 1
            for number in prime:
                primegcd *= number
            print("\nCommon prime factors: ", prime, '\n')
            print("GCD using middle school procedure is: ", primegcd)
            commoncount = 0

            uservalue = str(input("Produce scatter plot? 'yes', 'y': "))
            if uservalue == 'yes' or 'y':
                colors = (1, 0, 0)
                area = np.pi * 3
                xplot = []
                yplot = []
                for i in range(500):
                    #generate some integers
                    MValue = random.randint(2, 1000)
                    NValue = random.randint(2, 1000)

                    xplot.append(max(MValue, NValue))#(i)#max(MValue, NValue))

                    mlist = list(SieveOfEratosthenes(MValue))
                    nlist = list(SieveOfEratosthenes(NValue))

                    Mpfnumbers = primefactorization(mlist, m)
                    Npfnumbers = primefactorization(mlist, n)

                    primefactors = commonfactors(Mpfnumbers, Npfnumbers)
                    yplot.append(commoncount)
                    #commoncount = 0
                #print(yplot)
                #print(commoncount)
                commoncount = 0
                xplot.sort()
                plt.scatter(xplot, yplot, s=area, c=colors, alpha=0.5)
                plt.title('O(g) complexity of Middle School Procedure')
                plt.xlabel('Input size')
                plt.ylabel('# of comparisons')
                plt.show()




            #print(mprimes)
            #print(nprimes)


main()