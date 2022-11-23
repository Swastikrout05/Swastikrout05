def iterative(n, cur):
    stack={} # used to store the calculations that need to be computed 
    stack[0]=(n,cur) #store the first call in the stack 
    result=0
    i=1
    # While there is a calculation that needs to be caculated/ if there is something in the stack
    while  not len(stack)==0:
        n , cur = stack.pop(i-1)
        # Pop the values from the stack 

        if (not cur): # if teh cur !=1 then we will go in here
            cur=0
        if (n<2):
            continue 
        
        # if we have calculated the score we then continue to adderss other calculations
        # no need to continue to add to the stack by interpreting further.
        if (n==2):
            result+= (1/n+cur) 
            continue
        #  act as a recursive call , by adding it to the stack 
        stack[i]=(n-1, cur+1/(n*(n-1)))
        i+=1
    return result

