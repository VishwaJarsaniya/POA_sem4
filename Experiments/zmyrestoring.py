def add(A,M):
    carry=0
    sum=''
    for i in range(len(A)-1,-1,-1):
        temp = int(A[i]) + int(M[i]) + carry
        if(temp>1):
            sum += str(temp%2)
            carry=1
        else:
            sum += str(temp)
            carry=0
    return sum[::-1]
    
def twoc(m):
    M=''
    for i in range(len(m)):
        M += str((int(m[i])+1)%2)
    M = add(M,'0001')
    return M

def restoring(Q,M,A):
    count=len(M)
    print("Initial values: A: ",A, " Q: ",Q ,"M: ",M)
    while(count):
        print(" \nStep:",len(M)-count+1, end="")
        print(" Left shift and subtract",end="")
        A = A[1:] + Q[0]
        comp_M = twoc(M)
        A = add(A,comp_M)
        print(" A: ",A)
        print(" A: ",A, "Q: ", Q[1:]+"_" , end="")
        if(A[0]=="1"):
            Q = Q[1:] + "0"
            print(" - MSB=1")
            A=add(A,M)
            print(" A: ",A , "Q: ",Q, "A=A+M")
        else:
            Q =Q[1:] + "1"
            print(" - MSB=0 ")
            print(" A: ",A,"Q: ",Q,"No restoration")
        count -= 1
    print("\n Quotient= ",Q, "Remainder= ",A)

dividend = "1101"
divisor = "0100"
accumulator = "0" * len(dividend)
restoring(dividend,divisor,accumulator)