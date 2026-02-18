A = int(input())
B = int(input())
C = int(input())


pos = 0
neg = 0

if A > 0:
    pos += 1
elif A <0:
    neg += 1
if B > 0:
    pos += 1
elif B < 0:
    neg += 1
if C > 0:
    pos +=1
elif C <0:
    neg += 1


print(pos, neg)