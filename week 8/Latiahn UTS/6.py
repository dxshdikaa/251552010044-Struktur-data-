kata = "algoritma"

stack = []

for huruf in kata:
    stack.append(huruf)

terbalik = ""

while stack:
    terbalik += stack.pop()

print("Original :", kata)
print("Terbalik :", terbalik)