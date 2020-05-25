maximum = 1000000
minimum = -1000000

def alphabeta( a, b, d, index, maxpl,A):
    if(d==3):
        return A[index]

    if(maxpl==True):
        ans = minimum
        for i in range(0,2):
            val = alphabeta(a,b,d+1,index*2+i,False,A)
            ans = max(ans, val) 
            a = max(a, ans) 
            if (b <= a):
                break
        return ans
    
    else:
        ans = maximum
        for i in range(0,2):
            val = alphabeta(a,b,d+1,index*2+i,True,A)
            ans = min(ans, val) 
            a = min(a, ans) 
            if (b <= a):
                break
        return ans


                
if __name__ == "__main__":

    A = [3, 5, 6, 9, 1, 2, 0, -1]
    print(alphabeta(minimum,maximum,0,0,True,A))