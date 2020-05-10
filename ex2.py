#convert arr_binary to bin
def binary_array_to_number(a):
    x=0;
    t=1;
    for i in range(0,len(a)):
        x+=a[len(a)-i-1]*(t);
        t*=2;
    return x;
    
 #update
 def binary_array_to_number(a):
   return int(''.join(map(str,a)),2);