#trong mảng chỉ có 1 số là odd hoặc 1 số là even, tìm nó
def find_outlier(i):
    ok=0;
    for a in i:
        if(a%2==0):
            ok+=1;
    if(ok==1):
        for a in i:
            if a%2==0:
                return a;
    else:
        for a in i:
            if a%2!=0:
                return a;
        
#update
    def find_outlier(int):
        odds = [x for x in int if x%2!=0]
        evens= [x for x in int if x%2==0]
        return odds[0] if len(odds)<len(evens) else evens[0]