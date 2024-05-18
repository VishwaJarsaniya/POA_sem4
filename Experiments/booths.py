# Conversion Function: Ensure both binary numbers have the same length
def conversion(a, count):
    return a.zfill(count) 

# Addition Function: Perform binary addition
def add(x, y):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)  # Pad with leading zeros
    y = y.zfill(max_len)  
    result = ''  # Final answer
    carry = 0
    for i in range(max_len - 1, -1, -1):
        r = carry
        if x[i] == '1':
            r += 1
        if y[i] == '1':
            r += 1
        if r % 2 == 1:
            result = "1" + result
        else:
            result = "0" + result
        if r < 2:
            carry = 0
        else:
            carry = 1
    return result.zfill(max_len)

# Two's Complement Function: Compute the two's complement of a binary number
def twoc(a):
    l = list(a)
    for i in range(len(l)):
        if l[i] == "1":
            l[i] = "0"
        else:
            l[i] = "1"
    b = "0" * (len(l) - 1) + "1"
    return add("".join(l), b)

# Right Shift Function: Simulate arithmetic right shift operation
def right_shift(ac, q, q1):
    a = ac[0]
    for i in range(1, len(ac)):
        a += ac[i - 1]
    b = ac[-1]
    for j in range(1, len(q)):
        b += q[j - 1]
    c = q[-1]
    return a, b, c

# Input: Prompt user for multiplicand and multiplier
x = int(input('Enter Multiplicand: '))
y = int(input('Enter Multiplier: '))

# Decimal to Binary Conversion
a = bin(x)[2:]
b = bin(y)[2:]

negative_a = 0
negative_b = 0

if x < 0:
    a = twoc(bin(-x)[2:])
    negative_a = 1
if y < 0:
    b = twoc(bin(-y)[2:])
    negative_b = 1

# Finding max length of the bits
count = max(len(a), len(b)) + 1

# Conversion and Two's Complement
firstP = conversion(a, count)
secondP = conversion(b, count)

firstN = twoc(firstP)
secondN = twoc(secondP)
print("Q= ",secondN)

# Multiplicand and Multiplier Selection
if negative_a == 0:
    M = firstP
    M2 = firstN
else:
    M = firstN
    M2 = firstP

if negative_b == 0:
    Q = secondP
else:
    Q = secondN

# Initialization
AC = conversion("0", count)
Q1 = "0"

# Output table header
print("The table for the Booth's algorithm is as follows:")
print("Count" + " " * count + "AC" + " " * count + "Q" + " " * count + "Q1" + " " * count + "Operation")
print(str(count) + " " * count + AC + " " * count + Q + " " * count + Q1 + " " * count + "initial")

# Booth's Algorithm Execution
while count > 0:
    compare = Q[-1] + Q1

    if compare[0] == compare[-1]:
        AC, Q, Q1 = right_shift(AC, Q, Q1)
        Op = "right shift"
    elif compare == "10":
        AC = add(AC, M2)
        AC, Q, Q1 = right_shift(AC, Q, Q1)
        Op = "AC=AC-M and right shift"
    elif compare == "01":
        AC = add(AC, M)
        AC, Q, Q1 = right_shift(AC, Q, Q1)
        Op = "AC=AC+M and right shift"

    # Output table rows
    print(str(count) + " " * count + AC + " " * count + Q + " " * count + Q1 + " " * count + Op)
    count -= 1

# Final Answer
answer = AC + Q

if negative_a == negative_b:
    ans_d = str(int(answer, 2))
else:
    ans_d = "-" + str(int(twoc(answer), 2))

print("Binary answer: " + answer)
print("Decimal conversion: " + ans_d)
