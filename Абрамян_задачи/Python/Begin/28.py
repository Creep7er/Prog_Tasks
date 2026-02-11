A = int(input("A: "))

temp = A * A 
print(f"A^2 = {temp}")

temp2 = temp * A 
print(f"A^3 = {temp2}")

temp = temp * temp2
print(f"A^5 = {temp}")

temp = temp * temp
print(f"A^10 = {temp}")

temp = temp * temp2
print(f"A^15 = {temp}")
