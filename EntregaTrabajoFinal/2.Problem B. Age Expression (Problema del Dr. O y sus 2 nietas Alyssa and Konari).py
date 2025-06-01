B = input()
B = B.split()
if(int(B[0]) >= int(B[1])/2):
    print("E")
else:
    print("H")
    
C = input()
C = C.split()

C = input()
C = C.split()
AgeDr = int(C[0])
AgeA = int(C[1])
AgeK = int(C[2])

flag = False
for i in range(AgeDr + 1):
    for j in range(AgeDr +1):
        if(AgeA * i + AgeK * j == AgeDr):
            flag = True
            break
    if flag:
        break
if flag:
    print("1")
else:
    print("0")