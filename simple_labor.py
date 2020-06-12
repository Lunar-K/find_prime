import time

def lprime(i):
    if i == 1:
        return 0
    if i == 2:
        return 1

    for k in range(2, i):
        if i%k == 0:
            return 0
        else:
            True
    return 1







n = int(input('Enter the max more than 2: '))
start = time.time()
number = 1

for i in range(3, n+1):
      number += lprime(i)
            
       

print(number)
print('time taken:',time.time()-start)
            
            
            