import sys
import shlex

class fibbonaci:
    
    fibarr = [0,1]
    
    def  __init__(self, val):
        self.name = "GANESHA VANDHANAM"
        self.nth = val
        
    
    def fib_recursive(self, k):
        if k == 0:
            return 0
        if k == 1:
            return 1
        return self.fib_recursive(k-1) +  self.fib_recursive(k-2)
    
    def fib(self , k):
       first = 0
       second = 1
       res = 0
       print(res)
       print(second)
       for i in range(1,k):
           
           res = first + second
           print(res)
           first = second
           second = res
           
    def fib_array(self , k):
       arr  = [0] * k
       arr[1] = 1
       for i in range( len(arr),-1):
           arr[i-2] = arr[i+1] + arr[i-2]
    
       print(arr)
    
    def fib_nth_dp(self, k):
        
        if len(self.fibarr) < 2:
         return print('Not a proper array')
     
        if k <0 :
            return print('Not a proper array')
        
        if k < len(self.fibarr):
            return self.fibarr[k]
        else:
            self.fibarr.append( self.fib_nth_dp(k-1)  +  self.fib_nth_dp(k-2))
            return self.fibarr[k]
    


def fibbonaci_method(k, memo = {}):
    if k <= 0: 
        return 0
    elif k==1:
        return 1
    elif k in memo:
        return memo[k]
    else:
        memo[k] = fibbonaci_method(k-1) + fibbonaci_method(k-2)
        return memo[k]

    
    
def fibonacci_1(n, memo={}):
	if n <= 0:
		return 0
	elif n == 1:
		return 1
	elif n in memo:
		return memo[n]
	else:
		memo[n] = fibonacci_1(n-1) + fibonacci_1(n-2)
		return memo[n]

# Driver Program



def main() -> int:
    """Echo the input arguments to standard output"""
    phrase = shlex.join(sys.argv)
    obj = fibbonaci(4)
    r = obj.fib_recursive(9)
    print(f'recursive results {r}')
    print(f'non-recursive results {r}')
    obj.fib(9)
    
    print(f'array results {r}')
    obj.fib_array(29)
    
    print(f'non-recursive array storing values and nth DP result ')
    #print(obj.fib_nth_dp(209))
    
    memo = fibbonaci_method(9)
    # for x,y in memo:
    #     print(f'{x , y} ')
    print(memo)
        
    print(fibonacci_1(9))
    
    return 0



if __name__ == '__main__':
    sys.exit(main())
    
    
    
            