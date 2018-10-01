#PF-Assgn-26

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    
    rabbit_count = (legs//2)-heads
    chicken_count = heads-rabbit_count
    if(legs%2!=0 and heads>legs):
        print(error_msg)
    else:
        print(chicken_count,rabbit_count)    
    
solve(20,100)
