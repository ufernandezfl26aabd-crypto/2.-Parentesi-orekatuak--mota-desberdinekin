katea = "{[()]}"
pila = []

for i in katea:
    if i == "(":
        pila.append(i)
    if i == ")":
        pila.pop()

print("True")