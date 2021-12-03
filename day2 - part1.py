horizontal = []
depth = []

with open('advent_input_2.txt') as file:
    lines = file.readlines()
    
    for i in range(len(lines)):
        for word in str(lines[i]).split():
            if word.isdigit() and "forward" in str(lines[i]):
                horizontal.append(int(word))
    
print(sum(horizontal))
print(horizontal)

for i in range(len(lines)):
        for word in str(lines[i]).split():
            if word.isdigit() and "up" in str(lines[i]):
                depth.append(-int(word))
            if word.isdigit() and "down" in str(lines[i]):
                depth.append(int(word))
    
print(sum(depth))
print(depth)
