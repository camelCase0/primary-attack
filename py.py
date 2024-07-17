import math
from progress.bar import Bar # type: ignore

n = int(input("n: ")) #439 31
q = int(input("q: ")) # mod 6833 
d = int(input("d: ")) # 142
# n = 439
# q = 6833
# d = 142


res = []
with Bar('Processing...', max=10000) as bar:
    for m in range(1, 10000):
        bar.next()
        t = n+m+1
        for b in range(200,t):
            s = (((math.pi * b))**(1/b))*(b/(2*math.pi*math.e))
            s = s**(1/(2*(b-1)))
            
            l = ((2*d+1)*math.sqrt(b/3))
            r = ((s**(2*b-t))*(q**(m/t)))
            #print(f'{l}|{r}')
            if ( l<= r):
                res.append(b)
minn = min(res)
if res:
    print(f'min = {minn}')
t = 2**(0.292*minn)
print(f"T = {t}")
print(f"Log = {math.log2(t)}")
