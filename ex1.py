# return the middle character of the word

def get_middle(s):
    a=len(s);
    if(a%2==0):
        return s[int(a/2)-1]+s[int(a/2)];
    else:
        return s[int((a-1)/2)];
        
 
#before update
def get_middle(s):
    return s[int((len(s)-1)/2):int(len(s)/2+1)];