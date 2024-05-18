def conversion(a,count):
    q=""
    current = len(a)
    temp = count - current
    if current != count:
        q = "0" *temp  + a
    return q

def add(x,y):
    max_length = max(len(x),len(y))
    result =''
    carry = 0
    for i in range (max_length-1, -1, -1):
        r=carry
        if x[i]=="1":
            r += 1
        if y[i]=="1":
            r += 1
        if r%2 == 1:
            result = "1" + result
        else:
            result = "0" + result
        if r<2:
            carry=0
        else:
            carry=1
    return result

def twoc(a):
    l = list(a)
    for i in range (len(l)):
        if l[i]=="1":
            l[i]="0"
        else:
            l[i]="1"
    b = "0"*(len(l)-1) + "1"
    return add("".join(l),b)

def right_shift(ac,q,q1):
    a=ac[0]
    for i in range (1,len(ac)):
        a += ac[i-1]
    b=ac[-1]
    for j in range (1,len(q)):
        b += q[j-1]
    c=q[-1]
    return a,b,c

x = int(input("Enter multiplicand: "))
y = int(input("Enter multiplier : "))

a = bin(x)[2:]
b = bin(y)[2:]

negative_a = 0
negative_b = 0

if a[0]=="-":
    a=a[1:]
    negative_a=1
if b[0]=="-":
    b=b[1:]
    negative_b=1

count = max(len(a),len(b)) + 1

firstP = conversion(a,count)
secondP = conversion(b,count)
firstN = twoc(firstP)
secondN = twoc(secondP)

if negative_a==0:
    M = firstP
    M2 = firstN
else:
    M = firstN
    M2 = firstP
if negative_b==0:
    Q = secondP
else:
    Q = secondN


AC = conversion("0",count)
Q1 = "0"

print("Count" + " "*count + "AC" + " "*count + "Q" + " "*count + "Q1" + " "*count + "Operation")
print(str(count) + " "*count + AC + " "*count + Q + " "*count + Q1 + " "*count + "initial")

while count>0:
    compare = Q[-1] + Q1

    if compare[0]==compare[-1]:
        AC, Q, Q1 = right_shift(AC, Q, Q1)
        op = "arithmetic right shift"

    elif compare == "10":
        AC = add(AC, M2)
        AC, Q, Q1 = right_shift(AC, Q, Q1)
        op = "AC=AC-M & arithmetic right shift"

    elif compare == "01":
        AC = add(AC, M)
        AC, Q, Q1 = right_shift(AC, Q, Q1)
        op = "AC=AC+M & arithmetic right shift"

    print(str(count) + " "*count + AC + " "*count + Q + " "*count + Q1 + " "*count + op)
    count -=1

answer = AC + Q

if negative_a == negative_b:
    ans_d = str(int(answer,2))
else:
    ans_d = "-" + str(int(twoc(answer),2))


print("Binary ans = " + answer)
print("Decimal ans = " + ans_d)

