
N = int(input())

S = 0
for i in range(1, N+1):
    print(f"{S} = {((-1)**i+1)} * {1**(N-i+1)} / {(N-i+1)}**{(i)}")
    S += ((-1)**(i+1)) * i**(N-i+1) / (N-i+1)**i

print(S)