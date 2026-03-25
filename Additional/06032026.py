N = int(input())
a = 0
S = 0
count = 0
i = 1
while count <= N:
    count += 1
    fac = 1
    for j in range(i+2, 0, -1): fac *= j
    a = (-1)**(count+1)*((i**(i+1)) / (fac * (i+4)**(-(i+5))))
    print(f"{(-1)**(count+1)}*(({i}**({i+1})) / ({i+2}! * ({i+4})**(-({i+5}))))")
    print(a)
    i += 6
    S += a
