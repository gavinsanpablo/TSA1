A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'i', 'j', 'k'}

print(f"Elements in A: {len(A)}")
print(f"Elements in B: {len(B)}")

print(f"Elements in B not in A and C: {len((B - A) & (B - C))}")

print(f"i. [h, i, j, k]: {C - A - B}")
print(f"ii. [c, d, f]: {A & C}")
print(f"iii. [b, c, h]: {A & B}")
print(f"iv. [d, f]: {(A & C) - B}")
print(f"v. [c]: {A & B & C}")
print(f"vi. [l, m, o]: {B - A - C}")