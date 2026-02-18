# Demonstrer en liste og hvordan man manipulerer den.
L = ["hej", 1, 1.76]
print(L)

for el in L:
    if isinstance(el,int):
        print(el)

L.append("success")

print(L)