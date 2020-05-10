#Given an array, find the integer that appears an odd number of times.
def find_it(s):
    for i in range(0,len(s)):
        temp=s[i];
        cout=0;
        for i in range(0,len(s)):
            if(s[i]==temp):
                cout+=1
        if(cout%2!=0):
            return temp

#update
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i