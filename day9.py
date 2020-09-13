#GENETOR

def k(l,v):
    for  num in range(l,v+1):
        t=num
        sum=0
        while t >0:
            x=t%10
            c=x*x*x
            sum+=c
            t=t//10
            if (num == sum):
                yield(sum)
print(list(k(1,1000)))



#UNIT TEXTING





import unittest
import prime

class prime_np(unittest.TestCase):
    def test(self):
        
        Number=11
        result=prime.isprime(Number)
        self.assertEqual(result,Number)
    def test_k(self):
        
        num=199
        res=prime.isprime(num)
        self.assertEqual(res,num)
if __name__ == "__main__":
    unittest.main()
