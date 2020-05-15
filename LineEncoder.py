import numpy as np
import matplotlib.pyplot as plt


print("Enter The Data Stream:")
d_s = input()
arr = list()
_index = list()
_no = len(d_s)
print("1.NRZ-L,2.NRZ-I,3.Manchaster,4.Differential-Manchester,5.AMI")
_choice = int(input())
if(_choice == 1):
    for i in d_s:
        _index.append(int(i))
        if(i=='1'):
            arr.append(1)
        else:
            arr.append(-1)

    axis_0 = np.repeat(range(len(arr)), 2)
    axis_0 = axis_0[1:]
    axis_0 = np.append(axis_0 , len(arr))
    axis_1 = np.repeat(arr, 2)
    plt.title("NRZ-L")
    plt.plot(axis_0,axis_1) 
    plt.ylim(-2,2)
    plt.xlim(0,len(arr))   
elif(_choice==2):
    if(arr==[]):
        arr.append(-1)
    for i in d_s:
        _index.append(int(i))
    
    i=1
    
    while(i<_no):
        if(int(_index[i])==0):
            arr.append(arr[i-1])
        else:
            arr.append(-arr[i-1])
        i=i+1    
    axis_0 = np.repeat(range(len(arr)), 2)
    axis_0 = axis_0[1:]
    axis_0 = np.append(axis_0 , len(arr))
    axis_1 = np.repeat(arr, 2)
    plt.title("NRZ-I")
    plt.plot(axis_0,axis_1) 
    plt.ylim(-2,2)
    plt.xlim(0,len(arr))
elif(_choice==3):
    for i in d_s:
        _index.append(int(i))
    for i in _index:
        if(i==0):
            arr.append(1*0.5)
            arr.append(-1*0.5)
        else:
            arr.append(-1*0.5)
            arr.append(1*0.5)       
          
    axis_0 = np.repeat(range(len(arr)), 2)
    axis_0 = axis_0[1:]
    axis_0 = np.append(axis_0 , len(arr))
    axis_1 = np.repeat(arr, 2)
    plt.title("Manchester")
    plt.plot(axis_0,axis_1) 
    plt.ylim(-2,2)
    plt.xlim(0,len(arr))
elif(_choice==4):
    if(arr==[]):
        arr.append(0.5)
        arr.append(-0.5)
    
    
    for i in d_s:
        _index.append(int(i))
    i=1
    j=1
    while(j<_no):
            if(_index[j]==1):
                arr.append(arr[i])
                arr.append(-(arr[i+1]))
            else:
                arr.append(-(arr[i]))
                arr.append(-arr[i+1]) 
            i=i+2
            j=j+1
        
    
    axis_0 = np.repeat(range(len(arr)), 2)
    axis_0 = axis_0[1:]
    axis_0 = np.append(axis_0 , len(arr))
    axis_1 = np.repeat(arr, 2)
    plt.title("Differential-Manchester")
    plt.plot(axis_0,axis_1) 
    plt.ylim(-2,2)
    plt.xlim(0,len(arr))
            
else:
    print("1.No Scrambling,2.Scrambling.")
    _choice1 = int(input())
    if(_choice1 == 1):
        for i in d_s:
            _index.append(int(i))
        index=0
        for i in range(len(_index)):
            if(_index[i]==0):
                 arr.append(0)
           
            else:
                if(1 not in arr):
                    arr.append(1)
                    index = i
                else:
                    arr.append(-arr[index])
                    index = i
                
        axis_0 = np.repeat(range(len(arr)), 2)
        axis_0 = axis_0[1:]
        axis_0 = np.append(axis_0 , len(arr))
        axis_1 = np.repeat(arr, 2)
        plt.title("AMI")
        plt.plot(axis_0,axis_1) 
        plt.ylim(-2,2)
        plt.xlim(0,len(arr))
    else:           
        print("Press 1 for B8ZS")
        _choice = int(input())
        index=0
        if(_choice==1):
             d_s = d_s.replace("00000000","000VB0VB")
             for i in range(len(d_s)):
                 if(d_s[i]=='0'):
                      arr.append(0)
                 else:
                    if(1 not in arr):
                       arr.append(1)
                       index = i
                    else:
                        if(d_s[i]=='V'):
                            arr.append(arr[index])
                            index = i
                        else:
                            arr.append(-arr[index])
                            index = i
                            
                  
             axis_0 = np.repeat(range(len(arr)), 2)
             axis_0 = axis_0[1:]
             axis_0 = np.append(axis_0 , len(arr))
             axis_1 = np.repeat(arr, 2)
             plt.title("B8ZS")
             plt.plot(axis_0,axis_1) 
             plt.ylim(-2,2)
             plt.xlim(0,len(arr))                               
        
        
   
    
    
   
            
                
            
       