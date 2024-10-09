import random

text = "P1 \n100 100\n"

h = 100
w = 100

for height in range(0, h):
    for width in range(0, w):
        text += str(random.randint(0, 1)) + " "
    text += "\n"
    
with open("teste.pbm", "w") as file:
    file.write(text)
        
print(text)