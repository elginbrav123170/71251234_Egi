def C_to_F(C):
    f = ((9/5) * C) + 32
    return int(f)

def C_to_R(C):
    R = 0.8 * C
    return int(R)

C = int(input())
print(f"Input C = {C}. Output F = {C_to_F(C)}.")
print(f"Input C = {C}. Output R = {C_to_R(C)}.")