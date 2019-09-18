import random
# Using g=5, p=23 -> public domain
g = 5
p = 23

def isPrime(j):
    c = 0
    for i in range(2,j+1):
        if j%i == 0:
            c+=1
    if c==1:
        return True
    else:
        return False
    

def create_rand_prime(p,q):
    primes = [i for i in range(p,q) if isPrime(i)]
    n = random.choice(primes)
    return n

class Host:
    def __init__(self, g, p, name):
        self.g = g
        self.p = p
        self.name = name
        self.random_sender = create_rand_prime(1,15)
        self.key = 0
        self.partial_key = 0
        print(self.name, "-> secret random prime : ", self.random_sender)
        
    def receive_calc_key(self, par_key):
        self.key = (par_key**self.random_sender) % self.p
        #print(self.name, "-> final secret key : ", self.key)

    def partial_key_creation(self):
        self.partial_key = (self.g**self.random_sender) % self.p
        print(self.name, "-> partial key : ", self.partial_key)

Alice = Host(g, p, "Alice")
Bob = Host(g, p, "Bob")

Alice.partial_key_creation()
Bob.partial_key_creation()

Alice.receive_calc_key(Bob.partial_key)
Bob.receive_calc_key(Alice.partial_key)

print("Alice -> Secret Key for Communication : ", Alice.key)
print("Bob -> Secret Key for Communication : ", Bob.key)


        
