def Quicksort(A,l,u):
    if(l<u):
        i=l+1
        j=u
        key=A[l]
        flag=1
        while(flag):
            while(A[i]<=key) and (i<=u):
                i+=1
            while(A[j]>key):
                j-=1
            if(i<j):
                A[i],A[j]=A[j],A[i]
                i+=1
                j-=1
            else:
                flag=0
        A[l],A[j]=A[j],A[l]
        Quicksort(A,l,j-1)
        Quicksort(A,j+1,u)
            


A=[56,3,72,2,9,5]
Quicksort(A,0,5)
print(A)

