def Mergesort(arr):
    if(len(arr)>1):
        mid=len(arr)//2
        start=arr[:mid]
        end=arr[mid:]
        Mergesort(start)
        Mergesort(end)
        i=j=k=0    
        while(i<len(start) and j<len(end)):
            if(start[i]<end[j]):
                arr[k]=start[i]
                i+=1
            else:
                arr[k]=end[j]
                j+=1
            k+=1
        while(i<len(start)):
            arr[k]=start[i]
            i+=1
            k+=1
        while(j<len(end)):
            arr[k]=end[j]
            j+=1
            k+=1
        return(arr)
arr=[24,64,89,44,4,2,7,1]
Mergesort(arr)
