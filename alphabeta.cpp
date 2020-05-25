#include<bits/stdc++.h> 
using namespace std; 

int alphabeta(int a,int b,int d, int index, bool maxpl, vector<int> A)
{
    if(d==3)
    {
        return A[index];
    }

    if(maxpl==true)
    {

     int best = INT_MIN; 
  
        for (int i = 0; i < 2; i++) 
        { 
              
            int val = alphabeta(a,b,d+1,index*2+i,false,A); 
            best = max(best, val); 
            a = max(a, best); 
  
            // Alpha Beta Pruning 
            if (b <= a) 
                break; 
        } 
        return best; 
    } 
    else
    { 
        int best = INT_MAX; 
   
        for (int i = 0; i < 2; i++) 
        { 
            int val = alphabeta(a,b,d+1,index*2+i,true,A);  
            best = min(best, val); 
            b = min(b, best); 
  
            // Alpha Beta Pruning 
            if (b <= a) 
                break; 
        } 
        return best; 
    } 


}
int main() 
{ 
    vector<int> A({ 3, 5, 6, 9, 1, 2, 0, -1 }); 
    cout <<"The optimal value is : "<< alphabeta(INT_MIN,INT_MAX,0,0,true,A);
    return 0; 
} 