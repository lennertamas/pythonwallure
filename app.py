import prime

data = input("Give me a number:")

try:
    x = int(data)
    if prime.is_prime(x):
        print (f"{data} is prime number")
    else:
        print (f"{data} is not prime number")
except:

    print ("Ssomething is wrong")